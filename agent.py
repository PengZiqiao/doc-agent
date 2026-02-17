import os

from dotenv import load_dotenv

from langchain_core.prompts import load_prompt
from deepagents import create_deep_agent
from deepagents.backends import FilesystemBackend, CompositeBackend

from model import llm
from tools import tools

load_dotenv()

# 配置提示词
system_prompt_template = load_prompt("system_prompt.yaml", encoding="utf-8")
system_prompt = system_prompt_template.format()

# 配置文件系统后端
current_dir = os.path.dirname(os.path.abspath(__file__))
files_dir = os.path.join(current_dir, "files")
memories_dir = os.path.join(current_dir, "memories")
skills_dir = os.path.join(current_dir, "skills/")

def make_backend(runtime):
    return CompositeBackend(
        default=FilesystemBackend(root_dir=current_dir),
        routes={
            "/files/": FilesystemBackend(root_dir=files_dir, virtual_mode=True),
            "/memories/": FilesystemBackend(root_dir=memories_dir, virtual_mode=True)
        }
    )

# 初始化智能体
agent = create_deep_agent(
    tools=tools,
    system_prompt='你是个人工智能助手',
    model=llm,
    backend=make_backend,
    skills=[skills_dir]
)

# 导出agent供langgraph CLI使用
__all__ = ["agent"]
