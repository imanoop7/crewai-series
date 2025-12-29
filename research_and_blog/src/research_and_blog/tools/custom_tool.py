from crewai.tools import BaseTool, tool
from typing import Type
from pydantic import BaseModel, Field
from ddgs import DDGS

@tool
def custom_search(query:str) -> str:
    """Search the web using DuckDuckGo and return formatted results."""
    results = DDGS().text("python programming", max_results=5)
    results_str = "\n\n".join(
    f"Title: {r['title']}\nURL: {r['href']}\nSummary: {r['body']}"
    for r in results
    )
    print(results_str)
    return results_str

