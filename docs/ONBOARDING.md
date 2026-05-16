# AMD Quark 新人入职指南

## 项目概览

| 属性 | 值 |
|---|---|
| **名称** | AMD Quark (v0.11.1) |
| **语言** | Python, C++, CUDA, CMake, Protobuf |
| **框架** | PyTorch, ONNX, ONNX Runtime, Triton, Transformers, lm-eval-harness |
| **描述** | AMD Quark 是一款全面的跨平台深度学习模型量化工具包。支持 PyTorch 和 ONNX 后端，提供静态/动态量化、多种校准方法、高级 PTQ 算法（AWQ、GPTQ、SmoothQuant、QuaRot、Rotation），以及模型剪枝功能。可部署至多种硬件后端（AMD GPU、Ryzen AI NPU、ONNX Runtime）。支持 LLM 量化、扩散模型量化、CV 模型量化等场景，提供 GGUF、Safetensors、ONNX 等多种导出格式。 |
| **仓库** | https://github.com/amd/quark |
| **文档** | https://quark.docs.amd.com |
| **许可证** | MIT |
| **Python 要求** | >= 3.10, < 3.13 |

---

## 架构层次

Quark 采用分层架构，从底层共享基础到上层应用共 12 层：

### 1. 共享基础设施层
**代码位置**：`quark/shares/`

定义跨后端共享的抽象基类型、配置基类和通用工具。这是理解整个代码库的**第一站**。

| 文件 | 用途 |
|---|---|
| `quark/shares/data_type.py` | 30+ 种量化数据类型定义（Int4 ~ FP8, MX, BFP） |
| `quark/shares/config.py` | 三层配置基类（BaseQConfig / BaseQLayerConfig / BaseQTensorConfig） |
| `quark/shares/utils/log.py` | ScreenLogger 日志系统，支持 ANSI 颜色输出和去重过滤 |
| `quark/shares/utils/import_utils.py` | 第三方包可用性检测（torch/transformers/vllm 等） |

### 2. PyTorch 量化后端
**代码位置**：`quark/torch/quantization/`

PyTorch 后端的**核心**，所有量化请求的入口都在这里。

| 文件 | 用途 | 复杂度 |
|---|---|---|
| `quark/torch/quantization/api.py` | `ModelQuantizer` — 量化流水线主入口（eager/FX模式） | 🔴 高 |
| `quark/torch/quantization/config/config.py` | QConfig → QLayerConfig → QTensorConfig 三层配置体系 | 🔴 高 |
| `quark/torch/quantization/config/type.py` | 量化数据类型枚举（Dtype）、模式（QuantizationMode） | 🟡 中 |
| `quark/torch/quantization/config/template.py` | LLMTemplate — 30+ 预注册 LLM 模型量化模板 | 🔴 高 |
| `quark/torch/quantization/tensor_quantize.py` | 伪量化模块（Scaled/Static/Dynamic/NonScaled/Frozen/Sequential） | 🔴 高 |
| `quark/torch/quantization/model_transformation.py` | 模型算子替换（nn.Linear → QuantLinear 等） | 🟡 中 |

### 3. PyTorch 高级量化算法
**代码位置**：`quark/torch/algorithm/`

PTQ 增强算法，由统一注册表 PROCESSOR_MAP 驱动，按序执行。

| 模块 | 算法 | 复杂度 |
|---|---|---|
| `quark/torch/algorithm/awq/` | AWQ — 激活感知权重量化（网格搜索最优缩放/裁剪） | 🔴 高 |
| `quark/torch/algorithm/gptq/` | GPTQ — 基于 Hessian 的逐列权重量化（Cholesky 分解） | 🔴 高 |
| `quark/torch/algorithm/rotation/` | Rotation — Hadamard 正交旋转优化（R1-R4 四层，在线/离线双模式） | 🔴 极高 |
| `quark/torch/algorithm/api.py` | 算法调度 API（PROCESSOR_MAP 注册 + 自动配置生成） | 🟡 中 |

### 4. PyTorch 模型导出
**代码位置**：`quark/torch/export/api.py`

| 导出格式 | 用途 |
|---|---|
| ONNX | 标准 ONNX 导出（含 uint4/int4 转换） |
| GGUF | LLM 量化格式（Q4_1 等） |
| JSON-Safetensors | Quark 原生格式（配置+权重分离） |

### 5. PyTorch 量化内核
**代码位置**：`quark/torch/kernel/`

自定义 CUDA autograd Function 实现的量化/反量化底层算子。支持 FP8 (E4M3/E5M2)、MX 格式、LSQ、TQT 可学习量化器、torch.compile 加速和 DTensor 分片。

### 6. ONNX 量化后端
**代码位置**：`quark/onnx/quantization/`

| 文件 | 用途 | 复杂度 |
|---|---|---|
| `quark/onnx/quantization/api.py` | `ModelQuantizer` — ONNX 量化入口（静态/动态分派） | 🔴 高 |
| `quark/onnx/quantization/quantize.py` | `quantize_static()` / `quantize_dynamic()` — 完整量化流水线 | 🔴 极高 |
| `quark/onnx/quantization/config/config.py` | Config/QConfig — 分层配置 + 旧 API 兼容 | 🟡 中 |
| `quark/onnx/calibration/` | 校准子包：Cached/Path/Random 数据读取器，Int16/PowerOfTwo/LayerWise 校准方法 | 🟢 低 |
| `quark/onnx/quantizers/` | 量化器子包：ONNXQuantizer/QDQ/BFP/MatMulNbits/NPU | 🟢 低 |

### 7. ONNX 高级量化算法
**代码位置**：`quark/onnx/algorithm/`

SmoothQuant / CLE（跨层均衡）/ QuaRot / GPTQ / BiasCorrection / AdaRound / AdaQuant / AutoMixPrecision / FastFinetune。通过统一 `apply_*` 接口执行。

### 8. ONNX 图优化
**代码位置**：`quark/onnx/optimizations/`

模型 Transformer、转换流水线、ONNX Runtime 优化、ONNX Slim 简化。

### 9. 自动精度搜索
**代码位置**：`quark/onnx/quantization/auto_search/`

AutoSearch / AutoSearchPro 在配置空间中自动搜索最优量化组合。

### 10. ONNX 适配器
**代码位置**：`quark/onnx_adapter/`

24 种图变换 Pass（BN 折叠、算子融合、形状固定、算子集版本转换、布局转换等），基于 Pass/Engine 架构。

### 11. CLI 命令行接口
**代码位置**：`quark/experimental/cli/main.py`

`quark-cli` 命令，8 个子命令：
- `onnx-ptq` — ONNX 后训练量化
- `onnx-autosearch` — 自动精度搜索
- `export-onnx` / `export-oga` — 导出 ONNX 模型
- `onnx-validate` — 精度验证
- `onnx-prepare-data` — 数据准备
- `torch-llm-ptq` — PyTorch LLM 量化
- `onnx-adapter` — ONNX 图适配

### 12. 贡献模块
**代码位置**：`quark/contrib/`

| 模块 | 用途 |
|---|---|
| `quark/contrib/llm_eval/` | LLM 评估（perplexity、lm-eval-harness、ROUGE、MLPerf） |
| `quark/contrib/onnx_utils/` | Ryzen AI 硬件工具（自定义 ONNX 算子、140+ 图变换 Pass） |

---

## 关键概念

### 量化流水线

```
配置解析 → 模型准备 → 算法应用（预量化优化）→ 校准 → 量化（插入 FakeQuant）→ 后处理 → 冻结导出
```

1. **配置解析**：用户通过 `QConfig → QLayerConfig → QTensorConfig` 三层体系指定量化目标
2. **模型准备**：将原始算子替换为量化算子（`nn.Linear → QuantLinear`）
3. **算法应用**：AWQ / GPTQ / Rotation / SmoothQuant 等预量化优化
4. **校准**：运行校准数据收集激活分布统计量（scale / zero_point）
5. **量化**：插入伪量化模块（FakeQuantize），模拟低精度推理效果
6. **后处理**：BiasCorrection / AdaRound 等精度恢复
7. **冻结导出**：固化量化参数，导出为 ONNX / GGUF / Safetensors

### 双后端对称设计

Quark 的 PyTorch 和 ONNX 后端遵循几乎相同的架构模式：

| 概念 | PyTorch 后端 | ONNX 后端 |
|---|---|---|
| 入口 | `quark.torch.quantization.api.ModelQuantizer` | `quark.onnx.quantization.api.ModelQuantizer` |
| 配置 | `QConfig → QLayerConfig → QTensorConfig` | `QConfig → global/layer_type/specific_layer` |
| 模式 | eager / FX graph | 静态（需校准）/ 动态（无需校准） |
| 校准 | Observer 模式（PerTensor/PerChannel/PerGroup） | 数据读取器 + 校准方法（MinMax/Percentile/MSE/Entropy） |
| 算法 | AWQ / GPTQ / Rotation / GPTAQ / Qronos | SmoothQuant / CLE / QuaRot / GPTQ / AdaRound |

### 配置优先级

```
逐层配置（layer_quant_config） > 按类型配置（layer_type_quant_config） > 全局配置（global_quant_config）
```

### 支持的量化数据类型

- **整数**：int2/3/4/8/16/32, uint4/8/16/32
- **浮点**：float16, bfloat16, fp8_e4m3, fp8_e5m2, fp6, fp4
- **MX 格式**：MXFP4 (E2M1), MXFP6 (E3M2/E2M3), MXFP8 (E5M2/E4M3), MXInt8
- **BFP**：bfp16

---

## 导览路径

按以下顺序学习代码库，由浅入深：

### 第 1 步：项目概览与入口
- 阅读 `README.md`、`pyproject.toml`
- 浏览 `quark/__init__.py`、`quark/torch/__init__.py`、`quark/onnx/__init__.py`
- **目标**：理解双后端架构的顶层接口

### 第 2 步：共享基础类型
- 深入 `quark/shares/data_type.py` — 30+ 种量化数据类型定义
- 阅读 `quark/shares/config.py` — 三层配置基类的抽象设计
- **目标**：理解 PyTorch 和 ONNX 后端的共同抽象

### 第 3 步：PyTorch 量化核心流水线
- 从 `quark/torch/quantization/api.py` 的 `ModelQuantizer` 类入口，跟踪完整流水线
- 理解三层配置体系：`QConfig → QLayerConfig → QTensorConfig`
- 学习模型转换：`model_transformation.py` 的算子替换逻辑
- 掌握伪量化模块：`tensor_quantize.py` 的 Scaled/Static/Dynamic/NonScaled 体系
- **目标**：能独立完成一个 PyTorch 模型的量化

### 第 4 步：LLM 量化配置模板
- 阅读 `quark/torch/quantization/config/template.py`
- 理解 `LLMTemplate`、`QuantizationSchemeCollection` 和 30+ 预注册模型
- **目标**：理解如何为 LLaMA/Qwen/DeepSeek 等 LLM 一行代码完成量化配置

### 第 5 步：高级量化算法
- PyTorch 端：跟踪 `quark/torch/algorithm/api.py` 的 `PROCESSOR_MAP` 注册机制
- 学习 AWQ（激活感知）→ GPTQ（Hessian 最优）→ Rotation（正交变换）的算法原理
- ONNX 端：浏览 `quark/onnx/algorithm/` 了解 SmoothQuant / CLE / QuaRot 等
- **目标**：理解预量化优化如何提升精度

### 第 6 步：ONNX 量化流水线
- 从 `quark/onnx/quantization/api.py` 的 `ModelQuantizer.quantize_model()` 入口
- 跟踪 `quantize_static()` 完整流水：模型加载 → 预处理 → 校准 → 量化器创建 → QDQ 插入 → 后处理
- **目标**：理解 ONNX 量化与 PyTorch 量化的差异

### 第 7 步：量化内核与硬件仿真
- 深入 `quark/torch/kernel/__init__.py` — 自定义 autograd Function 实现
- 理解 FP8 / MX 格式的量化/反量化逻辑
- 学习硬件仿真层 `hw_emulation/` 的验证机制
- **目标**：掌握底层量化算子的实现原理

### 第 8 步：模型导出与部署
- 阅读 `quark/torch/export/api.py`
- 理解 Safetensors / ONNX / GGUF 三种导出格式的差异和适用场景
- **目标**：能正确导出量化模型到目标部署平台

### 第 9 步：CLI 与自动化
- 阅读 `quark/experimental/cli/main.py` — 8 个子命令的注册机制
- 结合 `quark/onnx/quantization/auto_search/` 理解自动精度搜索
- **目标**：能通过 CLI 自动化量化工作流

### 第 10 步：测试与评估
- 浏览 `test/` 目录了解 ~190+ 测试用例的组织方式
- 学习 `quark/contrib/llm_eval/evaluation.py` 的 LLM 评估集成
- **目标**：能运行测试并评估量化模型的精度

---

## 文件地图

按架构层次组织的关键文件：

```
quark/
├── shares/                          # 共享基础设施
│   ├── config.py                    #   基类配置
│   ├── data_type.py                 #   数据类型体系
│   └── utils/
│       ├── log.py                   #   日志系统
│       └── import_utils.py          #   包检测
│
├── torch/                           # PyTorch 后端
│   ├── quantization/
│   │   ├── api.py                   #   ModelQuantizer 入口
│   │   ├── config/
│   │   │   ├── config.py            #   三层配置 + DataTypeSpec 工厂
│   │   │   ├── type.py              #   类型枚举
│   │   │   └── template.py          #   LLM 模板
│   │   ├── tensor_quantize.py       #   伪量化模块（6 个类）
│   │   ├── model_transformation.py  #   算子替换
│   │   └── utils.py                 #   辅助函数
│   ├── algorithm/
│   │   ├── api.py                   #   算法调度 API
│   │   ├── awq/                     #   AWQ 算法
│   │   ├── gptq/                    #   GPTQ 算法
│   │   └── rotation/                #   Rotation 算法
│   ├── export/
│   │   └── api.py                   #   导出入口（ONNX/GGUF/Safetensors）
│   ├── pruning/
│   │   └── api.py                   #   模型剪枝
│   └── kernel/
│       └── __init__.py              #   自定义量化内核
│
├── onnx/                            # ONNX 后端
│   ├── quantization/
│   │   ├── api.py                   #   ModelQuantizer 入口
│   │   ├── quantize.py              #   quantize_static/dynamic 核心
│   │   ├── config/
│   │   │   ├── config.py            #   分层配置
│   │   │   ├── data_type.py         #   数据类型映射
│   │   │   └── algorithm.py         #   算法配置
│   │   └── auto_search/             #   自动精度搜索
│   ├── calibration/                 #   校准系统
│   ├── quantizers/                  #   量化器
│   ├── algorithm/                   #   高级算法（SmoothQuant/CLE/GPTQ/...）
│   └── optimizations/               #   图优化
│
├── onnx_adapter/                    # ONNX 适配器（24 种图 Pass）
│
├── experimental/cli/main.py         # CLI 入口（8 个子命令）
│
└── contrib/
    ├── llm_eval/evaluation.py       #   LLM 评估
    └── onnx_utils/                  #   Ryzen AI 工具
```

---

## 复杂度热点

以下模块复杂度较高，建议在有经验后深入学习：

| 文件 | 复杂度 | 原因 |
|---|---|---|
| `quark/onnx/quantization/quantize.py` | 🔴 极高 | ONNX 完整量化流水线，涵盖模型加载→预处理→校准→量化→后处理全流程，处理大量配置分支和加密/大模型特殊路径 |
| `quark/torch/algorithm/rotation/` | 🔴 极高 | 四层 Hadamard 正交旋转（R1-R4），在线/离线双模式，可训练平滑量化，RMSNorm 融合，Kronecker 积变换 |
| `quark/torch/algorithm/gptq/` | 🔴 高 | Hessian 矩阵 Cholesky 分解，CUDA Graph 录制/回放，激活顺序排序，分块量化 |
| `quark/torch/export/api.py` | 🔴 高 | 多种导出格式（Safetensors/ONNX/GGUF），配置解析与重建，多设备加载 |
| `quark/torch/kernel/__init__.py` | 🔴 高 | 多种自定义 autograd Function，ONNX 符号化导出，DTensor 分片，torch.compile 优化 |
| `quark/contrib/llm_eval/evaluation.py` | 🔴 高 | 多种评估指标（PPL/KV-Cache PPL/ROUGE/MLPerf），ONNX GenAI 支持，多模型兼容 |
| `quark/torch/algorithm/awq/` | 🔴 高 | 网格搜索最优缩放/裁剪，前/后钩子机制，MoE 支持 |

---

## 建议下一步

1. **运行测试**：`cd test && bash run_all_unit_tests.sh`（或选择单个测试文件调试）
2. **运行示例**：`examples/torch/vision/quantize.py` 是一个简单的 CV 模型量化起点
3. **阅读文档**：https://quark.docs.amd.com 获取完整 API 参考
4. **提交本文件**：`git add docs/ONBOARDING.md && git commit -m "docs: add onboarding guide for new developers"`
