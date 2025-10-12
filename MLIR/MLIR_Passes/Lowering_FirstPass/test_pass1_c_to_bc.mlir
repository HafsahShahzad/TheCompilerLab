module attributes {dlti.dl_spec = #dlti.dl_spec<!llvm.ptr = dense<64> : vector<4xi64>, i1 = dense<8> : vector<2xi64>, i128 = dense<128> : vector<2xi64>, !llvm.ptr<272> = dense<64> : vector<4xi64>, i64 = dense<64> : vector<2xi64>, f16 = dense<16> : vector<2xi64>, !llvm.ptr<271> = dense<32> : vector<4xi64>, f64 = dense<64> : vector<2xi64>, !llvm.ptr<270> = dense<32> : vector<4xi64>, f128 = dense<128> : vector<2xi64>, i32 = dense<32> : vector<2xi64>, i8 = dense<8> : vector<2xi64>, i16 = dense<16> : vector<2xi64>, "dlti.stack_alignment" = 128 : i64, "dlti.endianness" = "little">, llvm.ident = "Homebrew clang version 20.1.8"} {
  llvm.func @add_zero(%arg0: f32 {llvm.noundef}) -> f32 attributes {frame_pointer = #llvm.framePointerKind<"non-leaf">, no_inline, no_unwind, optimize_none, passthrough = ["ssp", ["uwtable", "1"], ["no-trapping-math", "true"], ["stack-protector-buffer-size", "8"], ["target-cpu", "apple-m1"]], target_cpu = "apple-m1", target_features = #llvm.target_features<["+aes", "+altnzcv", "+ccdp", "+ccidx", "+ccpp", "+complxnum", "+crc", "+dit", "+dotprod", "+flagm", "+fp-armv8", "+fp16fml", "+fptoint", "+fullfp16", "+jsconv", "+lse", "+neon", "+pauth", "+perfmon", "+predres", "+ras", "+rcpc", "+rdm", "+sb", "+sha2", "+sha3", "+specrestrict", "+ssbs", "+v8.1a", "+v8.2a", "+v8.3a", "+v8.4a", "+v8a", "+zcm", "+zcz"]>} {
    %0 = llvm.mlir.constant(1 : i32) : i32
    %1 = llvm.mlir.constant(0.000000e+00 : f32) : f32
    %2 = llvm.alloca %0 x f32 {alignment = 4 : i64} : (i32) -> !llvm.ptr
    %3 = llvm.alloca %0 x f32 {alignment = 4 : i64} : (i32) -> !llvm.ptr
    llvm.store %arg0, %2 {alignment = 4 : i64} : f32, !llvm.ptr
    %4 = llvm.load %2 {alignment = 4 : i64} : !llvm.ptr -> f32
    %5 = llvm.fadd %4, %1 : f32
    llvm.store %5, %3 {alignment = 4 : i64} : f32, !llvm.ptr
    %6 = llvm.load %3 {alignment = 4 : i64} : !llvm.ptr -> f32
    llvm.return %6 : f32
  }
  llvm.func @add_nonzero(%arg0: f32 {llvm.noundef}) -> f32 attributes {frame_pointer = #llvm.framePointerKind<"non-leaf">, no_inline, no_unwind, optimize_none, passthrough = ["ssp", ["uwtable", "1"], ["no-trapping-math", "true"], ["stack-protector-buffer-size", "8"], ["target-cpu", "apple-m1"]], target_cpu = "apple-m1", target_features = #llvm.target_features<["+aes", "+altnzcv", "+ccdp", "+ccidx", "+ccpp", "+complxnum", "+crc", "+dit", "+dotprod", "+flagm", "+fp-armv8", "+fp16fml", "+fptoint", "+fullfp16", "+jsconv", "+lse", "+neon", "+pauth", "+perfmon", "+predres", "+ras", "+rcpc", "+rdm", "+sb", "+sha2", "+sha3", "+specrestrict", "+ssbs", "+v8.1a", "+v8.2a", "+v8.3a", "+v8.4a", "+v8a", "+zcm", "+zcz"]>} {
    %0 = llvm.mlir.constant(1 : i32) : i32
    %1 = llvm.mlir.constant(1.000000e+00 : f32) : f32
    %2 = llvm.alloca %0 x f32 {alignment = 4 : i64} : (i32) -> !llvm.ptr
    %3 = llvm.alloca %0 x f32 {alignment = 4 : i64} : (i32) -> !llvm.ptr
    llvm.store %arg0, %2 {alignment = 4 : i64} : f32, !llvm.ptr
    %4 = llvm.load %2 {alignment = 4 : i64} : !llvm.ptr -> f32
    %5 = llvm.fadd %4, %1 : f32
    llvm.store %5, %3 {alignment = 4 : i64} : f32, !llvm.ptr
    %6 = llvm.load %3 {alignment = 4 : i64} : !llvm.ptr -> f32
    llvm.return %6 : f32
  }
}
