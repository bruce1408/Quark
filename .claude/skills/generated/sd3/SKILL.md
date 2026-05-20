---
name: sd3
description: "Skill for the Sd3 area of Quark. 138 symbols across 68 files."
---

# Sd3

138 symbols | 68 files | Cohesion: 81%

## When to Use

- Working with code in `quark/`
- Understanding how find_nodes_by_input, find_consts, is_output_edge work
- Modifying sd3-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/matcher.py` | find_nodes_by_input, find_consts, is_output_edge, is_output_edge_or_adjacent, get_shapes (+22) |
| `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/transform/cast.py` | _add_cast, float_to_bfloat16, float16_to_bfloat16, bfloat16_to_float16, add_cast_dtype_to_bfloat16 (+2) |
| `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/passes/sd3/dit160_fusion.py` | _get_matmul_params, is_dit160_fusion_supported, get_dit160_fusion_wsize, weights_shuffle_dit160fusion, replacement |
| `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/passes/sd3/ditfusion_tbib_bf.py` | _get_matmul_params, is_dittbib_supported, weights_shuffle_dittbib, replacement |
| `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/passes/sd3/dynamic_pad_mmdit.py` | make_dynamic_pad_node, make_shape_gather_nodes, make_arith_node, replacement |
| `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/passes/sd3/mha_to_sd_mha_with_gemm_concat_trans.py` | is_supported_pattern, merge_attributes_flattened, make_sd_gemm_concat_node, replacement |
| `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/passes/sd_bfp/bfp_utils.py` | add_pre_cast, add_post_cast, get_in_dtypes, wrap |
| `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/passes/sd3/whitebox_checker.py` | prepare_op_info, check_op_info_exist, shape_checker, run |
| `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/passes/phi3_5/matmulnbits_to_sd_matmulnbits.py` | get_matmulnbits_params, is_matmulnbits_supported, replacement |
| `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/passes/sd3/mul_add_to_sd_mul_add.py` | get_mul_add_inputs, is_supported_pattern, replacement |

## Entry Points

Start here when exploring this area:

- **`find_nodes_by_input`** (Function) — `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/matcher.py:75`
- **`find_consts`** (Function) — `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/matcher.py:184`
- **`is_output_edge`** (Function) — `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/matcher.py:223`
- **`is_output_edge_or_adjacent`** (Function) — `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/matcher.py:227`
- **`get_shapes`** (Function) — `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/matcher.py:247`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `find_nodes_by_input` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/matcher.py` | 75 |
| `find_consts` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/matcher.py` | 184 |
| `is_output_edge` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/matcher.py` | 223 |
| `is_output_edge_or_adjacent` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/matcher.py` | 227 |
| `get_shapes` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/matcher.py` | 247 |
| `get_shape` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/matcher.py` | 254 |
| `get_dtype` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/matcher.py` | 285 |
| `get_external_data_for_tensor` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/matcher.py` | 381 |
| `load_tensor` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/matcher.py` | 405 |
| `add_attribute` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/matcher.py` | 424 |
| `delete_attribute` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/matcher.py` | 452 |
| `set_attribute` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/matcher.py` | 462 |
| `copy_attributes` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/matcher.py` | 467 |
| `is_initializer` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/matcher.py` | 502 |
| `get_initializer` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/matcher.py` | 524 |
| `get_initializer_as_numpy` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/matcher.py` | 565 |
| `get_initializer_or_const` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/matcher.py` | 596 |
| `get_initializers` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/matcher.py` | 836 |
| `find_initializers_by_nodes` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/matcher.py` | 848 |
| `find_inputs_by_nodes` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/matcher.py` | 877 |

## Execution Flows

| Flow | Type | Steps |
|------|------|-------|
| `Replacement → Is_initializer` | intra_community | 6 |
| `Replacement → Get_external_data_for_tensor` | intra_community | 6 |
| `Replacement → Is_initializer` | cross_community | 6 |
| `Replacement → Get_external_data_for_tensor` | cross_community | 6 |
| `Replacement → Is_initializer` | intra_community | 6 |
| `Replacement → Get_external_data_for_tensor` | intra_community | 6 |
| `Wrap → Is_initializer` | intra_community | 6 |
| `Wrap → Get_external_data_for_tensor` | intra_community | 6 |
| `Replacement → Is_initializer` | cross_community | 6 |
| `Replacement → Get_external_data_for_tensor` | cross_community | 6 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Sd15 | 18 calls |
| Passes | 15 calls |
| Ryzenai_onnx_utils | 3 calls |
| Sd_bfp | 2 calls |

## How to Explore

1. `gitnexus_context({name: "find_nodes_by_input"})` — see callers and callees
2. `gitnexus_query({query: "sd3"})` — find related execution flows
3. Read key files listed above for implementation details
