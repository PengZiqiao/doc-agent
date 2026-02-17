import os
import yaml
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI



# 读取配置文件
with open("config.yaml", 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

# 从配置文件提取模型配置
provider = "zhipu"
provider_config = config[provider]
base_url = provider_config['base_url']
model = provider_config['model']

# 加载环境变量，获取 API 密钥
load_dotenv()
api_key = os.getenv(f"{provider.upper()}_API_KEY")

# 初始化大模型客户端
llm = ChatOpenAI(
    api_key=api_key,
    base_url=base_url,
    model=model,
    temperature=0.7
)
