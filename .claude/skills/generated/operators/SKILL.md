---
name: operators
description: "Skill for the Operators area of Quark. 81 symbols across 36 files."
---

# Operators

81 symbols | 36 files | Cohesion: 93%

## When to Use

- Working with code in `quark/`
- Understanding how ctx, ctx, ctx work
- Modifying operators-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/operators/hybrid_kernel.cpp` | withCustomAllocator, dmlInstance, gpuTensors, createGpu, initializeGpu (+4) |
| `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/gpu/operator.cpp` | StringToDataType, StringToActivationFunc, ComputeStrides, MarkRepackIfOddDim, CreateTensorDesc (+2) |
| `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/gpu/operators/ssmlp_gelu.cpp` | DequantizeBForMatmul, CreateDmlCastTensorDesc, SSMLPGeluOperator, SharedInit, CreateTensorDescSSLRN (+2) |
| `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/gpu/operators/ssmlp.cpp` | DequantizeBForMatmul, SSMLPOperator, SharedInit, CreateTensorDescSSLRN, CreateTensorDescMatMul |
| `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/operators/opUtils.h` | ElementFormat, GetPackedTensorSize, printLog, HandleNegativeAxis |
| `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/gpu/operators/gqa.cpp` | CreateDmlCastTensorDesc, CreateGQAOperator, GQAOperator, SharedInit |
| `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/gpu/operators/matMulNBits.cpp` | CreateMatmulNBitOperator, MatMulNBitsOperator, SharedInit |
| `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/operators/gather.cpp` | GatherKernel, ctx |
| `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/operators/gqo.cpp` | GQOKernel, ctx |
| `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/operators/matmul.cpp` | MatMulKernel, ctx |

## Entry Points

Start here when exploring this area:

- **`ctx`** (Function) — `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/operators/gather.cpp:113`
- **`ctx`** (Function) — `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/operators/gqo.cpp:164`
- **`ctx`** (Function) — `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/operators/matmul.cpp:61`
- **`ctx`** (Function) — `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/operators/matmulnbits.cpp:155`
- **`ElementFormat`** (Function) — `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/operators/opUtils.h:17`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `ctx` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/operators/gather.cpp` | 113 |
| `ctx` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/operators/gqo.cpp` | 164 |
| `ctx` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/operators/matmul.cpp` | 61 |
| `ctx` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/operators/matmulnbits.cpp` | 155 |
| `ElementFormat` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/operators/opUtils.h` | 17 |
| `GetPackedTensorSize` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/operators/opUtils.h` | 76 |
| `printLog` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/operators/opUtils.h` | 140 |
| `ctx` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/operators/qmoe.cpp` | 52 |
| `ctx` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/operators/reducesum.cpp` | 114 |
| `ctx` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/operators/rope.cpp` | 76 |
| `ctx` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/operators/slrn.cpp` | 176 |
| `ctx` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/operators/ssgmlp.cpp` | 121 |
| `ctx` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/operators/sslrn.cpp` | 110 |
| `ctx` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/operators/ssmlp.cpp` | 127 |
| `ctx` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/operators/sub.cpp` | 100 |
| `getAttribute` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/ort.hpp` | 12 |
| `UseRMMBuffer` | Method | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/gpu/gpu_utils.h` | 32 |
| `InitializeJitTensorInfo` | Method | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/gpu/jit_wts_loader.cpp` | 113 |
| `GatherKernel` | Method | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/operators/gather.cpp` | 29 |
| `GQOKernel` | Method | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/operators/gqo.cpp` | 31 |

## Execution Flows

| Flow | Type | Steps |
|------|------|-------|
| `SSMLPGeluOperator → CreateTensorDesc` | cross_community | 4 |
| `SSMLPOperator → CreateTensorDesc` | cross_community | 4 |
| `AMDQMoEKernel → GetAttribute` | cross_community | 3 |
| `SSMLPGeluOperator → Max` | cross_community | 3 |
| `SSMLPOperator → Max` | cross_community | 3 |
| `MatMulNBitsKernel → UseRMMAllocatedMemory` | intra_community | 3 |
| `MatMulNBitsKernel → UseRMMBuffer` | intra_community | 3 |
| `MatMulNBitsKernel → ElementFormat` | intra_community | 3 |
| `MatMulNBitsKernel → GetPackedTensorSize` | intra_community | 3 |
| `SimplifiedLayerNormKernel → UseRMMAllocatedMemory` | intra_community | 3 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Gpu | 1 calls |

## How to Explore

1. `gitnexus_context({name: "ctx"})` — see callers and callees
2. `gitnexus_query({query: "operators"})` — find related execution flows
3. Read key files listed above for implementation details
