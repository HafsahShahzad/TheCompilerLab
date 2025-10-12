#include "mlir/IR/MLIRContext.h"
#include "mlir/IR/Dialect.h"
#include "mlir/Pass/PassManager.h"
#include "mlir/Pass/PassRegistry.h"
#include "mlir/Parser/Parser.h"
#include "mlir/InitAllDialects.h"
#include "mlir/Tools/mlir-opt/MlirOptMain.h"
#include "mlir/Conversion/Passes.h"
#include "mlir/Conversion/FuncToLLVM/ConvertFuncToLLVMPass.h"
#include "mlir/Conversion/ControlFlowToLLVM/ControlFlowToLLVM.h"
#include "mlir/Dialect/LLVMIR/LLVMDialect.h"

// Include your pass header
#include "../lib/SimplifyAdd.h"

using namespace mlir;

int main(int argc, char **argv) {
  // Create a registry and register all MLIR dialects
  DialectRegistry registry;
  registry.insert<mlir::arith::ArithDialect,
                mlir::func::FuncDialect,
                mlir::math::MathDialect,
                LLVM::LLVMDialect>();
  mlir::registerConvertFuncToLLVMPass();
  mlir::registerConvertControlFlowToLLVMPass();

  // Configure mlir-opt to run your pass
  MlirOptMainConfig config;
  config.setPassPipelineSetupFn([](PassManager &pm) -> LogicalResult {
      pm.addPass(createSimplifyAddPass());
      return success();
  });

  // Run mlir-opt main with CLI arguments
  return asMainReturnCode(MlirOptMain(argc, argv, "simplify-add-opt", registry));
}
