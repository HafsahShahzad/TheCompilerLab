// === Required for Metal-C++ Implementation (define in exactly one file) ===
#define NS_PRIVATE_IMPLEMENTATION
#define CA_PRIVATE_IMPLEMENTATION
#define MTL_PRIVATE_IMPLEMENTATION

#include <Foundation/Foundation.hpp>
#include <QuartzCore/QuartzCore.hpp>
#include <Metal/Metal.hpp>

#include <iostream>
#include <vector>
#include <chrono>   // for CPU timing

using namespace MTL;

int main() {
    // ------------------------------------------------------------------------
    // 1. Setup Metal device and command queue
    // ------------------------------------------------------------------------
    NS::AutoreleasePool* pool = NS::AutoreleasePool::alloc()->init();

    MTL::Device* device = MTL::CreateSystemDefaultDevice();
    if (!device) {
        std::cerr << "No Metal device found.\n";
        return 1;
    }
    std::cout << "Using device: " << device->name()->utf8String() << std::endl;

    MTL::CommandQueue* queue = device->newCommandQueue();

    // ------------------------------------------------------------------------
    // 2. Load metallib (precompiled)
    // ------------------------------------------------------------------------
    NS::String* libPath = NS::String::string("vector_add.metallib", NS::UTF8StringEncoding);
    NS::URL* libURL = NS::URL::fileURLWithPath(libPath);
    NS::Error* error = nullptr;

    MTL::Library* library = device->newLibrary(libURL, &error);
    if (!library) {
        std::cerr << "Failed to load metallib: "
                  << (error ? error->localizedDescription()->utf8String() : "unknown")
                  << std::endl;
        return 1;
    }

    // ------------------------------------------------------------------------
    // 3. Create compute pipeline
    // ------------------------------------------------------------------------
    NS::String* kernelName = NS::String::string("vector_add", NS::UTF8StringEncoding);
    MTL::Function* function = library->newFunction(kernelName);
    MTL::ComputePipelineState* pipeline = device->newComputePipelineState(function, &error);

    if (!pipeline) {
        std::cerr << "Failed to create pipeline: "
                  << (error ? error->localizedDescription()->utf8String() : "unknown")
                  << std::endl;
        return 1;
    }

    // ------------------------------------------------------------------------
    // 4. Prepare input/output buffers
    // ------------------------------------------------------------------------
    const size_t N = 1024;
    const size_t bufBytes = N * sizeof(float);

    std::vector<float> A(N), B(N);
    for (size_t i = 0; i < N; i++) {
        A[i] = float(i);
        B[i] = float(N - i);
    }

    MTL::Buffer* bufA = device->newBuffer(A.data(), bufBytes, MTL::ResourceStorageModeShared);
    MTL::Buffer* bufB = device->newBuffer(B.data(), bufBytes, MTL::ResourceStorageModeShared);
    MTL::Buffer* bufC = device->newBuffer(bufBytes, MTL::ResourceStorageModeShared);

    // ------------------------------------------------------------------------
    // 5. Encode and submit commands with GPU + CPU timing
    // ------------------------------------------------------------------------
    auto cpuStart = std::chrono::high_resolution_clock::now();

    MTL::CommandBuffer* cb = queue->commandBuffer();

    // GPU timing handler
    cb->addCompletedHandler(^void(MTL::CommandBuffer* buffer) {
        double gpuStart = buffer->GPUStartTime();
        double gpuEnd = buffer->GPUEndTime();
        double gpuTimeMs = (gpuEnd - gpuStart) * 1000.0;
        std::cout << "GPU execution time: " << gpuTimeMs << " ms" << std::endl;
    });

    MTL::ComputeCommandEncoder* enc = cb->computeCommandEncoder();
    enc->setComputePipelineState(pipeline);
    enc->setBuffer(bufA, 0, 0);
    enc->setBuffer(bufB, 0, 1);
    enc->setBuffer(bufC, 0, 2);

    NS::UInteger threadWidth = pipeline->threadExecutionWidth();
    MTL::Size gridSize(N, 1, 1);
    MTL::Size tgSize(threadWidth, 1, 1);

    enc->dispatchThreads(gridSize, tgSize);
    enc->endEncoding();

    cb->commit();
    cb->waitUntilCompleted();

    auto cpuEnd = std::chrono::high_resolution_clock::now();
    double cpuMs = std::chrono::duration<double, std::milli>(cpuEnd - cpuStart).count();
    std::cout << "CPU wall time: " << cpuMs << " ms" << std::endl;

    // ------------------------------------------------------------------------
    // 6. Verify results
    // ------------------------------------------------------------------------
    float* C = reinterpret_cast<float*>(bufC->contents());
    for (size_t i = 0; i < 5; i++) {
        std::cout << A[i] << " + " << B[i] << " = " << C[i] << std::endl;
    }

    pool->release();
    return 0;
}

