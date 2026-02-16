import os
import uuid
import yaml
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import load_prompt
from deepagents import create_deep_agent
from deepagents.backends import FilesystemBackend, CompositeBackend
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()

# 从config.yaml加载配置
with open("config.yaml", 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

# 选择使用的provider与模型
provider = "zhipu" # siliconflow | zhipu
provider_config = config[provider]
base_url = provider_config['base_url']
model = provider_config['model']

# 根据provider获取API密钥
api_key_env = f"{provider.upper()}_API_KEY"
api_key = os.getenv(api_key_env)

# 初始化ChatOpenAI模型
llm = ChatOpenAI(
    api_key=api_key,
    base_url=base_url,
    model=model,
    temperature=0.7
)

system_prompt_template = load_prompt("system_prompt.yaml", encoding="utf-8")

tools_description = """
- 规划任务：使用 write_todos 工具来规划和分解任务
- 管理文件系统：使用 ls, read_file, write_file, edit_file 等工具管理文件
- 委派子任务：委派复杂任务给专门的子智能体
"""

system_prompt = system_prompt_template.format(tools_description=tools_description)

current_dir = os.path.dirname(os.path.abspath(__file__))
files_dir = os.path.join(current_dir, "files")
memories_dir = os.path.join(current_dir, "memories")

def make_backend(runtime):
    return CompositeBackend(
        default=FilesystemBackend(root_dir=files_dir, virtual_mode=True),
        routes={
            "/memories/": FilesystemBackend(root_dir=memories_dir, virtual_mode=True)
        }
    )

agent = create_deep_agent(
    tools=[],
    system_prompt=system_prompt,
    model=llm,
    backend=make_backend
)

# 导出agent供langgraph CLI使用
__all__ = ["agent"]
