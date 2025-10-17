#include <metal_stdlib>
using namespace metal;

kernel void vector_add(
    const device float* inA [[buffer(0)]],
    const device float* inB [[buffer(1)]],
    device float* out [[buffer(2)]],
    uint id [[thread_position_in_grid]]
) {
    out[id] = inA[id] + inB[id];
}
