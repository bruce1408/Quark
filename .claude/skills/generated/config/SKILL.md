---
name: config
description: "Skill for the Config area of Quark. 83 symbols across 13 files."
---

# Config

83 symbols | 13 files | Cohesion: 86%

## When to Use

- Working with code in `quark/`
- Understanding how get_per_tensor_observer, get_scale_type, get_round_method work
- Modifying config-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `quark/torch/quantization/config/config.py` | get_per_tensor_observer, get_scale_type, get_round_method, to_quantization_spec, to_quantization_spec (+32) |
| `quark/torch/quantization/config/config_verification.py` | _get_tensor_specs, _check_is_dynamic, _check_is_weight_only, _check_tensors_dynamic, _check_tensors_has_per_tensor_scale (+5) |
| `quark/torch/quantization/config/template.py` | get_supported_schemes, register_scheme, unregister_scheme, get_scheme, _create_global_config (+5) |
| `quark/onnx/quantization/config/maps.py` | _check_q_config, _check_global_config, _map_mixed_precision_tensors, _map_q_config, _check_qlayer_config (+3) |
| `quark/shares/config.py` | BaseConfigImpl, BaseAlgoConfig, BaseQConfig, from_dict |
| `quark/onnx/quantization/config/spec.py` | QTensorConfig, Int8Spec, __init__, __init__ |
| `quark/onnx/quantization/quant_utils.py` | recursive_update, match_subgraphs, get_all_target_nodes |
| `quark/torch/export/main_export/quant_config_parser.py` | from_custom_config, get_layer_quant_config |
| `quark/onnx/quantization/api.py` | quantize_model |
| `quark/onnx/quantization/config/algorithm.py` | _resolove_algo_conflict |

## Entry Points

Start here when exploring this area:

- **`get_per_tensor_observer`** (Function) — `quark/torch/quantization/config/config.py:79`
- **`get_scale_type`** (Function) — `quark/torch/quantization/config/config.py:90`
- **`get_round_method`** (Function) — `quark/torch/quantization/config/config.py:99`
- **`init_quantization_config`** (Function) — `quark/torch/quantization/config/config_verification.py:95`
- **`recursive_update`** (Function) — `quark/onnx/quantization/quant_utils.py:2120`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `BaseConfigImpl` | Class | `quark/shares/config.py` | 23 |
| `BaseAlgoConfig` | Class | `quark/shares/config.py` | 39 |
| `BaseQConfig` | Class | `quark/shares/config.py` | 120 |
| `QConfig` | Class | `quark/torch/quantization/config/config.py` | 125 |
| `TwoStageSpec` | Class | `quark/torch/quantization/config/config.py` | 437 |
| `DataTypeSpec` | Class | `quark/torch/quantization/config/config.py` | 524 |
| `OCP_MXSpec` | Class | `quark/torch/quantization/config/config.py` | 1332 |
| `QATSpec` | Class | `quark/torch/quantization/config/config.py` | 1926 |
| `AlgoConfig` | Class | `quark/torch/quantization/config/config.py` | 2031 |
| `QTensorConfig` | Class | `quark/onnx/quantization/config/spec.py` | 68 |
| `Int8Spec` | Class | `quark/onnx/quantization/config/spec.py` | 114 |
| `get_per_tensor_observer` | Function | `quark/torch/quantization/config/config.py` | 79 |
| `get_scale_type` | Function | `quark/torch/quantization/config/config.py` | 90 |
| `get_round_method` | Function | `quark/torch/quantization/config/config.py` | 99 |
| `init_quantization_config` | Function | `quark/torch/quantization/config/config_verification.py` | 95 |
| `recursive_update` | Function | `quark/onnx/quantization/quant_utils.py` | 2120 |
| `match_subgraphs` | Function | `quark/onnx/quantization/quant_utils.py` | 1979 |
| `get_all_target_nodes` | Function | `quark/onnx/quantization/quant_utils.py` | 2074 |
| `from_float_and_dict` | Function | `quark/torch/quantization/api.py` | 672 |
| `convert_dict_to_spec` | Function | `quark/torch/quantization/config/config.py` | 404 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Passes | 15 calls |
| Test_for_torch | 3 calls |
| Quantization | 2 calls |
| Optimizations | 1 calls |

## How to Explore

1. `gitnexus_context({name: "get_per_tensor_observer"})` — see callers and callees
2. `gitnexus_query({query: "config"})` — find related execution flows
3. Read key files listed above for implementation details
