---
name: npu
description: "Skill for the Npu area of Quark. 138 symbols across 16 files."
---

# Npu

138 symbols | 16 files | Cohesion: 58%

## When to Use

- Working with code in `quark/`
- Understanding how ctx, ctx, ctx work
- Modifying npu-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/npu/gqo.cpp` | executeMatMulNBitsAie, ctx, executeMatMulNBits, set_params_bmm, initializeKernels (+46) |
| `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/npu/npu_op.cpp` | freeAfterPrefill, lastNode, useExternalData, runCommandSilently, manageDynamicDpmState (+11) |
| `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/npu/ssmlp_base.cpp` | ctx, initializeProjection, loadOneLoraData, get_fused_size, UpdateSharedBuffer (+8) |
| `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/npu/matmulnbits.cpp` | ctx, loadLoraData, UpdateSharedBuffer, readDataImpl, LoadLora (+6) |
| `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/npu/qmoe.cpp` | map_experts, bind_experts, initializeKernels, AMDQMoEKernel, UpdateSharedBuffer (+3) |
| `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/npu/jit_node_impl.hpp` | loadData, readData, unloadData, weightsReady, isJitEnabled (+2) |
| `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/npu/conv_split_mul.cpp` | info2, initBufBos, transpose021WithCast, Conv1DSim, ConvCpu (+2) |
| `quark/contrib/onnx_utils/src/onnx_custom_ops/lora.hpp` | prefillHeader, loadBinData, getMaxRank, getLoraName, isEnabled |
| `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/npu/ssmlpfuse.cpp` | ctx, UpdateSharedBuffer, readDataImpl, execute_ssmlp |
| `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/npu/npu_utils.hpp` | alignTo4096, get_NPU_tensor_size, init_rmsnorm_wts, getRmsNormConstData |

## Entry Points

Start here when exploring this area:

- **`ctx`** (Function) — `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/npu/gqo.cpp:4102`
- **`ctx`** (Function) — `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/npu/matmulnbits.cpp:642`
- **`ctx`** (Function) — `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/npu/ssmlp_base.cpp:1301`
- **`ctx`** (Function) — `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/npu/ssmlpfuse.cpp:310`
- **`getExternalTensorInfo`** (Function) — `quark/contrib/onnx_utils/src/onnx_custom_ops/external_data.cpp:19`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `ctx` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/npu/gqo.cpp` | 4102 |
| `ctx` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/npu/matmulnbits.cpp` | 642 |
| `ctx` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/npu/ssmlp_base.cpp` | 1301 |
| `ctx` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/npu/ssmlpfuse.cpp` | 310 |
| `getExternalTensorInfo` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/external_data.cpp` | 19 |
| `alignTo4096` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/npu/npu_utils.hpp` | 19 |
| `get_NPU_tensor_size` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/npu/npu_utils.hpp` | 24 |
| `loadBin` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/external_data.cpp` | 35 |
| `updateJitBuffer` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/npu/npu_op.cpp` | 147 |
| `ctx` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/npu/qmoe.cpp` | 940 |
| `endsWith` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/string.cpp` | 67 |
| `info2` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/npu/conv_split_mul.cpp` | 49 |
| `init_rmsnorm_wts` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/npu/npu_utils.hpp` | 64 |
| `execute_mha` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/npu/gqo.cpp` | 1306 |
| `execute_bmm2_npu` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/npu/gqo.cpp` | 1460 |
| `execute_bmm2` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/npu/gqo.cpp` | 1529 |
| `conditionalTry` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/npu/npu_op.hpp` | 43 |
| `ctx` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/npu/conv_split_mul.cpp` | 408 |
| `softmax_mask_info` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/npu/gqo.cpp` | 2955 |
| `softmax_state` | Function | `quark/contrib/onnx_utils/src/onnx_custom_ops/hybrid_llm/npu/gqo.cpp` | 2957 |

## Execution Flows

| Flow | Type | Steps |
|------|------|-------|
| `Ctx → IsEnabled` | cross_community | 4 |
| `Ctx → Preemption` | cross_community | 4 |
| `Ctx → MaxSeqLength` | cross_community | 4 |
| `Ctx → IsEnabled` | cross_community | 4 |
| `Ctx → Preemption` | cross_community | 4 |
| `Ctx → IsEnabled` | cross_community | 4 |
| `Ctx → Preemption` | cross_community | 4 |
| `AMDQMoEKernel → Raw` | cross_community | 4 |
| `Ctx → Raw` | cross_community | 4 |
| `Ctx → IsEnabled` | cross_community | 4 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Onnx_custom_ops | 9 calls |
| Operators | 5 calls |
| Dynamic_dispatch | 4 calls |

## How to Explore

1. `gitnexus_context({name: "ctx"})` — see callers and callees
2. `gitnexus_query({query: "npu"})` — find related execution flows
3. Read key files listed above for implementation details
