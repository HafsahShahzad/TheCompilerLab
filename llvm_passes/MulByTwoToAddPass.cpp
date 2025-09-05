
#include "llvm/IR/Function.h"
#include "llvm/IR/PassManager.h"
#include "llvm/Passes/PassBuilder.h"
#include "llvm/Passes/PassPlugin.h"
#include "llvm/Support/raw_ostream.h"
#include "llvm/IR/Instructions.h"
#include "llvm/IR/IRBuilder.h"

using namespace llvm;

struct MulByTwoToAddPass : public PassInfoMixin<MulByTwoToAddPass> {
    // Main entry point, takes IR unit to run the pass on (&F) and the
    // corresponding pass manager (to be queried if need be)
    PreservedAnalyses run(Function &F, FunctionAnalysisManager &) {
        bool Changed = false;

        for (auto &BB : F) {
            for (auto Inst = BB.begin(), E = BB.end(); Inst != E;) {
                Instruction *I = &*Inst++;

                // Look for binary operators
                if (auto *BinOp = dyn_cast<BinaryOperator>(I)) {
                    if (BinOp->getOpcode() == Instruction::Mul) {
                        Value *Op1 = BinOp->getOperand(0);
                        Value *Op2 = BinOp->getOperand(1);

                        // Case: x * 2
                        if (auto *C = dyn_cast<ConstantInt>(Op2)) {
                            if (C->equalsInt(2)) {
                                IRBuilder<> Builder(BinOp);
                                Value *NewAdd = Builder.CreateAdd(Op1, Op1, "mul_by_2_as_add");
                                BinOp->replaceAllUsesWith(NewAdd);
                                errs() << "[MulByTwoToAddPass] Replaced '"
                                       << *BinOp << "' with '" << *NewAdd
                                       << "' in function " << F.getName() << "\n";
                                BinOp->eraseFromParent();
                                Changed = true;
                                continue;
                            }
                        }

                        // Case: 2 * x
                        if (auto *C = dyn_cast<ConstantInt>(Op1)) {
                            if (C->equalsInt(2)) {
                                IRBuilder<> Builder(BinOp);
                                Value *NewAdd = Builder.CreateAdd(Op2, Op2, "mul_by_2_as_add");
                                BinOp->replaceAllUsesWith(NewAdd);
                                errs() << "[MulByTwoToAddPass] Replaced '"
                                       << *BinOp << "' with '" << *NewAdd
                                       << "' in function " << F.getName() << "\n";
                                BinOp->eraseFromParent();
                                Changed = true;
                                continue;
                            }
                        }
                    }
                }
            }
        }

        if (Changed)
            return PreservedAnalyses::none();
        return PreservedAnalyses::all();
    }

    // Without isRequired returning true, this pass will be skipped for functions
    // decorated with the optnone LLVM attribute. Note that clang -O0 decorates
    // all functions with optnone.
    static bool isRequired() { return true; }
}; //Note!! close struct properly with semicolon!


// Register plugin 
// This is the core interface for pass plugins. It guarantees that 'opt' will
// be able to recognize MulByTwoToAddPass when added to the pass pipeline on the
// command line, i.e. via '-passes=MulByTwoToAddPass'
extern "C" LLVM_ATTRIBUTE_WEAK PassPluginLibraryInfo llvmGetPassPluginInfo() {
    return {
    //-----------------------------------------------------------------------------
    // New PM Registration
    //-----------------------------------------------------------------------------
        LLVM_PLUGIN_API_VERSION, "MulByTwoToAddPass", "v0.1",
        [](PassBuilder &PB) {
            PB.registerPipelineParsingCallback(
                [](StringRef Name, FunctionPassManager &FPM,
                   ArrayRef<PassBuilder::PipelineElement>) {
                    if (Name == "mul-to-add") {
                        FPM.addPass(MulByTwoToAddPass());
                        return true;
                    }
                    return false;
                });
        }
    };
}

