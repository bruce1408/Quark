<!-- gitnexus:start -->
# GitNexus — Code Intelligence

This project is indexed by GitNexus as **Quark** (42436 symbols, 70873 relationships, 300 execution flows). Use the GitNexus MCP tools to understand code, assess impact, and navigate safely.

> If any GitNexus tool warns the index is stale, run `npx gitnexus analyze` in terminal first.

## Always Do

- **MUST run impact analysis before editing any symbol.** Before modifying a function, class, or method, run `gitnexus_impact({target: "symbolName", direction: "upstream"})` and report the blast radius (direct callers, affected processes, risk level) to the user.
- **MUST run `gitnexus_detect_changes()` before committing** to verify your changes only affect expected symbols and execution flows.
- **MUST warn the user** if impact analysis returns HIGH or CRITICAL risk before proceeding with edits.
- When exploring unfamiliar code, use `gitnexus_query({query: "concept"})` to find execution flows instead of grepping. It returns process-grouped results ranked by relevance.
- When you need full context on a specific symbol — callers, callees, which execution flows it participates in — use `gitnexus_context({name: "symbolName"})`.

## Never Do

- NEVER edit a function, class, or method without first running `gitnexus_impact` on it.
- NEVER ignore HIGH or CRITICAL risk warnings from impact analysis.
- NEVER rename symbols with find-and-replace — use `gitnexus_rename` which understands the call graph.
- NEVER commit changes without running `gitnexus_detect_changes()` to check affected scope.

## Resources

| Resource | Use for |
|----------|---------|
| `gitnexus://repo/Quark/context` | Codebase overview, check index freshness |
| `gitnexus://repo/Quark/clusters` | All functional areas |
| `gitnexus://repo/Quark/processes` | All execution flows |
| `gitnexus://repo/Quark/process/{name}` | Step-by-step execution trace |

## CLI

| Task | Read this skill file |
|------|---------------------|
| Understand architecture / "How does X work?" | `.claude/skills/gitnexus/gitnexus-exploring/SKILL.md` |
| Blast radius / "What breaks if I change X?" | `.claude/skills/gitnexus/gitnexus-impact-analysis/SKILL.md` |
| Trace bugs / "Why is X failing?" | `.claude/skills/gitnexus/gitnexus-debugging/SKILL.md` |
| Rename / extract / split / refactor | `.claude/skills/gitnexus/gitnexus-refactoring/SKILL.md` |
| Tools, resources, schema reference | `.claude/skills/gitnexus/gitnexus-guide/SKILL.md` |
| Index, status, clean, wiki CLI commands | `.claude/skills/gitnexus/gitnexus-cli/SKILL.md` |
| Work in the Test_for_onnx area (374 symbols) | `.claude/skills/generated/test-for-onnx/SKILL.md` |
| Work in the Passes area (249 symbols) | `.claude/skills/generated/passes/SKILL.md` |
| Work in the Test_for_torch area (222 symbols) | `.claude/skills/generated/test-for-torch/SKILL.md` |
| Work in the Sd3 area (138 symbols) | `.claude/skills/generated/sd3/SKILL.md` |
| Work in the Npu area (138 symbols) | `.claude/skills/generated/npu/SKILL.md` |
| Work in the Ryzenai_onnx_utils area (137 symbols) | `.claude/skills/generated/ryzenai-onnx-utils/SKILL.md` |
| Work in the Quantization area (111 symbols) | `.claude/skills/generated/quantization/SKILL.md` |
| Work in the Config area (83 symbols) | `.claude/skills/generated/config/SKILL.md` |
| Work in the Operators area (81 symbols) | `.claude/skills/generated/operators/SKILL.md` |
| Work in the Optimizations area (70 symbols) | `.claude/skills/generated/optimizations/SKILL.md` |
| Work in the Create_torch area (68 symbols) | `.claude/skills/generated/create-torch/SKILL.md` |
| Work in the Calibration area (59 symbols) | `.claude/skills/generated/calibration/SKILL.md` |
| Work in the Processor area (58 symbols) | `.claude/skills/generated/processor/SKILL.md` |
| Work in the Observer area (56 symbols) | `.claude/skills/generated/observer/SKILL.md` |
| Work in the Pre_quant area (55 symbols) | `.claude/skills/generated/pre-quant/SKILL.md` |
| Work in the Awq area (54 symbols) | `.claude/skills/generated/awq/SKILL.md` |
| Work in the Post_quant area (54 symbols) | `.claude/skills/generated/post-quant/SKILL.md` |
| Work in the Brevitas area (53 symbols) | `.claude/skills/generated/brevitas/SKILL.md` |
| Work in the Modules area (52 symbols) | `.claude/skills/generated/modules/SKILL.md` |
| Work in the Refinement area (50 symbols) | `.claude/skills/generated/refinement/SKILL.md` |

<!-- gitnexus:end -->
