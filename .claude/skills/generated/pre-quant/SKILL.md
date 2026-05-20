---
name: pre-quant
description: "Skill for the Pre_quant area of Quark. 55 symbols across 18 files."
---

# Pre_quant

55 symbols | 18 files | Cohesion: 63%

## When to Use

- Working with code in `quark/`
- Understanding how trans_opsfunc_2_quant_module, convert_scalars_to_attrs, fold_bn_after_concat work
- Modifying pre_quant-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `quark/torch/quantization/graph/optimization/pre_quant/opt_pass_before_quant.py` | call, call, SplitQuantModuleCalledOverOnce, ConvertBn2D2ConvQOPass, ConvertReduceMean2GapQOPass (+16) |
| `quark/torch/quantization/graph/torch_utils.py` | is_linear_node, is_conv2d_node, is_convtranspose2d_node, is_batchnorm_node, is_silu_node (+6) |
| `test/test_for_torch/test_graph_replace_convbn_to_qtconvbn_cle.py` | fx_contain_module_num, test_replace_convbn_to_qt_convnb, test_transposebn_2_quantConvTransposeBatchNorm2d_strategy |
| `quark/torch/quantization/graph/optimization/model_optimization.py` | trans_opsfunc_2_quant_module, apply_pre_hw_constrain_passes |
| `quark/torch/quantization/graph/optimization/pre_quant/fold_bn_after_concat.py` | _check_foldable, fold_bn_after_concat |
| `quark/torch/quantization/graph/optimization/utils.py` | _copy_node_meta_info, is_all_nodes_save_parameters |
| `test/test_for_torch/test_fx_quant_align_hw_pow_of_2.py` | test_use_over_once_module_optim, test_torch_sg_bn2d_to_conv2d_optim_strategy |
| `quark/torch/quantization/graph/processor/processor_utils.py` | _is_call_function_shape_change_node, _is_call_function_pool2d_node |
| `quark/torch/quantization/graph/optimization/pre_quant/convert_scalars_to_attrs.py` | convert_scalars_to_attrs |
| `quark/torch/quantization/graph/optimization/pre_quant/replace_conv2d_to_qtconv2d.py` | replace_conv2d_qtconv2d |

## Entry Points

Start here when exploring this area:

- **`trans_opsfunc_2_quant_module`** (Function) — `quark/torch/quantization/graph/optimization/model_optimization.py:64`
- **`convert_scalars_to_attrs`** (Function) — `quark/torch/quantization/graph/optimization/pre_quant/convert_scalars_to_attrs.py:13`
- **`fold_bn_after_concat`** (Function) — `quark/torch/quantization/graph/optimization/pre_quant/fold_bn_after_concat.py:88`
- **`replace_conv2d_qtconv2d`** (Function) — `quark/torch/quantization/graph/optimization/pre_quant/replace_conv2d_to_qtconv2d.py:21`
- **`replace_conv2dbn_quantizedconv_module`** (Function) — `quark/torch/quantization/graph/optimization/pre_quant/replace_conv_bn_to_qt_model.py:25`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `OptPassBase` | Class | `quark/torch/quantization/graph/optimization/opt_pass_manager.py` | 17 |
| `SplitQuantModuleCalledOverOnce` | Class | `quark/torch/quantization/graph/optimization/pre_quant/opt_pass_before_quant.py` | 58 |
| `ConvertBn2D2ConvQOPass` | Class | `quark/torch/quantization/graph/optimization/pre_quant/opt_pass_before_quant.py` | 103 |
| `ConvertReduceMean2GapQOPass` | Class | `quark/torch/quantization/graph/optimization/pre_quant/opt_pass_before_quant.py` | 229 |
| `ConvertAdaptiveavgpool2d2Quantadaptiveavgpool2DQOPass` | Class | `quark/torch/quantization/graph/optimization/pre_quant/opt_pass_before_quant.py` | 329 |
| `ConverAvgpool2d2QuantAvgPool2dQOPass` | Class | `quark/torch/quantization/graph/optimization/pre_quant/opt_pass_before_quant.py` | 381 |
| `ConvertSplit2SliceQOPass` | Class | `quark/torch/quantization/graph/optimization/pre_quant/opt_pass_before_quant.py` | 452 |
| `SplitLargeKernelPoolQOPass` | Class | `quark/torch/quantization/graph/optimization/pre_quant/opt_pass_before_quant.py` | 570 |
| `ConvertDeleteRedundantSliceQOPass` | Class | `quark/torch/quantization/graph/optimization/pre_quant/opt_pass_before_quant.py` | 672 |
| `ConvertSigmoid2HardSigmoidQOPass` | Class | `quark/torch/quantization/graph/optimization/pre_quant/opt_pass_before_quant.py` | 746 |
| `ConvertSilu2HardswishQOPass` | Class | `quark/torch/quantization/graph/optimization/pre_quant/opt_pass_before_quant.py` | 778 |
| `ConvertLeakyReLu2QuantLeakyReLuQOPass` | Class | `quark/torch/quantization/graph/optimization/pre_quant/opt_pass_before_quant.py` | 808 |
| `trans_opsfunc_2_quant_module` | Function | `quark/torch/quantization/graph/optimization/model_optimization.py` | 64 |
| `convert_scalars_to_attrs` | Function | `quark/torch/quantization/graph/optimization/pre_quant/convert_scalars_to_attrs.py` | 13 |
| `fold_bn_after_concat` | Function | `quark/torch/quantization/graph/optimization/pre_quant/fold_bn_after_concat.py` | 88 |
| `replace_conv2d_qtconv2d` | Function | `quark/torch/quantization/graph/optimization/pre_quant/replace_conv2d_to_qtconv2d.py` | 21 |
| `replace_conv2dbn_quantizedconv_module` | Function | `quark/torch/quantization/graph/optimization/pre_quant/replace_conv_bn_to_qt_model.py` | 25 |
| `replace_convtranspose2d_qtconvtranspose2d` | Function | `quark/torch/quantization/graph/optimization/pre_quant/replace_convtranspose2d_to_qtconvtranspose2d.py` | 22 |
| `replace_linear_qtlinear` | Function | `quark/torch/quantization/graph/optimization/pre_quant/replace_linear_to_qtlinear.py` | 21 |
| `replace_silu_node` | Function | `quark/torch/quantization/graph/optimization/pre_quant/replace_silu_2_sigmoid_mul.py` | 15 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Optimizations | 20 calls |
| Passes | 14 calls |
| Optimization | 11 calls |
| Test_for_torch | 2 calls |
| Post_quant | 1 calls |
| Processor | 1 calls |

## How to Explore

1. `gitnexus_context({name: "trans_opsfunc_2_quant_module"})` — see callers and callees
2. `gitnexus_query({query: "pre_quant"})` — find related execution flows
3. Read key files listed above for implementation details
