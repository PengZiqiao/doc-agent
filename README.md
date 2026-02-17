# Doc Agent

一个基于 LangGraph 和 Deep Agents 的智能文档助手，支持联网搜索、微信公众号管理和稿件审核等功能。

## 功能特性

- 🌐 **联网搜索** - 使用 Tavily 进行实时信息检索
- 📝 **稿件审核** - 审核文章和文案的语言、内容和格式
- 📱 **微信公众号** - 创建、发布、删除草稿和素材
- 💾 **文件管理** - 在 files 目录下管理文档
- 🧠 **长期记忆** - 在 memories 目录下存储用户偏好

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置环境变量

复制 `.env` 文件并配置必要的 API keys：

```env
# 模型配置
ZHIPU_API_KEY=your-zhipu-api-key

# 搜索服务
TAVILY_API_KEY=your-tavily-api-key

# 微信公众号（可选）
WECHAT_APP_ID=your-wechat-app-id
WECHAT_APP_SECRET=your-wechat-app-secret

# LangChain 追踪（可选）
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your-langchain-api-key
LANGCHAIN_PROJECT=doc-agent
```

### 3. 一键启动所有服务

```bash
bash start_all.sh
```

这将启动：
- 微信公众号 MCP 服务器（端口 8000）
- LangGraph 后端服务（端口 2024）
- Deep Agents UI 前端（端口 3000）

### 4. 访问应用

- 前端界面：http://localhost:3000
- 后端 API：http://localhost:2024

### 5. 停止所有服务

```bash
bash stop_all.sh
```

## 项目结构

```
doc_agent/
├── agent.py              # 主程序，创建 deep agent
├── model.py             # 模型配置
├── tools.py             # 工具定义（搜索、MCP）
├── config.yaml          # 模型配置文件
├── system_prompt.yaml    # 系统提示词
├── skills/              # 技能目录
│   └── review-drafts/   # 稿件审核技能
├── files/               # 文档存储目录
├── memories/            # 记忆存储目录
├── logs/                # 日志目录
├── start_all.sh         # 一键启动脚本
├── stop_all.sh          # 一键停止脚本
└── deep-agents-ui/     # 前端项目
```

## 查看日志

```bash
# MCP 服务器日志
tail -f logs/mcp.log

# 后端服务日志
tail -f logs/backend.log

# 前端服务日志
tail -f logs/frontend.log
```

## 开发模式

后端使用 LangGraph 开发模式运行，支持热重载。修改代码后无需重启，自动生效。

## 获取 API Keys

- **智谱 AI**：https://open.bigmodel.cn/
- **Tavily 搜索**：https://tavily.com/（每月 1000 次免费搜索）
- **微信公众号**：https://mp.weixin.qq.com/
- **LangChain**：https://smith.langchain.com/
