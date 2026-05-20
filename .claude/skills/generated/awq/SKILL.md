---
name: awq
description: "Skill for the Awq area of Quark. 54 symbols across 21 files."
---

# Awq

54 symbols | 21 files | Cohesion: 59%

## When to Use

- Working with code in `quark/`
- Understanding how block_forward, get_named_linears, get_device work
- Modifying awq-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `quark/torch/algorithm/awq/awq.py` | init_quant, apply, __init__, _search_best_clip, _compute_best_clip (+5) |
| `quark/torch/algorithm/awq/auto_smooth.py` | init_quant, apply, _search_best_scale, _compute_best_scale, pseudo_quantize_tensor (+1) |
| `quark/torch/algorithm/utils/module.py` | get_named_linears, get_device, move_to_device, get_named_quant_linears, get_moe_layers (+1) |
| `quark/torch/algorithm/awq/scale.py` | apply_clip, scale_ln_fcs, scale_gelu_fc, apply_scale, scale_fc_fc |
| `quark/torch/algorithm/awq/smooth.py` | apply, _get_act_scale_and_input_feat, init_quant, __init__ |
| `quark/torch/algorithm/utils/utils.py` | clear_memory, is_attention_module, get_num_attn_heads_from_model |
| `quark/torch/algorithm/osscar/osscar.py` | add_batch, apply |
| `quark/torch/algorithm/utils/prepare.py` | cache_model_inps, reset_model_kv_cache |
| `quark/torch/quantization/api.py` | _do_calibration, _calibrate_all_params |
| `quark/torch/utils/accelerate_helper.py` | offload_to_weights_map, update_offload_parameter |

## Entry Points

Start here when exploring this area:

- **`block_forward`** (Function) — `quark/torch/algorithm/blockwise_tuning/blockwise_utils.py:55`
- **`get_named_linears`** (Function) — `quark/torch/algorithm/utils/module.py:14`
- **`get_device`** (Function) — `quark/torch/algorithm/utils/module.py:46`
- **`move_to_device`** (Function) — `quark/torch/algorithm/utils/module.py:67`
- **`cache_model_inps`** (Function) — `quark/torch/algorithm/utils/prepare.py:23`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `block_forward` | Function | `quark/torch/algorithm/blockwise_tuning/blockwise_utils.py` | 55 |
| `get_named_linears` | Function | `quark/torch/algorithm/utils/module.py` | 14 |
| `get_device` | Function | `quark/torch/algorithm/utils/module.py` | 46 |
| `move_to_device` | Function | `quark/torch/algorithm/utils/module.py` | 67 |
| `cache_model_inps` | Function | `quark/torch/algorithm/utils/prepare.py` | 23 |
| `reset_model_kv_cache` | Function | `quark/torch/algorithm/utils/prepare.py` | 236 |
| `clear_memory` | Function | `quark/torch/algorithm/utils/utils.py` | 28 |
| `is_accelerate_available` | Function | `quark/shares/utils/import_utils.py` | 106 |
| `apply_clip` | Function | `quark/torch/algorithm/awq/scale.py` | 30 |
| `scale_ln_fcs` | Function | `quark/torch/algorithm/awq/scale.py` | 116 |
| `scale_gelu_fc` | Function | `quark/torch/algorithm/awq/scale.py` | 216 |
| `offload_to_weights_map` | Function | `quark/torch/utils/accelerate_helper.py` | 63 |
| `update_offload_parameter` | Function | `quark/torch/utils/accelerate_helper.py` | 105 |
| `test_grok` | Function | `test/test_for_torch/test_grok.py` | 13 |
| `get_named_quant_linears` | Function | `quark/torch/algorithm/utils/module.py` | 18 |
| `get_moe_layers` | Function | `quark/torch/algorithm/utils/module.py` | 24 |
| `append_str_prefix` | Function | `quark/torch/algorithm/utils/module.py` | 35 |
| `align_attention_mask_with_input` | Function | `quark/torch/algorithm/awq/utils.py` | 12 |
| `apply_scale` | Function | `quark/torch/algorithm/awq/scale.py` | 46 |
| `scale_fc_fc` | Function | `quark/torch/algorithm/awq/scale.py` | 150 |

## Execution Flows

| Flow | Type | Steps |
|------|------|-------|
| `Apply → Create_hook` | cross_community | 5 |
| `Apply → Is_ocp_mxfp4` | cross_community | 5 |
| `Apply → _compute_loss` | cross_community | 4 |
| `Apply → Is_attention_module` | cross_community | 4 |
| `Apply → Align_attention_mask_with_input` | cross_community | 4 |
| `Apply → Pseudo_quantize_tensor` | cross_community | 4 |
| `Apply → Clear_memory` | cross_community | 4 |
| `Apply → Align_attention_mask_with_input` | cross_community | 4 |
| `Apply → Get_device` | intra_community | 4 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Optimizations | 21 calls |
| Depth_pruning | 6 calls |
| Passes | 4 calls |
| Get_ | 4 calls |
| Blockwise_tuning | 2 calls |
| Gguf_export | 1 calls |

## How to Explore

1. `gitnexus_context({name: "block_forward"})` — see callers and callees
2. `gitnexus_query({query: "awq"})` — find related execution flows
3. Read key files listed above for implementation details
