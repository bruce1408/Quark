# AMD Quark 新成员入职指南

> 自动生成自知识图谱 — 最后更新: 2026-05-19

---

## 1. 项目概览

| 属性 | 值 |
|------|-----|
| **项目名称** | AMD Quark |
| **语言** | Python, C++, CUDA, CMake, Protocol Buffers |
| **框架** | PyTorch, ONNX Runtime, Transformers |
| **定位** | 跨平台深度学习模型量化工具包 |

**核心能力**: 支持 PyTorch 和 ONNX 双后端，提供静态/动态量化、多种校准方法、高级 PTQ 算法（AWQ、GPTQ、SmoothQuant、QuaRot、Rotation），以及模型剪枝功能。可部署至多种硬件后端（AMD GPU、Ryzen AI NPU、ONNX Runtime）。支持 LLM 量化、扩散模型量化、CV 模型量化等场景，提供 GGUF、Safetensors、ONNX 等多种导出格式。

---

## 2. 架构分层

AMD Quark 采用 **8 层** 分层架构，从底层共享基础设施到顶层 CLI 工具逐步构建：

### 2.1 共享基础设施层 (`layer_shared`)
跨后端共享的抽象基类型、配置基类、通用工具函数与项目整体架构文档。

| 模块 | 文件路径 | 复杂度 | 职责 |
|------|----------|--------|------|
| `quark` | `quark/__init__.py` | simple | 顶层包入口，版本号获取与公共 API 定义 |
| `quark.shares.config` | `quark/shares/config.py` | moderate | `BaseQConfig` → `BaseQLayerConfig` → `BaseQTensorConfig` 三层抽象配置体系 |
| `quark.shares.data_type` | `quark/shares/data_type.py` | moderate | 30+ 量化数据类型定义（Int4-FP8）+ MX 特殊格式 |
| `quark.shares.utils.import_utils` | `quark/shares/utils/import_utils.py` | moderate | 第三方包可用性检测与版本管理（惰性导入） |
| `quark.shares.utils.log` | `quark/shares/utils/log.py` | moderate | 带 ANSI 颜色、去重过滤的自定义日志系统 |

### 2.2 PyTorch 量化后端 (`layer_torch_backend`)
PyTorch 后端的量化入口 API，统一导出 ModelQuantizer、ModelPruner、export 系列工具以及 LLMTemplate。

| 模块 | 文件路径 | 复杂度 | 职责 |
|------|----------|--------|------|
| `quark.torch` | `quark/torch/__init__.py` | moderate | 桶文件模式汇总所有公开 API（量化/剪枝/导出/LLM 模板） |

### 2.3 PyTorch 高级量化算法与工具 (`layer_torch_algorithms`)
实现 AWQ、GPTQ、Rotation 等高级 PTQ 优化算法、模型剪枝 (OSSCAR/Blockwise)、多格式模型导出以及自定义 autograd 量化内核。

| 模块 | 文件路径 | 复杂度 | 职责 |
|------|----------|--------|------|
| Algorithm API | `quark/torch/algorithm/api.py` | **complex** | PROCESSOR_MAP 注册表驱动的算法调度入口 |
| AWQ Module | `quark/torch/algorithm/awq/__init__.py` | **complex** | 激活感知权重量化（逐通道缩放因子搜索） |
| GPTQ Module | `quark/torch/algorithm/gptq/__init__.py` | **complex** | 基于 Hessian + Cholesky 分解的逐列权重量化 |
| Rotation Module | `quark/torch/algorithm/rotation/__init__.py` | **complex** | Hadamard 正交旋转（R1-R4）优化权重分布 |
| Kernel Init | `quark/torch/kernel/__init__.py` | **complex** | 自定义 autograd.Function 量化内核（FP8/MX/LSQ/TQT） |
| Export API | `quark/torch/export/api.py` | **complex** | Safetensors/ONNX/GGUF 多格式导出 |
| Pruning API | `quark/torch/pruning/api.py` | moderate | 剪枝流水线（预处理→剪枝→后处理→Blockwise 调优） |
| `kernel.hw_emulation` | `quark/torch/kernel/hw_emulation/__init__.py` | moderate | 硬件行为仿真 |

### 2.4 ONNX 量化后端 (`layer_onnx_backend`)
ONNX 后端的完整量化实现，包括入口 API、校准系统、量化器工厂、自动精度搜索和分层算法配置。

| 模块 | 文件路径 | 复杂度 | 职责 |
|------|----------|--------|------|
| `quark.onnx` | `quark/onnx/__init__.py` | **complex** | ONNX 后端桶文件入口，与 PyTorch 后端对称设计 |
| `quantize_static/dynamic` | `quark/onnx/quantization/quantize.py` | **complex** | 静态/动态量化的完整执行流水线 |
| `quark.onnx.calibration` | `quark/onnx/calibration/__init__.py` | moderate | 多方法数据读取器 + 校准策略 |
| `quark.onnx.quantizers` | `quark/onnx/quantizers/__init__.py` | moderate | 量化器工厂（static/dynamic/matmul_nbits） |
| `quark.onnx.quantization.auto_search` | `quark/onnx/quantization/auto_search/__init__.py` | moderate | AutoSearch/AutoSearchPro 自动精度搜索 |
| `quark.onnx.quantization.config.algorithm` | `quark/onnx/quantization/config/algorithm.py` | moderate | 算法参数调优接口 |

### 2.5 ONNX 高级算法与优化 (`layer_onnx_algorithms`)
ONNX 后端的高级 PTQ 算法集合以及图优化与模型转换流水线。

| 模块 | 文件路径 | 复杂度 | 职责 |
|------|----------|--------|------|
| `quark.onnx.algorithm` | `quark/onnx/algorithm/__init__.py` | moderate | 8 种 PTQ 算法（SmoothQuant/CLE/QuaRot/GPTQ/BiasCorrection/AdaRound/AdaQuant/AutoMixPrecision） |
| `quark.onnx.optimizations` | `quark/onnx/optimizations/__init__.py` | **complex** | ORT/ONNX Slim 图优化与模型转换 |

### 2.6 ONNX 适配器 (`layer_onnx_adapter`)
基于 Pass/Engine 架构的 24 种图变换 Pass 通道系统。

| 模块 | 文件路径 | 复杂度 | 职责 |
|------|----------|--------|------|
| `quark.onnx_adapter` | `quark/onnx_adapter/__init__.py` | **complex** | BN 折叠/算子融合/形状固定/布局转换 + Pass 管线 |

### 2.7 CLI 命令行接口 (`layer_cli`)
统一的命令行工具入口，基于 argparse 子命令架构。

| 模块 | 文件路径 | 复杂度 | 职责 |
|------|----------|--------|------|
| CLI Main | `quark/experimental/cli/main.py` | moderate | 8 个子命令注册（onnx-ptq/autosearch/export/validate/adapter/torch-llm-ptq 等） |

### 2.8 贡献模块 (`layer_contrib`)
社区贡献的扩展工具集。

| 模块 | 文件路径 | 复杂度 | 职责 |
|------|----------|--------|------|
| LLMEval | `quark/contrib/llm_eval/evaluation.py` | **complex** | LLM 评估（perplexity/KV-Cache/lm-eval/ROUGE/MLPerf） |
| ONNXUtils | `quark/contrib/onnx_utils/__init__.py` | moderate | Ryzen AI 自定义 ONNX 算子 + 140+ 图变换 Pass |

---

## 3. 关键设计模式与概念

### 3.1 双后端对称架构
PyTorch 和 ONNX 两个量化后端共享 `quark.shares` 中的配置基类和数据类型体系，使得跨后端的量化流程保持一致的用户体验和配置风格。这降低了学习成本和维护负担。

### 3.2 三层量化配置体系
`BaseQConfig` → `BaseQLayerConfig` → `BaseQTensorConfig` 构成组合模式（Composition），而非扁平配置。每一层可以独立演化而不破坏上层接口。

### 3.3 注册表模式（Registry Pattern）
`PROCESSOR_MAP` 字典将字符串算法名映射到具体处理器类，实现插件式的可扩展调度。新增算法只需注册到字典而无须修改调度逻辑，符合开闭原则（OCP）。

### 3.4 Pass/Engine 图优化架构
在 ONNX 适配器中，每个 Pass 对图执行一次单向变换（如 BN 折叠、算子融合），多个 Pass 可组合为优化管线。这与 LLVM 的 Pass Manager 设计一脉相承。

### 3.5 桶文件（Barrel File）模式
`__init__.py` 将子模块导入的类型统一汇集到扁平命名空间，对外呈现清晰的 API 表面而不暴露内部模块结构。

### 3.6 Q/DQ 量化插入模式
ONNX 量化在校准阶段收集激活值统计分布，随后在图中插入模拟量化的 QuantizeLinear/DequantizeLinear 算子对。静态量化使用预定参数，动态量化在推理时实时确定范围。

---

## 4. 代码导览路径

推荐按以下 **11 步** 渐进式了解代码库：

| 步骤 | 标题 | 核心内容 |
|------|------|----------|
| **1** | 项目全景与入门指南 | 阅读 `README.md` + `docs/ONBOARDING.md`，建立整体认知地图 |
| **2** | 包入口与项目配置 | `quark/__init__.py` 包入口 + `pyproject.toml` 依赖与构建配置 |
| **3** | 量化配置基类与数据类型体系 | `quark.shares.config` 三层配置抽象 + `quark.shares.data_type` 30+ 数据类型 |
| **4** | 共享工具模块 | `quark.shares.utils.import_utils` 惰性导入 + `quark.shares.utils.log` 统一日志 |
| **5** | PyTorch 后端入口 | `quark.torch/__init__.py` 桶文件模式与公共 API 组织 |
| **6** | PyTorch 高级量化算法 | Algorithm API 调度器 → AWQ / GPTQ / Rotation 三大算法 |
| **7** | 量化内核、导出与剪枝 | 自定义 autograd 内核 → Safetensors/ONNX/GGUF 导出 → 剪枝流水线 |
| **8** | ONNX 后端入口 | `quark.onnx/__init__.py` 对称设计与 API 汇集 |
| **9** | ONNX 量化核心流水线 | 校准（数据读取器+统计）→ 量化器工厂（Q/DQ 插入）→ 量化执行 |
| **10** | ONNX 高级算法与图优化 | 8 种 PTQ 算法 + ORT 图优化 + AutoSearch 精度搜索 + 24 种 Pass |
| **11** | CLI 命令行与贡献模块 | 8 个子命令 CLI 入口 + LLM 评估工具包 + Ryzen AI 扩展 |

---

## 5. 复杂度热点

以下模块/函数复杂度较高，新成员应优先理解其输入输出契约，再逐步深入实现细节：

| 热点 | 文件路径 | 类型 | 原因 |
|------|----------|------|------|
| **ONNX 入口** | `quark/onnx/__init__.py` | module | 大量子模块 API 汇集，与 PyTorch 后端对称设计 |
| **Algorithm API** | `quark/torch/algorithm/api.py` | module | 注册表驱动的算法调度核心，多算法路由 |
| **AWQ 模块** | `quark/torch/algorithm/awq/__init__.py` | module | 激活感知量化，涉及激活分布分析与缩放因子搜索 |
| **GPTQ 模块** | `quark/torch/algorithm/gptq/__init__.py` | module | Hessian + Cholesky 数学密集计算 |
| **Rotation 模块** | `quark/torch/algorithm/rotation/__init__.py` | module | Hadamard 正交旋转，R1-R4 四层优化 |
| **Kernel 初始化** | `quark/torch/kernel/__init__.py` | module | 自定义 autograd.Function，CUDA 内核集成 |
| **Export API** | `quark/torch/export/api.py` | module | 多格式导出协调（Safetensors/ONNX/GGUF） |
| **量化流水线** | `quark/onnx/quantization/quantize.py` | module | 完整静态/动态量化执行引擎 |
| **ONNX 优化** | `quark/onnx/optimizations/__init__.py` | module | ORT/Slim 图优化管线 |
| **ONNX 适配器** | `quark/onnx_adapter/__init__.py` | module | 24 种 Pass 的 Pass/Engine 架构 |
| **LLMEval** | `quark/contrib/llm_eval/evaluation.py` | module | 多评估指标集成（perplexity/KV-Cache/lm-eval） |
| `setup_config_per_layer` | `quark/torch/quantization/model_transformation.py` | function | 逐层配置设置，逻辑分支多 |
| `in_place_replace_layer` | `quark/torch/quantization/model_transformation.py` | function | 原地层替换，涉及模型图修改 |
| `even_round` | `quark/torch/quantization/utils.py` | function | 量化舍入策略，数值精度敏感 |

---

## 6. 学习路径建议

### 第一周：建立全局认知
1. 阅读 `README.md` 和 `docs/ONBOARDING.md`，理解项目定位和核心能力
2. 阅读 `pyproject.toml` 了解外部依赖
3. 通读 `quark.shares.config` 和 `quark.shares.data_type`，理解跨后端的类型基础

### 第二周：深入一个后端
4. 选择一个后端（建议从 PyTorch 开始，生态更熟悉），跟踪一个完整的量化流程
5. 阅读 `quark.torch` 入口 → Algorithm API → AWQ（最高频使用的算法）
6. 阅读 `quark.torch.kernel` 理解自定义量化算子

### 第三周：交叉学习 + 工具链
7. 切换到 ONNX 后端，对比相同概念（配置、校准、量化器）在 ONNX 中的实现
8. 阅读 `quark.onnx_adapter` 理解图优化 Pass 模式
9. 尝试 CLI 工具，运行一次完整的 onnx-ptq 流程

### 第四周：独立贡献
10. 选取一个复杂度 moderate 的模块，阅读全部代码并写出模块总结
11. 提交第一个 PR（建议从 CLI 子命令、工具函数或文档改进开始）

---

*本指南由 `/understand-onboard` 自动生成。建议随项目迭代定期更新。*
