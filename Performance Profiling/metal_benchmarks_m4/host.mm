
// host.mm
// Build:
// clang++ -std=c++17 host.mm -o host -I./metal-cpp \
//   -framework Metal -framework Foundation -framework QuartzCore
//
// Run: ./host
// Produces out_mesh.ppm and out_ray.ppm

#define NS_PRIVATE_IMPLEMENTATION
#define CA_PRIVATE_IMPLEMENTATION
#define MTL_PRIVATE_IMPLEMENTATION

#include <Foundation/Foundation.hpp>
#include <QuartzCore/QuartzCore.hpp>
#include <Metal/Metal.hpp>

#include <vector>
#include <string>
#include <iostream>
#include <cmath>
#include <cstdio>
#include <algorithm>

static void writePPM(const std::string& path, int w, int h, const std::vector<float>& rgba) {
    FILE* f = fopen(path.c_str(), "wb");
    if (!f) { std::cerr << "Failed to open " << path << "\n"; return; }
    fprintf(f, "P6\n%d %d\n255\n", w, h);
    for (int i=0; i<w*h; i++) {
        unsigned char r = (unsigned char)std::min(255, std::max(0, int(std::lround(rgba[4*i+0]*255.f))));
        unsigned char g = (unsigned char)std::min(255, std::max(0, int(std::lround(rgba[4*i+1]*255.f))));
        unsigned char b = (unsigned char)std::min(255, std::max(0, int(std::lround(rgba[4*i+2]*255.f))));
        fputc(r, f); fputc(g, f); fputc(b, f);
    }
    fclose(f);
}

static MTL::Library* loadLib(MTL::Device* dev, const char* name) {
    NS::Error* err = nullptr;
    MTL::Library* lib = dev->newLibrary(NS::String::string(name, NS::ASCIIStringEncoding), &err);
    if (!lib) {
        std::cerr << "Failed to load " << name << (err ? std::string(": ") + err->localizedDescription()->utf8String() : "") << "\n";
    }
    return lib;
}

int main() {
    @autoreleasepool {
        auto* pool = NS::AutoreleasePool::alloc()->init();

        MTL::Device* device = MTL::CreateSystemDefaultDevice();
        if (!device) { std::cerr << "No Metal device.\n"; return -1; }

        MTL::CommandQueue* cq = device->newCommandQueue();
        if (!cq) { std::cerr << "No command queue.\n"; return -1; }

        const uint32_t W = 800, H = 600;

        // ========== MESH VISUAL (compute) ==========
        MTL::Library* meshLib = loadLib(device, "mesh_shader_placeholder.metallib");
        if (!meshLib) return -1;

        MTL::Function* meshFn  = meshLib->newFunction(NS::String::string("mesh_visual_compute", NS::ASCIIStringEncoding));
        if (!meshFn) { std::cerr << "mesh_visual_compute not found\n"; return -1; }

        NS::Error* meshErr = nullptr;
        MTL::ComputePipelineState* meshPSO = device->newComputePipelineState(meshFn, &meshErr);
        if (!meshPSO) {
            std::cerr << "mesh PSO: " << (meshErr ? meshErr->localizedDescription()->utf8String() : "(unknown)") << "\n";
            return -1;
        }

        // Render target: PRIVATE
        MTL::TextureDescriptor* tdPriv = MTL::TextureDescriptor::texture2DDescriptor(MTL::PixelFormatRGBA32Float, W, H, false);
        tdPriv->setStorageMode(MTL::StorageModePrivate);
        tdPriv->setUsage(MTL::TextureUsageShaderWrite);
        MTL::Texture* texMeshPriv = device->newTexture(tdPriv);

        // Staging target for CPU readback: SHARED
        MTL::TextureDescriptor* tdShared = MTL::TextureDescriptor::texture2DDescriptor(MTL::PixelFormatRGBA32Float, W, H, false);
        tdShared->setStorageMode(MTL::StorageModeShared);
        tdShared->setUsage(MTL::TextureUsageUnknown);
        MTL::Texture* texMeshRead = device->newTexture(tdShared);

        struct Triangle { float a[2], b[2], c[2]; float col[3]; } tri = {
            {-0.8f,-0.6f}, {0.7f,-0.4f}, {0.1f,0.8f}, {0.9f,0.3f,0.2f}
        };
        // Constant buffers: SHARED on Apple Silicon
        MTL::Buffer* bufTri = device->newBuffer(&tri, sizeof(tri), MTL::ResourceStorageModeShared);
        uint32_t size[2] = {W,H};
        MTL::Buffer* bufSize = device->newBuffer(&size, sizeof(size), MTL::ResourceStorageModeShared);

        // Dispatch compute
        {
            MTL::CommandBuffer* cb = cq->commandBuffer();
            MTL::ComputeCommandEncoder* enc = cb->computeCommandEncoder();
            enc->setComputePipelineState(meshPSO);
            enc->setTexture(texMeshPriv, 0);
            enc->setBuffer(bufTri, 0, 0);
            enc->setBuffer(bufSize, 0, 1);

            MTL::Size tg(16, 16, 1);
            MTL::Size grid(W, H, 1);
            enc->dispatchThreads(grid, tg);
            enc->endEncoding();
            cb->commit();
            cb->waitUntilCompleted();
        }

        // Blit PRIVATE -> SHARED, then read
        {
            MTL::CommandBuffer* cb = cq->commandBuffer();
            MTL::BlitCommandEncoder* blit = cb->blitCommandEncoder();
            blit->copyFromTexture(texMeshPriv, 0, 0, MTL::Origin(0,0,0), MTL::Size(W,H,1),
                                  texMeshRead, 0, 0, MTL::Origin(0,0,0));
            blit->endEncoding();
            cb->commit();
            cb->waitUntilCompleted();
        }

        std::vector<float> pixels(W*H*4);
        MTL::Region region(0,0,W,H);
        texMeshRead->getBytes(pixels.data(), W*4*sizeof(float), region, 0);
        writePPM("out_mesh.ppm", W, H, pixels);
        std::cout << "Wrote out_mesh.ppm\n";

        pool->release();
        return 0;
    }
}

