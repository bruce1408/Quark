---
name: modules
description: "Skill for the Modules area of Quark. 52 symbols across 9 files."
---

# Modules

52 symbols | 9 files | Cohesion: 78%

## When to Use

- Working with code in `quark/`
- Understanding how test_fp4_per_group_fp8_per_tensor_scale_real_quantize, test_fp8_int4_perchannel_quantize, get_real_quantizer work
- Modifying modules-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `quark/torch/export/nn/modules/realquantizer.py` | unpack_tensor, unpack_params, forward, get_real_quantizer, create_observer (+5) |
| `quark/torch/export/nn/modules/qparamslinear.py` | __init__, _init_qparamlinear, _init_from_quantlinear, _real_quantize, _init_from_linear (+4) |
| `quark/torch/quantization/nn/modules/quantize_conv_bn_fused.py` | _ConvBnNd, _ConvTransposeBnNd, __init__, reset_bn_parameters, freeze_bn_stats (+4) |
| `quark/torch/quantization/nn/modules/quantize_conv.py` | forward, forward, __init__, __init__, _QuantizedConvNd (+2) |
| `quark/torch/quantization/nn/modules/mixin.py` | get_quant_input, get_quant_output, get_quant_weight, get_quant_bias, init_quantizer (+1) |
| `quark/torch/quantization/nn/modules/quantize_linear.py` | forward, forward_with_weight, forward, __init__, __init__ (+1) |
| `quark/torch/quantization/nn/modules/quantize_pool.py` | forward, forward |
| `test/test_for_torch/test_real_quantizer.py` | test_fp4_per_group_fp8_per_tensor_scale_real_quantize, test_fp8_int4_perchannel_quantize |
| `quark/torch/quantization/nn/modules/quantize_leakyrelu.py` | forward |

## Entry Points

Start here when exploring this area:

- **`test_fp4_per_group_fp8_per_tensor_scale_real_quantize`** (Function) — `test/test_for_torch/test_real_quantizer.py:30`
- **`test_fp8_int4_perchannel_quantize`** (Function) — `test/test_for_torch/test_real_quantizer.py:121`
- **`get_real_quantizer`** (Function) — `quark/torch/export/nn/modules/realquantizer.py:636`
- **`QuantMixin`** (Class) — `quark/torch/quantization/nn/modules/mixin.py:12`
- **`QuantLinear`** (Class) — `quark/torch/quantization/nn/modules/quantize_linear.py:29`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `QuantMixin` | Class | `quark/torch/quantization/nn/modules/mixin.py` | 12 |
| `QuantLinear` | Class | `quark/torch/quantization/nn/modules/quantize_linear.py` | 29 |
| `RealQuantizerBase` | Class | `quark/torch/export/nn/modules/realquantizer.py` | 27 |
| `StaticRealQuantizer` | Class | `quark/torch/export/nn/modules/realquantizer.py` | 66 |
| `test_fp4_per_group_fp8_per_tensor_scale_real_quantize` | Function | `test/test_for_torch/test_real_quantizer.py` | 30 |
| `test_fp8_int4_perchannel_quantize` | Function | `test/test_for_torch/test_real_quantizer.py` | 121 |
| `get_real_quantizer` | Function | `quark/torch/export/nn/modules/realquantizer.py` | 636 |
| `get_quant_input` | Method | `quark/torch/quantization/nn/modules/mixin.py` | 73 |
| `get_quant_output` | Method | `quark/torch/quantization/nn/modules/mixin.py` | 81 |
| `forward` | Method | `quark/torch/quantization/nn/modules/quantize_conv.py` | 207 |
| `forward` | Method | `quark/torch/quantization/nn/modules/quantize_leakyrelu.py` | 38 |
| `forward` | Method | `quark/torch/quantization/nn/modules/quantize_pool.py` | 41 |
| `forward` | Method | `quark/torch/quantization/nn/modules/quantize_pool.py` | 91 |
| `get_quant_weight` | Method | `quark/torch/quantization/nn/modules/mixin.py` | 89 |
| `get_quant_bias` | Method | `quark/torch/quantization/nn/modules/mixin.py` | 97 |
| `forward` | Method | `quark/torch/quantization/nn/modules/quantize_conv.py` | 70 |
| `forward` | Method | `quark/torch/quantization/nn/modules/quantize_linear.py` | 47 |
| `forward_with_weight` | Method | `quark/torch/quantization/nn/modules/quantize_linear.py` | 50 |
| `forward` | Method | `quark/torch/quantization/nn/modules/quantize_linear.py` | 310 |
| `unpack_tensor` | Method | `quark/torch/export/nn/modules/realquantizer.py` | 105 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Test_for_torch | 4 calls |

## How to Explore

1. `gitnexus_context({name: "test_fp4_per_group_fp8_per_tensor_scale_real_quantize"})` — see callers and callees
2. `gitnexus_query({query: "modules"})` — find related execution flows
3. Read key files listed above for implementation details
