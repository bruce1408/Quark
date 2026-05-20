---
name: passes
description: "Skill for the Passes area of Quark. 249 symbols across 126 files."
---

# Passes

249 symbols | 126 files | Cohesion: 68%

## When to Use

- Working with code in `quark/`
- Understanding how get_modules_optimized_weight, save_tensor_hist_fig, calibrate_model work
- Modifying passes-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/passes/hybrid_llm_jit.py` | get_layer_id, node_gen, save_weights, save_embedding, save_jit_weights (+8) |
| `quark/onnx_adapter/passes/onnx_convert_fp16_to_fp32.py` | _convert_np_to_float16, _convert_tensor_float_to_float16, _sort_graph_node, _sort_topology, _convert_tensor_float16_to_float (+2) |
| `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/transform/cast.py` | add_cast_dtype_to_bfloat16_auto, add_cast_bfloat16_to_dtype_auto, bfloat16_to_float, add_cast_to_float_and_add_silu, add_cast_to_float_and_add_bfp_silu (+2) |
| `quark/contrib/onnx_utils/tests/passes/test_transfer_pow_mul_add_tanh_to_gelu.py` | verify_graph, run_model, test_transfer_pow_mul_add_tanh_to_gelu_add_pattern, test_transfer_pow_mul_add_tanh_to_gelu_sum_pattern, verify_fastgelu_replacement (+2) |
| `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/passes/hybrid_llm_ssmlp.py` | get_before_cast_outputs, process_ssmlp, process_ssgmlp, check_biases, add_casts (+1) |
| `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/passes/gather_transposes.py` | can_swap_simple, can_swap, gather_transposes, find_index_of_input, rewrite_nodes (+1) |
| `quark/onnx/quantization/quant_utils.py` | load_model_with_shape_infer, save_and_reload_model_with_shape_infer, get_model_node_name_dict, remove_initializer_from_input, inference_sub_model_with_data |
| `quark/onnx_adapter/passes/onnx_fix_shapes.py` | _onnx_fix_shapes, _run_for_config, _create_infer_session_for_onnx_model, _generate_random_data, _infer_all_tensors_shape |
| `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/passes/gemm_block_to_gemm_noqdq_bfp.py` | get_gemm_params, is_gemm_padded_supported, is_gemm_supported, get_gemm_parameters, replacement |
| `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/passes/gemm_to_gemm_noqdq_bfp.py` | get_gemm_params, is_gemm_padded_supported, is_gemm_supported, get_gemm_parameters, replacement |

## Entry Points

Start here when exploring this area:

- **`get_modules_optimized_weight`** (Function) — `quark/onnx/algorithm/finetuning/create_torch/create_model_ops.py:566`
- **`save_tensor_hist_fig`** (Function) — `quark/onnx/calibration/calib_utils.py:63`
- **`calibrate_model`** (Function) — `quark/onnx/calibration/calibrate.py:29`
- **`create_calibrator_float_scale`** (Function) — `quark/onnx/calibration/calibrators.py:1086`
- **`get_data_reader`** (Function) — `quark/onnx/calibration/data_readers.py:543`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `get_modules_optimized_weight` | Function | `quark/onnx/algorithm/finetuning/create_torch/create_model_ops.py` | 566 |
| `save_tensor_hist_fig` | Function | `quark/onnx/calibration/calib_utils.py` | 63 |
| `calibrate_model` | Function | `quark/onnx/calibration/calibrate.py` | 29 |
| `create_calibrator_float_scale` | Function | `quark/onnx/calibration/calibrators.py` | 1086 |
| `get_data_reader` | Function | `quark/onnx/calibration/data_readers.py` | 543 |
| `run_calibration` | Function | `quark/onnx/calibration/interface.py` | 45 |
| `apply_post_optimization_before_algo` | Function | `quark/onnx/postprocess/postproc.py` | 28 |
| `apply_pre_optimization_before_algo` | Function | `quark/onnx/preprocess/preproc.py` | 34 |
| `load_model_with_shape_infer` | Function | `quark/onnx/quantization/quant_utils.py` | 537 |
| `save_and_reload_model_with_shape_infer` | Function | `quark/onnx/quantization/quant_utils.py` | 546 |
| `get_model_node_name_dict` | Function | `quark/onnx/quantization/quant_utils.py` | 1269 |
| `remove_initializer_from_input` | Function | `quark/onnx/quantization/quant_utils.py` | 1488 |
| `inference_sub_model_with_data` | Function | `quark/onnx/quantization/quant_utils.py` | 1524 |
| `create_dynamic_quantizer` | Function | `quark/onnx/quantizers/interface.py` | 486 |
| `convert_bias_int32_to_int16` | Function | `quark/onnx/tools/convert_bias_int32_to_int16.py` | 35 |
| `convert_opset_version` | Function | `quark/onnx/tools/convert_opset_version.py` | 38 |
| `parse_input_and_output_shapes` | Function | `quark/onnx/tools/fix_shapes.py` | 31 |
| `fix_input_and_output_shapes` | Function | `quark/onnx/tools/fix_shapes.py` | 52 |
| `save_all_tensors_shape` | Function | `quark/onnx/tools/fix_shapes.py` | 137 |
| `fix_shapes` | Function | `quark/onnx/tools/fix_shapes.py` | 174 |

## Execution Flows

| Flow | Type | Steps |
|------|------|-------|
| `Quantize_model → Warning` | cross_community | 7 |
| `Quantize_model → Warning` | cross_community | 7 |
| `Fast_finetune → Warning` | cross_community | 6 |
| `Replacement → Is_initializer` | cross_community | 6 |
| `Replacement → Get_external_data_for_tensor` | cross_community | 6 |
| `Bias_correction → Warning` | cross_community | 5 |
| `Replacement → Is_sequence_of` | cross_community | 5 |
| `Replacement → _get_index` | cross_community | 5 |
| `Replacement → Is_sequence_of` | cross_community | 5 |
| `Replacement → _get_index` | cross_community | 5 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Sd3 | 33 calls |
| Optimizations | 30 calls |
| Refinement | 13 calls |
| Calibration | 11 calls |
| Quantization | 7 calls |
| Tools | 4 calls |
| Finetuning | 2 calls |
| Ryzenai_onnx_utils | 2 calls |

## How to Explore

1. `gitnexus_context({name: "get_modules_optimized_weight"})` — see callers and callees
2. `gitnexus_query({query: "passes"})` — find related execution flows
3. Read key files listed above for implementation details
