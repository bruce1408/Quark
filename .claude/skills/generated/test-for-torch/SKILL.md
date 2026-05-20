---
name: test-for-torch
description: "Skill for the Test_for_torch area of Quark. 222 symbols across 51 files."
---

# Test_for_torch

222 symbols | 51 files | Cohesion: 80%

## When to Use

- Working with code in `test/`
- Understanding how main, qlora_training, get_daring_anteater work
- Modifying test_for_torch-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `test/test_for_torch/test_llm_template.py` | test_register_template_method, test_supported_schemes, test_int4_wo_32_scheme, test_int4_wo_64_scheme, test_int4_wo_128_scheme (+34) |
| `test/test_for_torch/test_fx_quant_align_hw_pow_of_2.py` | onnx_contains_op_num, fx_contains_op_num, fx_contain_module_num, test_torch_module_used_over_once_optim_strategy, test_torch_clip_2_relu_optim_strategy (+17) |
| `test/test_for_torch/test_smoke.py` | get_dataloader, quantize_model, test_smoke_eager_save_load, test_smoke_autosmoothquant_quantization, set_config_for_awq_or_smooth (+6) |
| `test/test_for_torch/test_graph_annotation.py` | onnx_contains_op_num, fx_contains_op_num, fx_contain_module_num, test_annotation_element_arithmetic, test_annotation_without_grad_skip_quant (+5) |
| `test/test_for_torch/test_awq_autosq_dataset.py` | get_tokenizer, get_dataloader, get_model, quantize_model_pipeline, ppl_eval (+4) |
| `test/test_for_torch/test_hf_export_import.py` | get_dataloader, quantize_model, test_dbrx_import, test_wfp6_e2m3_afp6_e2m3_import, test_wfp6_e3m2_afp6_e3m2_import (+4) |
| `test/test_for_torch/test_fx_quant_align_hw_float_scale.py` | fx_contain_module_num, test_torch_align_concat_strategy, test_torch_align_pool_strategy, test_torch_align_pad_strategy, test_torch_align_transpose_strategy (+2) |
| `test/test_for_torch/test_mx.py` | create_4d_tensor_with_interesting_pattern, test_per_block_to_fake_quantize_mx, generate_test_case_input_normal, generate_test_case_input, load_test_case_result (+2) |
| `test/test_for_torch/test_graph_replace_convbn_to_qtconvbn_cle.py` | conv3x3, conv1x1, __init__, __init__, _make_layer (+2) |
| `test/test_for_torch/test_multi_device_quant_export_import.py` | get_dataloader, quantize_model, test_int8_import_export, test_OOM, get_multi_device_model (+2) |

## Entry Points

Start here when exploring this area:

- **`main`** (Function) — `examples/torch/language_modeling/llm_ptq/experimental/model_recipes/GLM-4.7-Flash/quantize_glm_4.7_flash.py:412`
- **`qlora_training`** (Function) — `examples/torch/language_modeling/llm_qat/qlora_training/qlora_training.py:117`
- **`get_daring_anteater`** (Function) — `examples/torch/language_modeling/llm_qat/qlora_training/utils.py:276`
- **`make_supervised_data_module`** (Function) — `examples/torch/language_modeling/llm_qat/qlora_training/utils.py:341`
- **`test_register_template_method`** (Function) — `test/test_for_torch/test_llm_template.py:45`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `AliginScaleOutputToInputBase` | Class | `quark/torch/quantization/graph/optimization/post_quant/opt_pass_after_quant_float_scale.py` | 51 |
| `AlignConcatQOPass` | Class | `quark/torch/quantization/graph/optimization/post_quant/opt_pass_after_quant_float_scale.py` | 179 |
| `AlignPoolQOPass` | Class | `quark/torch/quantization/graph/optimization/post_quant/opt_pass_after_quant_float_scale.py` | 189 |
| `AlignPadQOPass` | Class | `quark/torch/quantization/graph/optimization/post_quant/opt_pass_after_quant_float_scale.py` | 200 |
| `AlignTransposeQOPass` | Class | `quark/torch/quantization/graph/optimization/post_quant/opt_pass_after_quant_float_scale.py` | 220 |
| `AlignReshapeQOPass` | Class | `quark/torch/quantization/graph/optimization/post_quant/opt_pass_after_quant_float_scale.py` | 230 |
| `main` | Function | `examples/torch/language_modeling/llm_ptq/experimental/model_recipes/GLM-4.7-Flash/quantize_glm_4.7_flash.py` | 412 |
| `qlora_training` | Function | `examples/torch/language_modeling/llm_qat/qlora_training/qlora_training.py` | 117 |
| `get_daring_anteater` | Function | `examples/torch/language_modeling/llm_qat/qlora_training/utils.py` | 276 |
| `make_supervised_data_module` | Function | `examples/torch/language_modeling/llm_qat/qlora_training/utils.py` | 341 |
| `test_register_template_method` | Function | `test/test_for_torch/test_llm_template.py` | 45 |
| `test_supported_schemes` | Function | `test/test_for_torch/test_llm_template.py` | 103 |
| `test_int4_wo_32_scheme` | Function | `test/test_for_torch/test_llm_template.py` | 153 |
| `test_int4_wo_64_scheme` | Function | `test/test_for_torch/test_llm_template.py` | 164 |
| `test_int4_wo_128_scheme` | Function | `test/test_for_torch/test_llm_template.py` | 175 |
| `test_int4_wo_per_channel_scheme` | Function | `test/test_for_torch/test_llm_template.py` | 186 |
| `test_uint4_wo_32_scheme` | Function | `test/test_for_torch/test_llm_template.py` | 199 |
| `test_uint4_wo_64_scheme` | Function | `test/test_for_torch/test_llm_template.py` | 210 |
| `test_uint4_wo_128_scheme` | Function | `test/test_for_torch/test_llm_template.py` | 221 |
| `test_uint4_wo_per_channel_scheme` | Function | `test/test_for_torch/test_llm_template.py` | 232 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Optimizations | 30 calls |
| Pre_quant | 14 calls |
| Observer | 8 calls |
| Passes | 7 calls |
| Config | 7 calls |
| Optimization | 7 calls |
| Hw_emulation | 6 calls |
| Post_quant | 5 calls |

## How to Explore

1. `gitnexus_context({name: "main"})` — see callers and callees
2. `gitnexus_query({query: "test_for_torch"})` — find related execution flows
3. Read key files listed above for implementation details
