cmake_minimum_required(VERSION 3.20)
project(MLIRPasses LANGUAGES C CXX)

# Homebrew LLVM/MLIR paths
set(LLVM_DIR "/opt/homebrew/opt/llvm/lib/cmake/llvm")
set(MLIR_DIR "/opt/homebrew/opt/llvm/lib/cmake/mlir")

# Find MLIR
find_package(MLIR REQUIRED CONFIG)

# Include MLIR headers and definitions
add_definitions(${MLIR_DEFINITIONS})
include_directories(${MLIR_INCLUDE_DIRS})

# Source files for your executable
set(SOURCES
    tools/mlir-opt-custom.cpp
    lib/SimplifyAdd.cpp
)

# Create executable
add_executable(mlir-opt-custom ${SOURCES})

# Link against MLIR libraries (modern replacements)
# Check location: ls /opt/homebrew/Cellar/llvm/20.1.8/lib | grep MLIR
# code is actually inside libMLIRConvertToLLVMInterface.a and libMLIRConvertToLLVMPass.a
target_link_libraries(mlir-opt-custom
    PRIVATE
    MLIRIR
    MLIRPass
    MLIRSupport
    MLIRTransforms
    MLIRParser
    MLIRRewrite
    MLIRAnalysis
    MLIRFuncDialect      # needed for func::FuncOp
    MLIRArithDialect     # needed for arith::AddFOp\
    MLIRMathDialect
    MLIROptLib
    MLIRLLVMDialect
    MLIRFuncToLLVM
    MLIRMemRefToLLVM
    MLIRArithToLLVM
    MLIRIndexToLLVM
    MLIRComplexToLLVM
    MLIRMathToLLVM
    MLIRVectorToLLVM
    MLIRUBToLLVM
    MLIRControlFlowToLLVM
    MLIRLLVMCommonConversion
    MLIRConvertToLLVMPass
    MLIRConvertToLLVMInterface
)

# Set C++ standard
set_target_properties(mlir-opt-custom PROPERTIES
    CXX_STANDARD 17
    CXX_STANDARD_REQUIRED YES
    CXX_EXTENSIONS NO
)
