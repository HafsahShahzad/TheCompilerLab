#include "SimplifyAdd.h"         // your new header (adjust path if needed)

#include "mlir/IR/PatternMatch.h"
#include "mlir/Pass/Pass.h"
#include "mlir/Dialect/Func/IR/FuncOps.h"
#include "mlir/Dialect/Arith/IR/Arith.h"
#include "mlir/Transforms/GreedyPatternRewriteDriver.h"
#include "mlir/IR/Dialect.h"
#include "mlir/Dialect/LLVMIR/LLVMDialect.h" // check here: /opt/homebrew/opt/llvm/include/mlir/Dialect/LLVMIR

using namespace mlir;
// Pattern: arith.addf %x, 0.0 -> %x
struct AddZeroSimplify : public OpRewritePattern<arith::AddFOp> {
  using OpRewritePattern<arith::AddFOp>::OpRewritePattern;

  LogicalResult matchAndRewrite(arith::AddFOp op,
                                PatternRewriter &rewriter) const override {
    auto lhs = op.getOperand(0);

    // canonicalization patterns ensure the constant is on the right, if there is a constant
    // See https://mlir.llvm.org/docs/Canonicalization/#globally-applied-rules
    auto rhs = op.getOperand(1);
    auto rhsDefiningOp = rhs.getDefiningOp<arith::ConstantOp>();
    if (!rhsDefiningOp) {
      return failure();
    }
    auto attr = mlir::dyn_cast<FloatAttr>(rhsDefiningOp.getValue());
    if (!attr) return failure();
    if (attr.getValueAsDouble() == 0.0) {
      rewriter.replaceOp(op, lhs);
      return success();
    }
    return failure();

  }
};

//To be able to do this optimization on LLVM emit MLIR, we need to catch the pattern after lowering as well
struct LLVMAddZeroSimplify : public OpRewritePattern<LLVM::FAddOp> {
  using OpRewritePattern<LLVM::FAddOp>::OpRewritePattern;

  LogicalResult matchAndRewrite(LLVM::FAddOp op,
                                PatternRewriter &rewriter) const override {
    auto lhs = op.getOperand(0);
    auto rhs = op.getOperand(1);

    // Match a constant 0.0
    if (auto constOp = dyn_cast_or_null<LLVM::ConstantOp>(rhs.getDefiningOp())) {
      if (auto floatAttr = dyn_cast<FloatAttr>(constOp.getValue())) {
        if (floatAttr.getValueAsDouble() == 0.0) {
          rewriter.replaceOp(op, lhs);
          return success();
        }
      }
    }
    return failure();
  }
};

//All passes in MLIR derive from OperationPass 
struct SimplifyAddPass
    : public PassWrapper<SimplifyAddPass, OperationPass<ModuleOp>> {

  void runOnOperation() override {
    RewritePatternSet patterns(&getContext());
    patterns.add<AddZeroSimplify>(&getContext());
    patterns.add<LLVMAddZeroSimplify>(&getContext()); // llvm
    (void)applyPatternsGreedily(getOperation(), std::move(patterns));
  }
  StringRef getArgument() const final { return "simplify-add"; }
  StringRef getDescription() const final { return "Simplify x + 0.0 -> x"; }

};
// Legacy registration — works with Homebrew MLIR
namespace {
  PassRegistration<SimplifyAddPass> pass;
}

namespace mlir {
  void registerSimplifyAddPass() {
    PassRegistration<SimplifyAddPass>();
  }
}


// Factory function definition
std::unique_ptr<mlir::Pass> mlir::createSimplifyAddPass() {
  return std::make_unique<SimplifyAddPass>();
}

