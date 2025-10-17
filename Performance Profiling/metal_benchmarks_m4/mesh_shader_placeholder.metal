
#include <metal_stdlib>
using namespace metal;

struct Triangle { float2 a, b, c; float3 color; };

inline float edge(float2 p, float2 a, float2 b) {
    float2 ab = b - a;
    float2 ap = p - a;
    return ab.x * ap.y - ab.y * ap.x;
}

kernel void mesh_visual_compute(texture2d<float, access::write> outTex [[texture(0)]],
                                constant Triangle& tri [[buffer(0)]],
                                constant uint2& size [[buffer(1)]],
                                uint2 tid [[thread_position_in_grid]]) {
    if (tid.x >= size.x || tid.y >= size.y) return;
    float2 p = (float2(tid) + 0.5) / float2(size) * 2.0 - 1.0;
    float w0 = edge(p, tri.b, tri.c);
    float w1 = edge(p, tri.c, tri.a);
    float w2 = edge(p, tri.a, tri.b);
    bool inside = (w0 >= 0.0 && w1 >= 0.0 && w2 >= 0.0) || (w0 <= 0.0 && w1 <= 0.0 && w2 <= 0.0);
    float3 col = inside ? tri.color : float3(0.02, 0.02, 0.02);
    outTex.write(float4(col, 1.0), tid);
}
