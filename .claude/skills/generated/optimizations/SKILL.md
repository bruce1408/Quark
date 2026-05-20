---
name: optimizations
description: "Skill for the Optimizations area of Quark. 70 symbols across 26 files."
---

# Optimizations

70 symbols | 26 files | Cohesion: 45%

## When to Use

- Working with code in `quark/`
- Understanding how optimize_model, apply_post_optimization_after_algo, insert_clip_bfloat16_qdq work
- Modifying optimizations-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `quark/onnx/optimizations/model_transformer.py` | _update_status, _map_name_to_node, _get_node_metadata, _get_node_name, _match_node (+17) |
| `quark/onnx/optimizations/optimize.py` | should_quantize_node, convert_bn_to_conv, convert_reduce_mean_to_global_avg_pool, split_large_kernel_pool, convert_split_to_slice (+7) |
| `quark/torch/export/onnx.py` | export_onnx_model_optimization, convert_model_to_uint4_int4, _contain_uint16_or_int16_quant, change_opset_version, fold_quantizers_for_bias |
| `quark/onnx/tools/insert_clip_bfloat16_qdq.py` | insert_clip_bfloat16_qdq, main |
| `quark/onnx/tools/remove_bf16_cast.py` | convert_bf16_cast_to_fp32_weights, remove_bf16_cast |
| `quark/onnx/tools/replace_bfloat16_qdq_cast.py` | replace_bfloat16_qdq_cast, main |
| `quark/torch/algorithm/depth_pruning/layer_importance.py` | _trim_layers, apply |
| `quark/torch/export/api.py` | _export_impl, _import_impl |
| `quark/torch/quantization/api.py` | __init__, init_config |
| `quark/torch/quantization/cache_integration.py` | get_export_state_dict, prepare_cache_for_export |

## Entry Points

Start here when exploring this area:

- **`optimize_model`** (Function) — `quark/onnx/optimizations/interface.py:25`
- **`apply_post_optimization_after_algo`** (Function) — `quark/onnx/postprocess/postproc.py:192`
- **`insert_clip_bfloat16_qdq`** (Function) — `quark/onnx/tools/insert_clip_bfloat16_qdq.py:21`
- **`main`** (Function) — `quark/onnx/tools/insert_clip_bfloat16_qdq.py:62`
- **`convert_bf16_cast_to_fp32_weights`** (Function) — `quark/onnx/tools/remove_bf16_cast.py:106`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `optimize_model` | Function | `quark/onnx/optimizations/interface.py` | 25 |
| `apply_post_optimization_after_algo` | Function | `quark/onnx/postprocess/postproc.py` | 192 |
| `insert_clip_bfloat16_qdq` | Function | `quark/onnx/tools/insert_clip_bfloat16_qdq.py` | 21 |
| `main` | Function | `quark/onnx/tools/insert_clip_bfloat16_qdq.py` | 62 |
| `convert_bf16_cast_to_fp32_weights` | Function | `quark/onnx/tools/remove_bf16_cast.py` | 106 |
| `remove_bf16_cast` | Function | `quark/onnx/tools/remove_bf16_cast.py` | 201 |
| `replace_bfloat16_qdq_cast` | Function | `quark/onnx/tools/replace_bfloat16_qdq_cast.py` | 22 |
| `main` | Function | `quark/onnx/tools/replace_bfloat16_qdq_cast.py` | 146 |
| `replace_inf_in_onnx_weights` | Function | `quark/onnx/tools/replace_inf_weights.py` | 24 |
| `export_onnx_model_optimization` | Function | `quark/torch/export/onnx.py` | 23 |
| `convert_model_to_uint4_int4` | Function | `quark/torch/export/onnx.py` | 39 |
| `change_opset_version` | Function | `quark/torch/export/onnx.py` | 98 |
| `fold_quantizers_for_bias` | Function | `quark/torch/export/onnx.py` | 142 |
| `prepare_cache_for_export` | Function | `quark/torch/quantization/cache_integration.py` | 620 |
| `cross_layer_equalization` | Function | `quark/torch/quantization/graph/optimization/pre_quant/cross_layer_equaliztion.py` | 166 |
| `prepare_model_for_cache_export` | Function | `quark/torch/quantization/model_transformation.py` | 182 |
| `test_fp8_attn_asq` | Function | `test/test_for_torch/test_fp8_attn_asq.py` | 34 |
| `compute_percentile` | Method | `quark/onnx/calibration/collectors.py` | 103 |
| `should_quantize_node` | Method | `quark/onnx/optimizations/optimize.py` | 47 |
| `convert_bn_to_conv` | Method | `quark/onnx/optimizations/optimize.py` | 69 |

## Execution Flows

| Flow | Type | Steps |
|------|------|-------|
| `Bias_correction → Info` | cross_community | 5 |
| `Apply_post_quant_algorithms → Info` | cross_community | 4 |
| `Optimize_model → Info` | intra_community | 3 |
| `Optimize_model → Debug` | cross_community | 3 |
| `Optimize_model → Should_quantize_node` | intra_community | 3 |
| `Optimize_model → Replace_node_with` | intra_community | 3 |
| `Optimize_model → Warning` | cross_community | 3 |
| `Quantize_model → Info` | cross_community | 3 |
| `Simulate_transforms → Info` | cross_community | 3 |
| `Apply → Info` | intra_community | 3 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Passes | 27 calls |
| Refinement | 9 calls |
| Quantization | 6 calls |
| Test_for_torch | 2 calls |
| Export | 1 calls |
| Awq | 1 calls |
| Post_calib | 1 calls |
| Processor | 1 calls |

## How to Explore

1. `gitnexus_context({name: "optimize_model"})` — see callers and callees
2. `gitnexus_query({query: "optimizations"})` — find related execution flows
3. Read key files listed above for implementation details
