---
name: post-quant
description: "Skill for the Post_quant area of Quark. 54 symbols across 7 files."
---

# Post_quant

54 symbols | 7 files | Cohesion: 52%

## When to Use

- Working with code in `quark/`
- Understanding how test_torch_postquant_concat_strategy, test_torch_adjust_shift_read_strategy, test_torch_adjust_shift_write_strategy work
- Modifying post_quant-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `quark/torch/quantization/graph/optimization/post_quant/opt_pass_after_quant_powof2_scale.py` | ConvertClip2ReLUQOPass, ApplyConstrain2ConcatQOPass, AdjustShiftReadQOPass, AdjustShiftWriteQOPass, AdjustHardSigmoidQOPass (+24) |
| `test/test_for_torch/test_fx_quant_align_hw_pow_of_2.py` | test_torch_postquant_concat_strategy, test_torch_adjust_shift_read_strategy, test_torch_adjust_shift_write_strategy, test_torch_adjust_hard_sigmoid_strategy, test_torch_align_single_in_out_strategy (+3) |
| `quark/torch/quantization/graph/optimization/post_quant/opt_pass_after_quant_float_scale.py` | _is_has_one_user_and_followed_quantizer, _make_iterable, get_target_node, call, get_target_node (+3) |
| `quark/torch/quantization/graph/optimization/utils.py` | is_quantizer_node, get_quantizer_scale_pos, get_quantizer_powof2_scale_pos, is_quantizer |
| `quark/torch/quantization/graph/torch_utils.py` | is_clip_node, is_hardsigmoid_node, is_cat_node |
| `quark/torch/quantization/graph/optimization/model_optimization.py` | _apply_post_hw_powof2_constrain_passes |
| `test/test_for_torch/test_fx_quant_align_hw_float_scale.py` | test_torch_align_slice_strategy |

## Entry Points

Start here when exploring this area:

- **`test_torch_postquant_concat_strategy`** (Function) — `test/test_for_torch/test_fx_quant_align_hw_pow_of_2.py:1477`
- **`test_torch_adjust_shift_read_strategy`** (Function) — `test/test_for_torch/test_fx_quant_align_hw_pow_of_2.py:1692`
- **`test_torch_adjust_shift_write_strategy`** (Function) — `test/test_for_torch/test_fx_quant_align_hw_pow_of_2.py:1768`
- **`test_torch_adjust_hard_sigmoid_strategy`** (Function) — `test/test_for_torch/test_fx_quant_align_hw_pow_of_2.py:1989`
- **`is_clip_node`** (Function) — `quark/torch/quantization/graph/torch_utils.py:230`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `ConvertClip2ReLUQOPass` | Class | `quark/torch/quantization/graph/optimization/post_quant/opt_pass_after_quant_powof2_scale.py` | 82 |
| `ApplyConstrain2ConcatQOPass` | Class | `quark/torch/quantization/graph/optimization/post_quant/opt_pass_after_quant_powof2_scale.py` | 139 |
| `AdjustShiftReadQOPass` | Class | `quark/torch/quantization/graph/optimization/post_quant/opt_pass_after_quant_powof2_scale.py` | 318 |
| `AdjustShiftWriteQOPass` | Class | `quark/torch/quantization/graph/optimization/post_quant/opt_pass_after_quant_powof2_scale.py` | 377 |
| `AdjustHardSigmoidQOPass` | Class | `quark/torch/quantization/graph/optimization/post_quant/opt_pass_after_quant_powof2_scale.py` | 650 |
| `AdjustShiftSwishQOPass` | Class | `quark/torch/quantization/graph/optimization/post_quant/opt_pass_after_quant_powof2_scale.py` | 718 |
| `ConvertHardSigmoidDpuVersionQOPass` | Class | `quark/torch/quantization/graph/optimization/post_quant/opt_pass_after_quant_powof2_scale.py` | 823 |
| `AlignSingleInOutScaleBase` | Class | `quark/torch/quantization/graph/optimization/post_quant/opt_pass_after_quant_powof2_scale.py` | 217 |
| `AlignSingleInOutOpScaleQOPass` | Class | `quark/torch/quantization/graph/optimization/post_quant/opt_pass_after_quant_powof2_scale.py` | 287 |
| `AlignSingleInOutModuleScaleQOPass` | Class | `quark/torch/quantization/graph/optimization/post_quant/opt_pass_after_quant_powof2_scale.py` | 299 |
| `AdjustShiftBase` | Class | `quark/torch/quantization/graph/optimization/post_quant/opt_pass_after_quant_powof2_scale.py` | 468 |
| `AdjustShiftCutQOPass` | Class | `quark/torch/quantization/graph/optimization/post_quant/opt_pass_after_quant_powof2_scale.py` | 526 |
| `AdjustShiftBiasQOPass` | Class | `quark/torch/quantization/graph/optimization/post_quant/opt_pass_after_quant_powof2_scale.py` | 578 |
| `AliginScaleInputToOutputBase` | Class | `quark/torch/quantization/graph/optimization/post_quant/opt_pass_after_quant_float_scale.py` | 109 |
| `AlignSliceQOPass` | Class | `quark/torch/quantization/graph/optimization/post_quant/opt_pass_after_quant_float_scale.py` | 210 |
| `test_torch_postquant_concat_strategy` | Function | `test/test_for_torch/test_fx_quant_align_hw_pow_of_2.py` | 1477 |
| `test_torch_adjust_shift_read_strategy` | Function | `test/test_for_torch/test_fx_quant_align_hw_pow_of_2.py` | 1692 |
| `test_torch_adjust_shift_write_strategy` | Function | `test/test_for_torch/test_fx_quant_align_hw_pow_of_2.py` | 1768 |
| `test_torch_adjust_hard_sigmoid_strategy` | Function | `test/test_for_torch/test_fx_quant_align_hw_pow_of_2.py` | 1989 |
| `is_clip_node` | Function | `quark/torch/quantization/graph/torch_utils.py` | 230 |

## Execution Flows

| Flow | Type | Steps |
|------|------|-------|
| `Call → Is_call_module_node` | cross_community | 5 |
| `Call → Is_call_module_node` | cross_community | 4 |
| `Call → Is_call_module_node` | cross_community | 4 |
| `Call → Is_hardsigmoid_node` | intra_community | 4 |
| `Call → Warning` | cross_community | 4 |
| `Call → Warning` | cross_community | 3 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Passes | 31 calls |
| Optimizations | 15 calls |
| Optimization | 12 calls |
| Test_for_torch | 9 calls |
| Post_calib | 2 calls |
| Pre_quant | 2 calls |

## How to Explore

1. `gitnexus_context({name: "test_torch_postquant_concat_strategy"})` — see callers and callees
2. `gitnexus_query({query: "post_quant"})` — find related execution flows
3. Read key files listed above for implementation details
