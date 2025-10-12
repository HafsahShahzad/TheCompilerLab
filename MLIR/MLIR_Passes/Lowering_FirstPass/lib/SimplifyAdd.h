#ifndef SIMPLIFY_ADD_H
#define SIMPLIFY_ADD_H

#include "mlir/Pass/Pass.h"
#include "mlir/Dialect/Func/IR/FuncOps.h"

namespace mlir {
  std::unique_ptr<mlir::Pass> createSimplifyAddPass();
  void registerSimplifyAddPass();
}
#endif 
