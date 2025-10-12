module {
  // x + 0.0 → should be simplified
  func.func @add_zero(%arg0: f32) -> f32 {
    %c0 = arith.constant 0.0 : f32
    %0 = arith.addf %arg0, %c0 : f32
    return %0 : f32
  }

  // x + 1.0 → should remain unchanged
  func.func @add_nonzero(%arg0: f32) -> f32 {
    %c1 = arith.constant 1.0 : f32
    %0 = arith.addf %arg0, %c1 : f32
    return %0 : f32
  }

  // Nested addition: (x + 0.0) + 0.0 → inner and outer should simplify
  func.func @nested_add(%arg0: f32) -> f32 {
    %c0 = arith.constant 0.0 : f32
    %0 = arith.addf %arg0, %c0 : f32
    %1 = arith.addf %0, %c0 : f32
    return %1 : f32
  }

  // Mixed: x + 0.0 + 1.0 → only the +0.0 should simplify
  func.func @mixed_add(%arg0: f32) -> f32 {
    %c0 = arith.constant 0.0 : f32
    %c1 = arith.constant 1.0 : f32
    %0 = arith.addf %arg0, %c0 : f32
    %1 = arith.addf %0, %c1 : f32
    return %1 : f32
  }
}
