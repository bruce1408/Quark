---
name: ryzenai-onnx-utils
description: "Skill for the Ryzenai_onnx_utils area of Quark. 137 symbols across 20 files."
---

# Ryzenai_onnx_utils

137 symbols | 20 files | Cohesion: 81%

## When to Use

- Working with code in `quark/`
- Understanding how check_output_cache, generate_lora_bins, llm_postprocess work
- Modifying ryzenai_onnx_utils-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/optimize.py` | _check_output, check_output_cache, generate_lora_bins, llm_postprocess, llm_gpu_eager (+19) |
| `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/preprocess.py` | recurse_add_ifs, add_ifs, check_dynamic_inputs, get_opsets, fix_input_output_shapes (+18) |
| `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/matcher.py` | convert_to_external, delete_custom_metadata_props, get_extractor, load_model, load_extractor (+9) |
| `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/partitioner.py` | pattern_match, replace, partition, recurse, parse_runtime_attributes (+7) |
| `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/lora.py` | cast_bf16bfp16, aie_srs, np_fp32_2_bf16, np_fp32_2_int16, process_lora_flat (+7) |
| `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/pattern_generator.py` | PartitionGraph, get_node_label, is_subgraph, partition, PatternGenerator (+5) |
| `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/pattern_builder.py` | get_model, convert_model_to_pattern, add_input, add_output, _add_edge_data (+4) |
| `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/typing.py` | is_sequence_of, get_domains, get_op_namespaces, _get_properties, _get_subgraph_property (+1) |
| `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/strategy_builder/llm/genai_config.py` | finalize, set_option, set_filename, merge |
| `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/extract.py` | extract_model, extract_supported_nodes, save_intermediate_tensors, main |

## Entry Points

Start here when exploring this area:

- **`check_output_cache`** (Function) — `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/optimize.py:338`
- **`generate_lora_bins`** (Function) — `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/optimize.py:423`
- **`llm_postprocess`** (Function) — `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/optimize.py:484`
- **`llm_gpu_eager`** (Function) — `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/optimize.py:526`
- **`llm_hybrid`** (Function) — `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/optimize.py:532`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `PartitionGraph` | Class | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/pattern_generator.py` | 39 |
| `PatternGenerator` | Class | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/pattern_generator.py` | 417 |
| `check_output_cache` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/optimize.py` | 338 |
| `generate_lora_bins` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/optimize.py` | 423 |
| `llm_postprocess` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/optimize.py` | 484 |
| `llm_gpu_eager` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/optimize.py` | 526 |
| `llm_hybrid` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/optimize.py` | 532 |
| `llm_npu_eager` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/optimize.py` | 540 |
| `llm_token_fusion` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/optimize.py` | 631 |
| `llm_prefill_fusion` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/optimize.py` | 678 |
| `llm_full_fusion` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/optimize.py` | 721 |
| `llm` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/optimize.py` | 801 |
| `main` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/postprocess.py` | 46 |
| `pattern_match` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/partitioner.py` | 703 |
| `generate_pattern` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/passes/dd/dynamic_sd_nodes_to_dd.py` | 14 |
| `generate_pattern` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/passes/dd/llm_prefill_to_dd.py` | 15 |
| `generate_pattern` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/passes/dd/llm_token_to_dd.py` | 14 |
| `get_model` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/pattern_builder.py` | 109 |
| `convert_model_to_pattern` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/pattern_builder.py` | 145 |
| `recurse_add_ifs` | Function | `quark/contrib/onnx_utils/src/ryzenai_onnx_utils/preprocess.py` | 117 |

## Execution Flows

| Flow | Type | Steps |
|------|------|-------|
| `Llm_full_fusion → _config_model_static` | cross_community | 6 |
| `Llm_full_fusion → Write_to_bin` | cross_community | 6 |
| `Llm_full_fusion → Replace` | cross_community | 6 |
| `Llm_full_fusion → Confirm` | cross_community | 6 |
| `Llm_full_fusion → _load_strategy` | cross_community | 6 |
| `Replacement → Is_initializer` | cross_community | 6 |
| `Replacement → Get_external_data_for_tensor` | cross_community | 6 |
| `Replacement → Is_sequence_of` | cross_community | 5 |
| `Replacement → Is_sequence_of` | cross_community | 5 |
| `Replacement → Is_sequence_of` | cross_community | 5 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Sd3 | 7 calls |
| Llm | 4 calls |
| Sd_bfp | 1 calls |
| Sd15 | 1 calls |

## How to Explore

1. `gitnexus_context({name: "check_output_cache"})` — see callers and callees
2. `gitnexus_query({query: "ryzenai_onnx_utils"})` — find related execution flows
3. Read key files listed above for implementation details
