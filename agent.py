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

system_prompt = load_prompt("system_prompt.yaml", encoding="utf-8").format()

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
    backend=make_backend,
    checkpointer=MemorySaver()
)

def main():
    thread_id = str(uuid.uuid4())
    config = {"configurable": {"thread_id": thread_id}}
    
    while True:
        user_input = input("\n你: ")
        
        try:
            result = agent.invoke({
                "messages": [{"role": "user", "content": user_input}]
            }, config=config)
            print(f"\n助手: {result['messages'][-1].content}")
        except Exception as e:
            print(f"错误: {e}")

if __name__ == "__main__":
    main()
