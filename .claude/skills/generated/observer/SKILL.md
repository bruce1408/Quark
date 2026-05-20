---
name: observer
description: "Skill for the Observer area of Quark. 56 symbols across 9 files."
---

# Observer

56 symbols | 9 files | Cohesion: 74%

## When to Use

- Working with code in `quark/`
- Understanding how calculate_qmin_qmax, get_num_bits, get_dtype_params work
- Modifying observer-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `quark/torch/quantization/observer/observer.py` | __init__, __init__, __init__, __init__, __init__ (+35) |
| `quark/torch/quantization/utils.py` | calculate_qmin_qmax, get_num_bits, get_dtype_params, even_round |
| `quark/torch/export/nn/modules/realquantizer.py` | __init__, __init__, __init__ |
| `quark/torch/quantization/observer/tqt_observer.py` | __init__, forward, _KL_J |
| `test/test_for_torch/test_mx.py` | test_per_block_simple_scale, test_per_block_scale_tiled |
| `quark/torch/quantization/observer/lsq_observer.py` | __init__ |
| `quark/torch/quantization/config/type.py` | from_str |
| `quark/torch/utils/pack.py` | create_pack_method |
| `quark/shares/data_type.py` | BaseObserverBase |

## Entry Points

Start here when exploring this area:

- **`calculate_qmin_qmax`** (Function) — `quark/torch/quantization/utils.py:32`
- **`get_num_bits`** (Function) — `quark/torch/quantization/utils.py:68`
- **`get_dtype_params`** (Function) — `quark/torch/quantization/utils.py:99`
- **`even_round`** (Function) — `quark/torch/quantization/utils.py:204`
- **`create_pack_method`** (Function) — `quark/torch/utils/pack.py:669`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `UniformScalingObserver` | Class | `quark/torch/quantization/observer/observer.py` | 127 |
| `PerTensorMinMaxObserver` | Class | `quark/torch/quantization/observer/observer.py` | 290 |
| `PerTensorPowOf2MinMaxObserver` | Class | `quark/torch/quantization/observer/observer.py` | 314 |
| `PerChannelMinMaxObserver` | Class | `quark/torch/quantization/observer/observer.py` | 465 |
| `PerChannelPowOf2MinMaxObserver` | Class | `quark/torch/quantization/observer/observer.py` | 531 |
| `PerTensorHistogramObserver` | Class | `quark/torch/quantization/observer/observer.py` | 976 |
| `BaseObserverBase` | Class | `quark/shares/data_type.py` | 30 |
| `ObserverBase` | Class | `quark/torch/quantization/observer/observer.py` | 36 |
| `PerBlockMXObserver` | Class | `quark/torch/quantization/observer/observer.py` | 690 |
| `calculate_qmin_qmax` | Function | `quark/torch/quantization/utils.py` | 32 |
| `get_num_bits` | Function | `quark/torch/quantization/utils.py` | 68 |
| `get_dtype_params` | Function | `quark/torch/quantization/utils.py` | 99 |
| `even_round` | Function | `quark/torch/quantization/utils.py` | 204 |
| `create_pack_method` | Function | `quark/torch/utils/pack.py` | 669 |
| `test_per_block_simple_scale` | Function | `test/test_for_torch/test_mx.py` | 244 |
| `test_per_block_scale_tiled` | Function | `test/test_for_torch/test_mx.py` | 267 |
| `from_str` | Method | `quark/torch/quantization/config/type.py` | 272 |
| `calculate_fp4_quant_parameters` | Method | `quark/torch/quantization/observer/observer.py` | 223 |
| `calculate_qparams` | Method | `quark/torch/quantization/observer/observer.py` | 722 |
| `calculate_qparams` | Method | `quark/torch/quantization/observer/observer.py` | 161 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Nn | 5 calls |
| Modules | 2 calls |
| Hw_emulation | 1 calls |

## How to Explore

1. `gitnexus_context({name: "calculate_qmin_qmax"})` — see callers and callees
2. `gitnexus_query({query: "observer"})` — find related execution flows
3. Read key files listed above for implementation details
