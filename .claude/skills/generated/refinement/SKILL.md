---
name: refinement
description: "Skill for the Refinement area of Quark. 50 symbols across 11 files."
---

# Refinement

50 symbols | 11 files | Cohesion: 64%

## When to Use

- Working with code in `quark/`
- Understanding how get_modules_optimized_bias, adjust_quantize_info, main work
- Modifying refinement-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `quark/onnx/postprocess/refinement/refine.py` | set_scale, set_pos, find_node_name, get_ipos_name, get_ipos_name_by_id (+30) |
| `quark/torch/quantization/cache_integration.py` | load_from_state_dict, _load_kv_scales_from_state_dict, patch_model_with_quark_cache |
| `quark/onnx_adapter/passes/onnx_fuse_instance_norm.py` | _onnx_fuse_instance_norm, _run_for_config |
| `quark/onnx_adapter/passes/onnx_fuse_l2_norm.py` | _onnx_fuse_l2_norm, _run_for_config |
| `quark/torch/algorithm/rotation/cayley.py` | unit, step |
| `quark/onnx/algorithm/finetuning/create_torch/create_model_ops.py` | get_modules_optimized_bias |
| `quark/onnx/tools/save_weights_hist.py` | main |
| `quark/onnx_adapter/passes/remove_qdq.py` | _run_for_pattern |
| `quark/shares/utils/log.py` | debug |
| `quark/torch/quantization/model_transformation.py` | _setup_cache_based_kv_quantization_post_quantization |

## Entry Points

Start here when exploring this area:

- **`get_modules_optimized_bias`** (Function) — `quark/onnx/algorithm/finetuning/create_torch/create_model_ops.py:598`
- **`adjust_quantize_info`** (Function) — `quark/onnx/postprocess/refinement/refine.py:680`
- **`main`** (Function) — `quark/onnx/tools/save_weights_hist.py:34`
- **`unit`** (Function) — `quark/torch/algorithm/rotation/cayley.py:23`
- **`patch_model_with_quark_cache`** (Function) — `quark/torch/quantization/cache_integration.py:498`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `get_modules_optimized_bias` | Function | `quark/onnx/algorithm/finetuning/create_torch/create_model_ops.py` | 598 |
| `adjust_quantize_info` | Function | `quark/onnx/postprocess/refinement/refine.py` | 680 |
| `main` | Function | `quark/onnx/tools/save_weights_hist.py` | 34 |
| `unit` | Function | `quark/torch/algorithm/rotation/cayley.py` | 23 |
| `patch_model_with_quark_cache` | Function | `quark/torch/quantization/cache_integration.py` | 498 |
| `test_logging_levels` | Function | `test/test_for_torch/test_logging.py` | 12 |
| `align_quantize_info` | Function | `quark/onnx/postprocess/refinement/refine.py` | 939 |
| `set_scale` | Method | `quark/onnx/postprocess/refinement/refine.py` | 52 |
| `set_pos` | Method | `quark/onnx/postprocess/refinement/refine.py` | 73 |
| `find_node_name` | Method | `quark/onnx/postprocess/refinement/refine.py` | 88 |
| `get_ipos_name` | Method | `quark/onnx/postprocess/refinement/refine.py` | 94 |
| `get_ipos_name_by_id` | Method | `quark/onnx/postprocess/refinement/refine.py` | 110 |
| `get_node_by_name` | Method | `quark/onnx/postprocess/refinement/refine.py` | 117 |
| `get_pos_by_name` | Method | `quark/onnx/postprocess/refinement/refine.py` | 123 |
| `find_o_name` | Method | `quark/onnx/postprocess/refinement/refine.py` | 130 |
| `get_opos_name` | Method | `quark/onnx/postprocess/refinement/refine.py` | 136 |
| `get_wpos_name` | Method | `quark/onnx/postprocess/refinement/refine.py` | 160 |
| `get_bpos_name` | Method | `quark/onnx/postprocess/refinement/refine.py` | 167 |
| `adjust_shift_cut` | Method | `quark/onnx/postprocess/refinement/refine.py` | 174 |
| `adjust_shift_bias` | Method | `quark/onnx/postprocess/refinement/refine.py` | 215 |

## Execution Flows

| Flow | Type | Steps |
|------|------|-------|
| `Apply_post_quant_algorithms → Debug` | cross_community | 6 |
| `Adjust_shift_bias → Is_approximately_equal` | cross_community | 6 |
| `Adjust_shift_swish → Is_approximately_equal` | cross_community | 6 |
| `Adjust_quantize_info → Get_scale` | cross_community | 5 |
| `Adjust_quantize_info → Scale2pos` | cross_community | 5 |
| `Get_cle_pattern_pair → Debug` | cross_community | 5 |
| `Adjust_quantize_info → Find_o_name` | intra_community | 4 |
| `Adjust_quantize_info → Find_node_name` | intra_community | 4 |
| `Adjust_shift_write → Get_scale` | cross_community | 4 |
| `Adjust_shift_write → Scale2pos` | cross_community | 4 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Optimizations | 32 calls |
| Passes | 6 calls |
| Quantization | 5 calls |
| Mprecision | 1 calls |
| Quantizers | 1 calls |
| Test_for_onnx | 1 calls |

## How to Explore

1. `gitnexus_context({name: "get_modules_optimized_bias"})` — see callers and callees
2. `gitnexus_query({query: "refinement"})` — find related execution flows
3. Read key files listed above for implementation details
