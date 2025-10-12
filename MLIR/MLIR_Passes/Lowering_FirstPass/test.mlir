func.func @add_example(%arg0: f32) -> f32 {
  %c0 = arith.constant 0.0 : f32
  %res = arith.addf %arg0, %c0 : f32
  return %res : f32
}
func.func @main(%arg0: i32) -> i32 {
  %0 = math.ctlz %arg0 : i32
  func.return %0 : i32
}
