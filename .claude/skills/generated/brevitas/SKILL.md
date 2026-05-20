---
name: brevitas
description: "Skill for the Brevitas area of Quark. 53 symbols across 9 files."
---

# Brevitas

53 symbols | 9 files | Cohesion: 89%

## When to Use

- Working with code in `quark/`
- Understanding how validate, main, create_quantized_model work
- Modifying brevitas-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `test/test_for_torch/extensions/brevitas/test_verify.py` | test_valid_default_config, test_unsupported_backend, test_missing_floating_point_parameters, test_invalid_incorrect_algorithm_parameter, test_invalid_algorithm_combinations (+7) |
| `quark/torch/extensions/brevitas/algos.py` | _calibrate, AlgoConfig, GPFQ, GPFA2Q, GPTQ (+5) |
| `test/test_for_torch/extensions/brevitas/test_algos.py` | create_quantized_model, test_calibrate, test_algo_config_default_apply, test_pre_quant_default_apply, create_dataloader (+3) |
| `quark/torch/extensions/brevitas/verification.py` | verify_config, _verify_global_config, _verify_spec_common, _verify_activation_quant_spec, _verify_weight_quant_spec (+2) |
| `quark/torch/extensions/brevitas/api.py` | ModelQuantizer, _parse_activation_quant_spec, _create_layer_map, quantize_model, ModelExporter |
| `quark/torch/extensions/brevitas/config.py` | Config, QTensorConfig, QLayerConfig |
| `test/test_for_torch/extensions/brevitas/test_api.py` | test_basic_quantization_no_calibration_data, test_missing_calibration_data, test_basic_export_no_error |
| `examples/torch/extensions/brevitas/adapter.py` | quantize_model, _prepare_model, _prepare_model_fx |
| `examples/torch/extensions/brevitas/imagenet_classification/quantize_brevitas.py` | validate, main |

## Entry Points

Start here when exploring this area:

- **`validate`** (Function) — `examples/torch/extensions/brevitas/imagenet_classification/quantize_brevitas.py:108`
- **`main`** (Function) — `examples/torch/extensions/brevitas/imagenet_classification/quantize_brevitas.py:161`
- **`create_quantized_model`** (Function) — `test/test_for_torch/extensions/brevitas/test_algos.py:41`
- **`test_calibrate`** (Function) — `test/test_for_torch/extensions/brevitas/test_algos.py:104`
- **`test_basic_quantization_no_calibration_data`** (Function) — `test/test_for_torch/extensions/brevitas/test_api.py:40`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `ModelQuantizer` | Class | `quark/torch/extensions/brevitas/api.py` | 63 |
| `ModelExporter` | Class | `quark/torch/extensions/brevitas/api.py` | 245 |
| `Config` | Class | `quark/torch/extensions/brevitas/config.py` | 25 |
| `QTensorConfig` | Class | `quark/torch/extensions/brevitas/config.py` | 129 |
| `QLayerConfig` | Class | `quark/torch/extensions/brevitas/config.py` | 134 |
| `AlgoConfig` | Class | `quark/torch/extensions/brevitas/algos.py` | 36 |
| `GPFQ` | Class | `quark/torch/extensions/brevitas/algos.py` | 115 |
| `GPFA2Q` | Class | `quark/torch/extensions/brevitas/algos.py` | 158 |
| `GPTQ` | Class | `quark/torch/extensions/brevitas/algos.py` | 202 |
| `CalibrateBatchNorm` | Class | `quark/torch/extensions/brevitas/algos.py` | 234 |
| `BiasCorrection` | Class | `quark/torch/extensions/brevitas/algos.py` | 253 |
| `PreQuantOptConfig` | Class | `quark/torch/extensions/brevitas/algos.py` | 28 |
| `Preprocess` | Class | `quark/torch/extensions/brevitas/algos.py` | 43 |
| `ActivationEqualization` | Class | `quark/torch/extensions/brevitas/algos.py` | 80 |
| `validate` | Function | `examples/torch/extensions/brevitas/imagenet_classification/quantize_brevitas.py` | 108 |
| `main` | Function | `examples/torch/extensions/brevitas/imagenet_classification/quantize_brevitas.py` | 161 |
| `create_quantized_model` | Function | `test/test_for_torch/extensions/brevitas/test_algos.py` | 41 |
| `test_calibrate` | Function | `test/test_for_torch/extensions/brevitas/test_algos.py` | 104 |
| `test_basic_quantization_no_calibration_data` | Function | `test/test_for_torch/extensions/brevitas/test_api.py` | 40 |
| `test_missing_calibration_data` | Function | `test/test_for_torch/extensions/brevitas/test_api.py` | 63 |

## Execution Flows

| Flow | Type | Steps |
|------|------|-------|
| `Main → Preprocess` | cross_community | 3 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Passes | 8 calls |
| Optimizations | 4 calls |

## How to Explore

1. `gitnexus_context({name: "validate"})` — see callers and callees
2. `gitnexus_query({query: "brevitas"})` — find related execution flows
3. Read key files listed above for implementation details
