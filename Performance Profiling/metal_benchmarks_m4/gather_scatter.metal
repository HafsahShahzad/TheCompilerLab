
#include <metal_stdlib>
using namespace metal;

kernel void strided_gather(device float* dst [[buffer(0)]],
                           device const float* src [[buffer(1)]],
                           device const uint* idx [[buffer(2)]],
                           uint gid [[thread_position_in_grid]]) {
    uint index = idx[gid];
    dst[gid] = src[index];
}
