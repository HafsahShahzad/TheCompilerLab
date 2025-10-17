
#include <metal_stdlib>
using namespace metal;

kernel void divergent_add(device float* dst [[buffer(0)]],
                          device const float* src [[buffer(1)]],
                          uint gid [[thread_position_in_grid]]) {
    float v = src[gid];
    if ((gid & 1) == 0) {
        for (int i=0; i<64; ++i) { v = sin(v) + cos(v); }
    } else {
        for (int i=0; i<64; ++i) { v = v * 1.0001f + 0.0001f;; }
    }
    dst[gid] = v;
}
