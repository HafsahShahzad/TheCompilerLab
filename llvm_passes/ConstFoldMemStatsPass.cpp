
#include "llvm/IR/PassManager.h"
#include "llvm/Passes/PassBuilder.h"
#include "llvm/Passes/PassPlugin.h"

#include "llvm/IR/Function.h"
#include "llvm/IR/Module.h"
#include "llvm/IR/Instructions.h"
#include "llvm/IR/InstrTypes.h"
#include "llvm/IR/CFG.h"
#include "llvm/IR/Constants.h"
#include "llvm/IR/DataLayout.h"

#include "llvm/Analysis/TargetLibraryInfo.h"
#include "llvm/Analysis/ConstantFolding.h"   // ConstantFoldInstruction

#include "llvm/Support/raw_ostream.h"

#include <map>
#include <string>
#include <vector>

using namespace llvm;

namespace {

struct ConstFoldMemStatsPass : public PassInfoMixin<ConstFoldMemStatsPass> {
  PreservedAnalyses run(Function &F, FunctionAnalysisManager &FAM) {
    errs() << "\n[constfold-memstats] Function: " << F.getName() << "\n";

    const DataLayout &DL = F.getParent()->getDataLayout();
    TargetLibraryInfo &TLI = FAM.getResult<TargetLibraryAnalysis>(F);

    // 1) Constant folding sweep 
    // We only do a simple, safe fold using ConstantFoldInstruction.
    // We don't try aggressive simplify that needs DT/AC, etc.
    unsigned NumFolded = 0;
    std::vector<Instruction*> ToErase;

    for (auto &BB : F) {
      for (auto &I : BB) {
        // Only fold if the instruction produces a value (non-void)
        if (I.getType()->isVoidTy()) continue;

        if (Constant *C = ConstantFoldInstruction(&I, DL, &TLI)) {
          // Replace all uses with folded constant and mark for erasure.
          I.replaceAllUsesWith(C);
          ToErase.push_back(&I);
          ++NumFolded;
        }
      }
    }

    for (Instruction *I : ToErase)
      I->eraseFromParent();

    errs() << "  Constant-folded instructions: " << NumFolded << "\n";

    // 2) Memory access statistics
    struct MemAgg {
      uint64_t Loads = 0, Stores = 0;
      uint64_t LoadBytes = 0, StoreBytes = 0;
      uint64_t Volatile = 0, Atomic = 0;
    };

    // Overall totals
    MemAgg Tot;

    // Per address-space aggregation (useful on GPUs/accelerators/custom ISAs)
    std::map<unsigned, MemAgg> ByAS;

    auto addLoad = [&](LoadInst *LI) {
      Type *VTy = LI->getType();
      uint64_t sz = DL.getTypeStoreSize(VTy);
      unsigned AS = LI->getPointerAddressSpace();

      ++Tot.Loads; Tot.LoadBytes += sz;
      auto &A = ByAS[AS];
      ++A.Loads; A.LoadBytes += sz;
      if (LI->isVolatile()) { ++Tot.Volatile; ++A.Volatile; }
      if (LI->isAtomic())   { ++Tot.Atomic;   ++A.Atomic;   }
    };

    auto addStore = [&](StoreInst *SI) {
      Type *VTy = SI->getValueOperand()->getType();
      uint64_t sz = DL.getTypeStoreSize(VTy);
      unsigned AS = SI->getPointerAddressSpace();

      ++Tot.Stores; Tot.StoreBytes += sz;
      auto &A = ByAS[AS];
      ++A.Stores; A.StoreBytes += sz;
      if (SI->isVolatile()) { ++Tot.Volatile; ++A.Volatile; }
      if (SI->isAtomic())   { ++Tot.Atomic;   ++A.Atomic;   }
    };

    // 3. alignment histogram (bytes)
    std::map<unsigned, uint64_t> AlignHist; // align -> count

    for (auto &BB : F) {
      for (auto &I : BB) {
        if (auto *LI = dyn_cast<LoadInst>(&I)) {
          addLoad(LI);
          unsigned A = LI->getAlign().value();
          AlignHist[A]++;
        } else if (auto *SI = dyn_cast<StoreInst>(&I)) {
          addStore(SI);
          unsigned A = SI->getAlign().value();
          AlignHist[A]++;
        }
      }
    }

    // Print summary
    errs() << "  Memory accesses (overall):\n";
    errs() << "    Loads:  " << Tot.Loads  << "  (" << Tot.LoadBytes  << " bytes)\n";
    errs() << "    Stores: " << Tot.Stores << "  (" << Tot.StoreBytes << " bytes)\n";
    errs() << "    Volatile ops: " << Tot.Volatile << "\n";
    errs() << "    Atomic ops:   " << Tot.Atomic   << "\n";

    if (!ByAS.empty()) {
      errs() << "  By address space:\n";
      for (auto &kv : ByAS) {
        unsigned AS = kv.first;
        const MemAgg &A = kv.second;
        errs() << "    AS" << AS
               << "  Loads="  << A.Loads  << " (" << A.LoadBytes  << "B)"
               << "  Stores=" << A.Stores << " (" << A.StoreBytes << "B)"
               << "  Vol="    << A.Volatile
               << "  Atom="   << A.Atomic << "\n";
      }
    }

    if (!AlignHist.empty()) {
      errs() << "  Alignment histogram (bytes -> count):\n";
      for (auto &kv : AlignHist) {
        errs() << "    " << kv.first << " -> " << kv.second << "\n";
      }
    }

    // We modified IR only by replacing folded instructions with constants.
    // That does not change analyses we don't query here, but be conservative:
    return NumFolded ? PreservedAnalyses::none() : PreservedAnalyses::all();
  }

  static bool isRequired() { return true; }
};

} // namespace

// -------- Plugin registration --------
extern "C" LLVM_ATTRIBUTE_WEAK PassPluginLibraryInfo llvmGetPassPluginInfo() {
  return {
    LLVM_PLUGIN_API_VERSION, "ConstFoldMemStats", "v0.1",
    [](PassBuilder &PB) {
      PB.registerPipelineParsingCallback(
        [](StringRef Name, FunctionPassManager &FPM,
           ArrayRef<PassBuilder::PipelineElement>) {
          if (Name == "constfold-memstats") {
            FPM.addPass(ConstFoldMemStatsPass());
            return true;
          }
          return false;
        });
    }
  };
}

