---
name: quantization
description: "Skill for the Quantization area of Quark. 111 symbols across 34 files."
---

# Quantization

111 symbols | 34 files | Cohesion: 61%

## When to Use

- Working with code in `quark/`
- Understanding how compute_minmse, get_qmin_qmax_for_qType, quantize_nparray work
- Modifying quantization-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `quark/torch/quantization/tensor_quantize.py` | fake_quantize, contains_at_least_two_tensor_quantizers, forward, _process_tensor_quantizer, _apply_forward_quantization (+14) |
| `quark/onnx/quantization/quant_utils.py` | compute_minmse, _check_type, get_qmin_qmax_for_qType, quantize_nparray, pos2scale (+12) |
| `quark/torch/quantization/file2file_quantization.py` | _export_quant_config, _export_config, _empty_cache_if_cuda, _is_linear_weight_tensor, _get_layer_quant_config_by_tensor_name (+7) |
| `quark/torch/quantization/cache_integration.py` | extract_quantizers_from_model, extract_layer_index, patched_forward, disable_kv_proj_output_quantization, __init__ (+4) |
| `quark/onnx/utils/model_utils.py` | run_onnx_model, update_user_custom_op_lib_paths, onnx_save_model_with_encryption, onnx_load_model_with_decryption, cache_onnx_model_and_infer_shapes (+1) |
| `quark/torch/quantization/debug.py` | check_scale_stats, barplot, summarize_weight, summarize_activation, collect_quantization_statistics |
| `quark/torch/quantization/api.py` | quantize_model, _apply_advanced_quant_algo, load_params, direct_quantize_checkpoint, freeze |
| `quark/torch/quantization/model_transformation.py` | process_model_transformation, setup_config_per_layer, prepare_for_attention_quant, in_place_replace_layer, import_model_with_cache_from_safetensors |
| `quark/onnx/quantization/output_eval.py` | calculate_cos, calculate_l2_distance, eval_metrics |
| `quark/onnx/quantization/quantize.py` | quantize_static, quantize_dynamic |

## Entry Points

Start here when exploring this area:

- **`compute_minmse`** (Function) — `quark/onnx/quantization/quant_utils.py:129`
- **`get_qmin_qmax_for_qType`** (Function) — `quark/onnx/quantization/quant_utils.py:450`
- **`quantize_nparray`** (Function) — `quark/onnx/quantization/quant_utils.py:499`
- **`pos2scale`** (Function) — `quark/onnx/quantization/quant_utils.py:825`
- **`compute_scale_zp`** (Function) — `quark/onnx/quantization/quant_utils.py:835`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `FakeQuantizeBase` | Class | `quark/torch/quantization/tensor_quantize.py` | 60 |
| `ScaledFakeQuantize` | Class | `quark/torch/quantization/tensor_quantize.py` | 171 |
| `compute_minmse` | Function | `quark/onnx/quantization/quant_utils.py` | 129 |
| `get_qmin_qmax_for_qType` | Function | `quark/onnx/quantization/quant_utils.py` | 450 |
| `quantize_nparray` | Function | `quark/onnx/quantization/quant_utils.py` | 499 |
| `pos2scale` | Function | `quark/onnx/quantization/quant_utils.py` | 825 |
| `compute_scale_zp` | Function | `quark/onnx/quantization/quant_utils.py` | 835 |
| `compute_scale_zp_fp` | Function | `quark/onnx/quantization/quant_utils.py` | 939 |
| `dequantize_data` | Function | `quark/onnx/quantization/quant_utils.py` | 1001 |
| `quantize_data` | Function | `quark/onnx/quantization/quant_utils.py` | 1013 |
| `get_exclude_nodes` | Function | `quark/onnx/quantization/quant_utils.py` | 1124 |
| `get_pre_defined_preprocess_config` | Function | `quark/onnx/quantization/quant_utils.py` | 2128 |
| `quantize_static` | Function | `quark/onnx/quantization/quantize.py` | 90 |
| `save_quantized_info` | Function | `quark/onnx/utils/file_utils.py` | 16 |
| `run_onnx_model` | Function | `quark/onnx/utils/model_utils.py` | 494 |
| `update_user_custom_op_lib_paths` | Function | `quark/onnx/utils/model_utils.py` | 681 |
| `print_fp32_nodes` | Function | `quark/onnx/utils/print_utils.py` | 254 |
| `print_quantized_info` | Function | `quark/onnx/utils/print_utils.py` | 293 |
| `check_scale_stats` | Function | `quark/torch/quantization/debug.py` | 537 |
| `test_reload_config` | Function | `test/test_for_torch/test_config.py` | 13 |

## Execution Flows

| Flow | Type | Steps |
|------|------|-------|
| `Quantize_model → Get_qmin_qmax_for_qType` | cross_community | 8 |
| `Quantize_model → Dequantize_data` | cross_community | 8 |
| `Quantize_model → Get_qmin_qmax_for_qType` | cross_community | 8 |
| `Quantize_model → Dequantize_data` | cross_community | 8 |
| `Quantize_model → Warning` | cross_community | 7 |
| `Quantize_model → _check_type` | cross_community | 7 |
| `Quantize_model → Warning` | cross_community | 7 |
| `Quantize_model → _check_type` | cross_community | 7 |
| `Apply_post_quant_algorithms → Save_onnx_model_with_external_data` | cross_community | 6 |
| `Adjust_shift_bias → Is_approximately_equal` | cross_community | 6 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Optimizations | 49 calls |
| Passes | 38 calls |
| Refinement | 23 calls |
| Calibration | 8 calls |
| Config | 5 calls |
| Observer | 4 calls |
| Test_for_onnx | 4 calls |
| Gguf_export | 3 calls |

## How to Explore

1. `gitnexus_context({name: "compute_minmse"})` — see callers and callees
2. `gitnexus_query({query: "quantization"})` — find related execution flows
3. Read key files listed above for implementation details
