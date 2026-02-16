# Doc Agent

一个基于 LangChain DeepAgents 的智能文档助手，支持多种大语言模型提供商，具备长期记忆和文件管理功能。

## 功能特性

- 多模型支持：支持 SiliconFlow、智谱 GLM、NVIDIA 等多种模型提供商
- 长期记忆：使用文件系统存储用户偏好和历史信息
- 文件管理：内置文件系统工具，支持读写、编辑等操作
- 任务规划：自动分解复杂任务
- 子智能体：支持委派任务给专门的子智能体
- LangSmith 监控：集成 LangSmith 进行性能监控和调试

## 安装

1. 克隆项目
```bash
git clone https://github.com/PengZiqiao/doc-agent.git
cd doc_agent
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

## 配置

### 1. 环境变量配置

复制 `.env` 文件并配置必要的 API keys：

```bash
cp .env.example .env
```

编辑 `.env` 文件：

```env
# 选择使用的模型提供商 (siliconflow | zhipu | nvidia)
PROVIDER=siliconflow

# API Keys
SILICONFLOW_API_KEY=your_siliconflow_api_key
ZHIPU_API_KEY=your_zhipu_api_key
NVIDIA_API_KEY=your_nvidia_api_key

# LangSmith 配置（可选）
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=doc-agent
```

### 2. 模型配置

在 `agent.py` 中选择使用的模型提供商：

```python
provider = "siliconflow"  # 可选: siliconflow | zhipu | nvidia
```

### 3. 系统提示词

编辑 `system_prompt.yaml` 自定义系统提示词：

```yaml
你是一个有帮助的AI助手，可以回答各种问题。

你可以使用内置的工具来帮助你完成任务，包括：
- 规划任务
- 管理文件系统
- 委派子任务给专门的子智能体
```

## 使用方法

### 启动 Agent

```bash
python agent.py
```

### 交互示例

```
你: 你好，我是张三
助手: 你好张三！很高兴认识你。

你: 我喜欢用 Python 编程
助手: 好的，我已经记住了你喜欢用 Python 编程。

你: 记住我的名字
助手: 已将你的信息保存到长期记忆中。
```

## 项目结构

```
doc_agent/
├── agent.py              # 主程序
├── config.yaml           # 模型配置
├── system_prompt.yaml   # 系统提示词模板
├── requirements.txt      # Python 依赖
├── README.md            # 项目文档
├── .gitignore           # Git 忽略文件
├── .env.example         # 环境变量示例
├── .env                 # 环境变量（不提交到 Git）
├── files/               # 默认文件存储
└── memories/            # 长期记忆存储
```

## 支持的模型提供商

| 提供商 | 模型 | 说明 |
|--------|------|------|
| SiliconFlow | Qwen/Qwen2.5-7B-Instruct | 通义千问 2.5 |
| 智谱 GLM | glm-4-flash | 智谱 GLM-4 Flash |
| NVIDIA | meta/llama-3.1-405b-instruct | Llama 3.1 |

## 技术栈

- LangChain - LLM 应用框架
- DeepAgents - LangChain 智能体库
- LangGraph - 工作流编排
- PyYAML - YAML 配置解析
- python-dotenv - 环境变量管理

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！
