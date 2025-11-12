
#include "llvm/IR/Function.h"
#include "llvm/IR/PassManager.h"
#include "llvm/Passes/PassBuilder.h"
#include "llvm/Passes/PassPlugin.h"
#include "llvm/Support/raw_ostream.h"
#include "llvm/IR/Instructions.h"
#include "llvm/IR/InstrTypes.h"
#include "llvm/IR/CFG.h"
#include "llvm/Analysis/LoopInfo.h"
#include "llvm/IR/Dominators.h"

#include <map>
#include <string>


using namespace llvm;

struct FuncAnalysisPass : public PassInfoMixin<FuncAnalysisPass> {
  PreservedAnalyses run(Function &F, FunctionAnalysisManager &FAM) {
    // Print to stderr so we definitely see it
    errs() << "\n[FuncAnalysisPass] on function: " << F.getName() << "\n";

    DominatorTree DT(F);
    DT.recalculate(F);

    LoopInfo &LI = FAM.getResult<LoopAnalysis>(F);

    unsigned BBcount = 0, Instcount= 0, loads=0, stores=0;
    std::map<std::string, unsigned> opcodeCounts;
    std::map<std::string, unsigned> callCounts;

    // --- 1. Count BBs, instructions, opcode breakdown, loads/stores, calls ---
    for (auto &BB : F) {
      ++BBcount;
      Instcount += BB.size();
      const auto *Node = DT.getNode(&BB);
      if (Node && Node->getIDom())
          errs() << "  Immediate Dominator: " << Node->getIDom()->getBlock()->getName() << "\n";
      else
          errs() << "  Immediate Dominator: (entry block)\n";

      errs() << "  Dominates: ";
      for (auto *Child : *Node) {
          if (!Child->getBlock()->hasName())
              Child->getBlock()->setName("bb_dom_" + std::to_string(BBcount++));
          errs() << Child->getBlock()->getName() << " ";
      }
      errs() << "\n";


      for (auto &I : BB) {
            opcodeCounts[I.getOpcodeName()]++;

            if (isa<LoadInst>(&I)) loads++;
            if (isa<StoreInst>(&I)) stores++;

            if (auto *callInst = dyn_cast<CallBase>(&I)) {
                if (Function *calledFunc = callInst->getCalledFunction()) {
                    callCounts[calledFunc->getName().str()]++;
                    errs() << "    Calls function: " << calledFunc->getName() << "\n";
                }
            }
      }
    }

    // 2. Loop Detection using LoopAnalysis

    outs() << "Loops in function: " << std::distance(LI.begin(), LI.end()) << "\n";
    unsigned loopCount = 0;
    for (auto *L : LI) {
        BasicBlock *Header = L->getHeader();
        if (!Header->hasName())
            Header->setName("loop_header_" + std::to_string(loopCount));
        errs() << "  Loop " << loopCount
           << " header: " << Header->getName()
           << " (depth=" << L->getLoopDepth() << ")\n";
        loopCount++;
    }


    // 3. Print CFG edges
    for (auto &BB : F) {
        if (!BB.hasName())
            BB.setName("bb_" + F.getName() + "_" + std::to_string(BBcount++));

        errs() << "  BasicBlock " << BB.getName() << " successors: ";
        const Instruction *T = BB.getTerminator();
        for (unsigned i = 0; i < T->getNumSuccessors(); ++i) {
            BasicBlock *Succ = T->getSuccessor(i);
            if (!Succ->hasName())
                Succ->setName("succ_" + std::to_string(i));
            errs() << Succ->getName() << " ";
        }
        errs() << "\n";
    }

    errs() << "  Function: " << F.getName()
           << " | BasicBlocks: " << BBcount
           << " | Instructions: " << Instcount
           << " | Load Instructions: " << loads
           << " | Store Instructions: " << stores 
           << " | Loops: " << loopCount << "\n";

    // --- 5. Instruction breakdown ---
    errs() << "  Instruction breakdown:\n";
        for (auto &entry : opcodeCounts) {
            outs() << "    " << entry.first << ": " << entry.second << "\n";
        }

    // --- 6. Call counts ---
        errs() << "  Calls:\n";
        for (auto &entry : callCounts)
            errs() << "    " << entry.first << ": " << entry.second << "\n";

    errs().flush();
    return PreservedAnalyses::all();
  }
   // Run even if functions have optnone 
   //A required pass is a pass that may not be skipped. An example of a required pass
   //is AlwaysInlinerPass, which must always be run to preserve alwaysinline semantics. 
   //Pass managers are required since they may contain other required passes. An example
   //of how a pass can be skipped is the optnone function attribute, which specifies that
   //optimizations should not be run on the function. Required passes will still be run on
   //optnone functions.


  static bool isRequired() { return true; }
};


// Register plugin
extern "C" LLVM_ATTRIBUTE_WEAK PassPluginLibraryInfo llvmGetPassPluginInfo() {
  // This line confirms the .dylib was loaded.
  errs() << "FuncAnalysisPass plugin loaded!\n";

  return {
    LLVM_PLUGIN_API_VERSION, "FuncAnalysisPass", "v0.1",
    [](PassBuilder &PB) {
      // 1) Allow `-passes="func-analysis"` at *module* level by adapting to function pass
      PB.registerPipelineParsingCallback(
        [](StringRef Name, ModulePassManager &MPM,
           ArrayRef<PassBuilder::PipelineElement>) {
          if (Name == "func-analysis") {
            errs() << "FuncAnalysisPass added to module pipeline\n";
            MPM.addPass(createModuleToFunctionPassAdaptor(FuncAnalysisPass()));
            return true;
          }
          return false;
        });

      // 2) Also allow `-passes="function(func-analysis)"`
      PB.registerPipelineParsingCallback(
        [](StringRef Name, FunctionPassManager &FPM,
           ArrayRef<PassBuilder::PipelineElement>) {
          if (Name == "func-analysis") {
            errs() << "FuncAnalysisPass added to function pipeline\n";
            FPM.addPass(FuncAnalysisPass());
            return true;
          }
          return false;
        });
    }
  };
}
