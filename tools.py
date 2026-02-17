from langchain_tavily import TavilySearch

tavily_search = TavilySearch(
    max_results=5,
    topic="general",
    include_answer=False,
    include_raw_content=False,
    include_images=False,
    search_depth="basic"
)

tools = [tavily_search]
