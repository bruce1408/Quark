---
name: test-for-onnx
description: "Skill for the Test_for_onnx area of Quark. 374 symbols across 76 files."
---

# Test_for_onnx

374 symbols | 76 files | Cohesion: 83%

## When to Use

- Working with code in `test/`
- Understanding how prepare_model, prepare_config, prepare_fastft_config work
- Modifying test_for_onnx-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `test/test_for_onnx/test_quantize_auto_search.py` | prepare_model, prepare_config, prepare_fastft_config, prepare_data, tensor_quantize (+13) |
| `test/test_for_onnx/test_quantize_rotation.py` | test_quantize_correct, test_quantize_whole, test_quantize_abnormal, prepare_model, prepare_config (+8) |
| `test/test_for_onnx/test_quantize_rotation_refactor.py` | test_quantize_correct, test_quantize_whole, test_quantize_abnormal, prepare_model, prepare_config (+8) |
| `test/test_for_onnx/test_optimize_all.py` | contains_op_type, tensor_quantize, test_optimize_convert_bn_to_conv, test_optimize_convert_clip_to_relu, test_optimize_convert_reduce_mean_to_global_avg_pool (+8) |
| `test/test_for_onnx/test_optimize_all_refactor.py` | contains_op_type, tensor_quantize, test_optimize_convert_bn_to_conv, test_optimize_convert_clip_to_relu, test_optimize_convert_reduce_mean_to_global_avg_pool (+8) |
| `test/test_for_onnx/test_quantize_mix_precision_MX.py` | tensor_quantize, test_quantize_elementwise_mix_precision, test_quantize_layerwise_mix_precision, test_quantize_tensorwise_mix_precision, test_quantize_MXandBFP_standard_mix_precision (+7) |
| `test/test_for_onnx/test_quantize_calibrator_refactor.py` | tensor_quantize, test_tensor_quantize_minmse_all_multiple_workers, test_tensor_quantize_minmse_all, test_tensor_quantize_minmse_mostcommon, test_tensor_quantize_minmse_percentile (+7) |
| `test/test_for_onnx/test_quantize_fp16.py` | prepare_quantizer, infer_quantized_model, tensor_quantize, test_quantize_fp16_cast, test_quantize_fp16_constant_of_shape_node (+6) |
| `test/test_for_onnx/test_quantize_fp16_refactor.py` | prepare_quantizer, infer_quantized_model, tensor_quantize, test_quantize_fp16_cast, test_quantize_fp16_constant_of_shape_node (+6) |
| `test/test_for_onnx/test_quantize_matmul_nbits.py` | test_quantize_hqq, prepare_config, prepare_data, prepare_quantizer, quantize_static (+5) |

## Entry Points

Start here when exploring this area:

- **`prepare_model`** (Function) — `test/test_for_onnx/test_quantize_auto_search.py:124`
- **`prepare_config`** (Function) — `test/test_for_onnx/test_quantize_auto_search.py:146`
- **`prepare_fastft_config`** (Function) — `test/test_for_onnx/test_quantize_auto_search.py:156`
- **`prepare_data`** (Function) — `test/test_for_onnx/test_quantize_auto_search.py:167`
- **`tensor_quantize`** (Function) — `test/test_for_onnx/test_quantize_auto_search.py:193`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `prepare_model` | Function | `test/test_for_onnx/test_quantize_auto_search.py` | 124 |
| `prepare_config` | Function | `test/test_for_onnx/test_quantize_auto_search.py` | 146 |
| `prepare_fastft_config` | Function | `test/test_for_onnx/test_quantize_auto_search.py` | 156 |
| `prepare_data` | Function | `test/test_for_onnx/test_quantize_auto_search.py` | 167 |
| `tensor_quantize` | Function | `test/test_for_onnx/test_quantize_auto_search.py` | 193 |
| `check_fast_fintune_arguments` | Function | `quark/onnx/quantization/input_check.py` | 110 |
| `is_version_below` | Function | `quark/onnx/quantization/quant_utils.py` | 47 |
| `create_range_dict` | Function | `quark/onnx/quantization/quant_utils.py` | 345 |
| `tensor_quantize` | Function | `test/test_for_onnx/test_quantize_adjust_bias_scale.py` | 141 |
| `tensor_quantize` | Function | `test/test_for_onnx/test_quantize_adjust_bias_scale_refactor.py` | 144 |
| `contains_op_type` | Function | `test/test_for_onnx/test_optimize_all.py` | 565 |
| `tensor_quantize` | Function | `test/test_for_onnx/test_optimize_all.py` | 570 |
| `contains_op_type` | Function | `test/test_for_onnx/test_optimize_all_refactor.py` | 566 |
| `tensor_quantize` | Function | `test/test_for_onnx/test_optimize_all_refactor.py` | 571 |
| `prepare_config` | Function | `test/test_for_onnx/test_quantize_BFP_finetune.py` | 73 |
| `tensor_quantize` | Function | `test/test_for_onnx/test_quantize_BFP_finetune.py` | 143 |
| `prepare_config` | Function | `test/test_for_onnx/test_quantize_BFP_finetune_refactor.py` | 71 |
| `tensor_quantize` | Function | `test/test_for_onnx/test_quantize_BFP_finetune_refactor.py` | 134 |
| `tensor_quantize` | Function | `test/test_for_onnx/test_quantize_all_config.py` | 851 |
| `tensor_quantize` | Function | `test/test_for_onnx/test_quantize_bias_correction.py` | 108 |

## Execution Flows

| Flow | Type | Steps |
|------|------|-------|
| `Quantize_model → Is_version_below` | cross_community | 6 |
| `Quantize_model → Is_version_below` | cross_community | 6 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Auto_search | 18 calls |
| Passes | 6 calls |
| Optimizations | 5 calls |
| Test_for_torch | 5 calls |
| Observer | 4 calls |
| Hw_emulation | 4 calls |

## How to Explore

1. `gitnexus_context({name: "prepare_model"})` — see callers and callees
2. `gitnexus_query({query: "test_for_onnx"})` — find related execution flows
3. Read key files listed above for implementation details
