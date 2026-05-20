---
name: calibration
description: "Skill for the Calibration area of Quark. 59 symbols across 13 files."
---

# Calibration

59 symbols | 13 files | Cohesion: 61%

## When to Use

- Working with code in `quark/`
- Understanding how main, create_calibrator_power_of_two, optimize_model_using_onnxrt work
- Modifying calibration-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `quark/onnx/calibration/collectors.py` | compute_minmse_worker, _all_dims_equal, _nonbatch_dims_equal, _mostcommon_mode, _percentile_mode (+12) |
| `quark/onnx/calibration/calibrators.py` | create_inference_session, create_inference_session, create_calibrator_power_of_two, CachingDataOnDisk, GetCleanMergedDict (+10) |
| `quark/onnx/calibration/data_readers.py` | __init__, reset_iter, get_next, _get_input_name, load_npy_data (+8) |
| `quark/onnx/utils/model_utils.py` | check_onnx_model, create_infer_session_for_onnx_model, sanitize_model_outputs |
| `quark/onnx/tools/fix_shapes.py` | generate_random_data, infer_all_tensors_shape |
| `quark/onnx/postprocess/postproc.py` | apply_post_quantization_algorithms, apply_post_process |
| `quark/onnx/algorithm/finetuning/create_torch/create_model_test.py` | main |
| `quark/onnx/optimizations/interface.py` | optimize_model_using_onnxrt |
| `quark/onnx/utils/deploy_utils.py` | dump_model |
| `quark/onnx/algorithm/bc/bias_correction.py` | collect_data |

## Entry Points

Start here when exploring this area:

- **`main`** (Function) — `quark/onnx/algorithm/finetuning/create_torch/create_model_test.py:23`
- **`create_calibrator_power_of_two`** (Function) — `quark/onnx/calibration/calibrators.py:1012`
- **`optimize_model_using_onnxrt`** (Function) — `quark/onnx/optimizations/interface.py:127`
- **`generate_random_data`** (Function) — `quark/onnx/tools/fix_shapes.py:70`
- **`infer_all_tensors_shape`** (Function) — `quark/onnx/tools/fix_shapes.py:114`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `OverridedHistogramCalibrater` | Class | `quark/onnx/calibration/calibrators.py` | 279 |
| `PercentileCalibrater` | Class | `quark/onnx/calibration/calibrators.py` | 597 |
| `main` | Function | `quark/onnx/algorithm/finetuning/create_torch/create_model_test.py` | 23 |
| `create_calibrator_power_of_two` | Function | `quark/onnx/calibration/calibrators.py` | 1012 |
| `optimize_model_using_onnxrt` | Function | `quark/onnx/optimizations/interface.py` | 127 |
| `generate_random_data` | Function | `quark/onnx/tools/fix_shapes.py` | 70 |
| `infer_all_tensors_shape` | Function | `quark/onnx/tools/fix_shapes.py` | 114 |
| `dump_model` | Function | `quark/onnx/utils/deploy_utils.py` | 21 |
| `check_onnx_model` | Function | `quark/onnx/utils/model_utils.py` | 515 |
| `create_infer_session_for_onnx_model` | Function | `quark/onnx/utils/model_utils.py` | 697 |
| `compute_minmse_worker` | Function | `quark/onnx/calibration/collectors.py` | 280 |
| `inference_model` | Function | `quark/onnx/algorithm/finetuning/onnx_evaluate.py` | 46 |
| `apply_post_quantization_algorithms` | Function | `quark/onnx/postprocess/postproc.py` | 111 |
| `apply_post_process` | Function | `quark/onnx/postprocess/postproc.py` | 254 |
| `CachingDataOnDisk` | Function | `quark/onnx/calibration/calibrators.py` | 50 |
| `GetCleanMergedDict` | Function | `quark/onnx/calibration/calibrators.py` | 89 |
| `sanitize_model_outputs` | Function | `quark/onnx/utils/model_utils.py` | 751 |
| `get_tensor_type_from_qType` | Function | `quark/onnx/quantization/quant_utils.py` | 427 |
| `GenerateAnEmptyOnnxModel` | Function | `quark/onnx/calibration/calibrators.py` | 40 |
| `cal_layers_minmax` | Function | `quark/onnx/calibration/calibrators.py` | 956 |

## Execution Flows

| Flow | Type | Steps |
|------|------|-------|
| `Apply_post_quant_algorithms → Save_onnx_model_with_external_data` | cross_community | 6 |
| `Apply_post_quant_algorithms → Create_inference_session` | cross_community | 6 |
| `Fast_finetune → Save_onnx_model_with_external_data` | cross_community | 5 |
| `Fast_finetune → Create_inference_session` | cross_community | 5 |
| `Bias_correction → Warning` | cross_community | 5 |
| `Apply_post_quant_algorithms → Get_next` | cross_community | 5 |
| `Apply_post_quant_algorithms → Warning` | cross_community | 5 |
| `Get_next → Warning` | cross_community | 4 |
| `Get_next → Warning` | cross_community | 4 |
| `Get_next → Warning` | cross_community | 4 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Optimizations | 15 calls |
| Passes | 15 calls |
| Quantization | 6 calls |
| Refinement | 5 calls |
| Finetuning | 2 calls |
| Tools | 1 calls |

## How to Explore

1. `gitnexus_context({name: "main"})` — see callers and callees
2. `gitnexus_query({query: "calibration"})` — find related execution flows
3. Read key files listed above for implementation details
