---
name: create-torch
description: "Skill for the Create_torch area of Quark. 68 symbols across 15 files."
---

# Create_torch

68 symbols | 15 files | Cohesion: 79%

## When to Use

- Working with code in `quark/`
- Understanding how extract_padding_params_for_conv, extract_weight_and_bias, load_weight_and_bias work
- Modifying create_torch-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `quark/onnx/algorithm/finetuning/create_torch/base_qdq_quantizers.py` | fp_quant_func, fp_dequant_func, fp_quant_dequant_func, quantize_dequantize, round_impl (+8) |
| `quark/onnx/algorithm/finetuning/create_torch/create_model_ops.py` | extract_padding_params_for_conv, extract_weight_and_bias, load_weight_and_bias, convert_conv, _extract_attributes (+6) |
| `quark/onnx/algorithm/finetuning/create_torch/create_model_utils.py` | extract_attr_values, _find_node_input_qdq, _find_node_input_fn, _parse_fn_quant_info, get_inputs_qinfo (+5) |
| `quark/onnx/algorithm/finetuning/create_torch/quant_base_ops.py` | QuantizeWrapper, create_qdq_quantizer, create_fn_quantizer, __init__, create_input_quantizer (+2) |
| `quark/onnx/algorithm/finetuning/create_torch/quant_conv_ops.py` | QConv1d, QConv2d, QConv3d, QConvTranspose1d, QConvTranspose2d (+1) |
| `quark/onnx/algorithm/finetuning/create_torch/base_fn_quantizers.py` | bfp, forward, bfp_prime, forward, mx (+1) |
| `quark/onnx/algorithm/finetuning/create_torch/quant_norm_ops.py` | QInstanceNorm1d, QInstanceNorm2d, QInstanceNorm3d, QLayerNorm |
| `test/test_for_onnx/test_quantize_fastfinetune.py` | test_quantize_fpfunc, test_quantize_basic |
| `test/test_for_onnx/test_quantize_fastfinetune_refactor.py` | test_quantize_fpfunc, test_quantize_basic |
| `quark/onnx/algorithm/finetuning/create_torch/create_model.py` | set_weight, set_bias |

## Entry Points

Start here when exploring this area:

- **`extract_padding_params_for_conv`** (Function) — `quark/onnx/algorithm/finetuning/create_torch/create_model_ops.py:71`
- **`extract_weight_and_bias`** (Function) — `quark/onnx/algorithm/finetuning/create_torch/create_model_ops.py:85`
- **`load_weight_and_bias`** (Function) — `quark/onnx/algorithm/finetuning/create_torch/create_model_ops.py:99`
- **`convert_conv`** (Function) — `quark/onnx/algorithm/finetuning/create_torch/create_model_ops.py:108`
- **`convert_matmul`** (Function) — `quark/onnx/algorithm/finetuning/create_torch/create_model_ops.py:217`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `QuantizeWrapper` | Class | `quark/onnx/algorithm/finetuning/create_torch/quant_base_ops.py` | 95 |
| `QConv1d` | Class | `quark/onnx/algorithm/finetuning/create_torch/quant_conv_ops.py` | 13 |
| `QConv2d` | Class | `quark/onnx/algorithm/finetuning/create_torch/quant_conv_ops.py` | 30 |
| `QConv3d` | Class | `quark/onnx/algorithm/finetuning/create_torch/quant_conv_ops.py` | 47 |
| `QConvTranspose1d` | Class | `quark/onnx/algorithm/finetuning/create_torch/quant_conv_ops.py` | 64 |
| `QConvTranspose2d` | Class | `quark/onnx/algorithm/finetuning/create_torch/quant_conv_ops.py` | 83 |
| `QConvTranspose3d` | Class | `quark/onnx/algorithm/finetuning/create_torch/quant_conv_ops.py` | 102 |
| `QGemm` | Class | `quark/onnx/algorithm/finetuning/create_torch/quant_gemm_ops.py` | 13 |
| `QMatMul` | Class | `quark/onnx/algorithm/finetuning/create_torch/quant_matmul_ops.py` | 13 |
| `QInstanceNorm1d` | Class | `quark/onnx/algorithm/finetuning/create_torch/quant_norm_ops.py` | 13 |
| `QInstanceNorm2d` | Class | `quark/onnx/algorithm/finetuning/create_torch/quant_norm_ops.py` | 31 |
| `QInstanceNorm3d` | Class | `quark/onnx/algorithm/finetuning/create_torch/quant_norm_ops.py` | 49 |
| `QLayerNorm` | Class | `quark/onnx/algorithm/finetuning/create_torch/quant_norm_ops.py` | 67 |
| `extract_padding_params_for_conv` | Function | `quark/onnx/algorithm/finetuning/create_torch/create_model_ops.py` | 71 |
| `extract_weight_and_bias` | Function | `quark/onnx/algorithm/finetuning/create_torch/create_model_ops.py` | 85 |
| `load_weight_and_bias` | Function | `quark/onnx/algorithm/finetuning/create_torch/create_model_ops.py` | 99 |
| `convert_conv` | Function | `quark/onnx/algorithm/finetuning/create_torch/create_model_ops.py` | 108 |
| `convert_matmul` | Function | `quark/onnx/algorithm/finetuning/create_torch/create_model_ops.py` | 217 |
| `convert_gemm` | Function | `quark/onnx/algorithm/finetuning/create_torch/create_model_ops.py` | 262 |
| `convert_norm` | Function | `quark/onnx/algorithm/finetuning/create_torch/create_model_ops.py` | 329 |

## Execution Flows

| Flow | Type | Steps |
|------|------|-------|
| `Run → Initialize_alpha` | cross_community | 3 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Refinement | 10 calls |
| Passes | 6 calls |

## How to Explore

1. `gitnexus_context({name: "extract_padding_params_for_conv"})` — see callers and callees
2. `gitnexus_query({query: "create_torch"})` — find related execution flows
3. Read key files listed above for implementation details
