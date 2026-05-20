---
name: processor
description: "Skill for the Processor area of Quark. 58 symbols across 13 files."
---

# Processor

58 symbols | 13 files | Cohesion: 79%

## When to Use

- Working with code in `quark/`
- Understanding how propagate_annotation, add_node_input, get_weight_qspec work
- Modifying processor-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `quark/torch/quantization/graph/processor/processor_utils.py` | _is_annotated, _is_skip_quant_node, propagate_annotation, add_node_input, get_weight_qspec (+24) |
| `quark/torch/quantization/graph/processor/insert_quantizer.py` | _create_fakequantize_from_qspec, _get_node_to_fakequantize_map, _insert_quantizer_for_quantized_module, _insert_fakequantize_on_model, insert_quantizer |
| `quark/torch/quantization/graph/processor/pre_check_befor_quant.py` | _all_model_checks, _all_config_checks, pre_quant_model_and_config_checks, check_supported_model_and_config, _delete_guards_fn_if_torch_gt_290 |
| `quark/torch/quantization/graph/processor/tag_quant_node.py` | _mark_node_skip_quant, tag_quant_nodes, depth_first_search, width_first_search |
| `quark/torch/quantization/graph/torch_utils.py` | is_conv_like_node, is_slice_node, is_math_arithmetic_node |
| `quark/torch/quantization/graph/graph_modelquantizer.py` | _annotate_and_insert_quantizer, _pre_check_before_quant, _pre_quant_optimize |
| `quark/torch/quantization/graph/processor/processor.py` | annotate, prepare_quant_model, mark_exclude_nodes |
| `quark/torch/quantization/graph/optimization/pre_quant/opt_pass_before_quant.py` | call |
| `quark/torch/quantization/graph/optimization/model_optimization.py` | select_proper_hw_constrain_passes |
| `test/test_for_torch/test_graph_optim_condition_check.py` | test_graph_conv_weight_replace_condition |

## Entry Points

Start here when exploring this area:

- **`propagate_annotation`** (Function) — `quark/torch/quantization/graph/processor/processor_utils.py:147`
- **`add_node_input`** (Function) — `quark/torch/quantization/graph/processor/processor_utils.py:173`
- **`get_weight_qspec`** (Function) — `quark/torch/quantization/graph/processor/processor_utils.py:184`
- **`get_bias_qspec`** (Function) — `quark/torch/quantization/graph/processor/processor_utils.py:196`
- **`get_input_act_qspec`** (Function) — `quark/torch/quantization/graph/processor/processor_utils.py:208`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `propagate_annotation` | Function | `quark/torch/quantization/graph/processor/processor_utils.py` | 147 |
| `add_node_input` | Function | `quark/torch/quantization/graph/processor/processor_utils.py` | 173 |
| `get_weight_qspec` | Function | `quark/torch/quantization/graph/processor/processor_utils.py` | 184 |
| `get_bias_qspec` | Function | `quark/torch/quantization/graph/processor/processor_utils.py` | 196 |
| `get_input_act_qspec` | Function | `quark/torch/quantization/graph/processor/processor_utils.py` | 208 |
| `get_output_act_qspec` | Function | `quark/torch/quantization/graph/processor/processor_utils.py` | 220 |
| `is_conv_like_node` | Function | `quark/torch/quantization/graph/torch_utils.py` | 132 |
| `is_slice_node` | Function | `quark/torch/quantization/graph/torch_utils.py` | 262 |
| `is_math_arithmetic_node` | Function | `quark/torch/quantization/graph/torch_utils.py` | 274 |
| `select_proper_hw_constrain_passes` | Function | `quark/torch/quantization/graph/optimization/model_optimization.py` | 220 |
| `annotate` | Function | `quark/torch/quantization/graph/processor/processor.py` | 89 |
| `prepare_quant_model` | Function | `quark/torch/quantization/graph/processor/processor.py` | 126 |
| `test_graph_conv_weight_replace_condition` | Function | `test/test_for_torch/test_graph_optim_condition_check.py` | 146 |
| `insert_quantizer` | Function | `quark/torch/quantization/graph/processor/insert_quantizer.py` | 155 |
| `pre_quant_model_and_config_checks` | Function | `quark/torch/quantization/graph/processor/pre_check_befor_quant.py` | 76 |
| `mark_exclude_quant_node` | Function | `quark/torch/quantization/graph/processor/node_annotate.py` | 15 |
| `mark_exclude_nodes` | Function | `quark/torch/quantization/graph/processor/processor.py` | 116 |
| `test_torch_quant_stub` | Function | `test/test_for_torch/test_fx_stub.py` | 143 |
| `tag_quant_nodes` | Function | `quark/torch/quantization/graph/processor/tag_quant_node.py` | 22 |
| `depth_first_search` | Function | `quark/torch/quantization/graph/processor/tag_quant_node.py` | 50 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Pre_quant | 7 calls |
| Passes | 5 calls |
| Optimizations | 3 calls |
| Post_quant | 3 calls |
| Optimization | 2 calls |
| Refinement | 1 calls |
| Test_for_torch | 1 calls |
| Quantization | 1 calls |

## How to Explore

1. `gitnexus_context({name: "propagate_annotation"})` — see callers and callees
2. `gitnexus_query({query: "processor"})` — find related execution flows
3. Read key files listed above for implementation details
