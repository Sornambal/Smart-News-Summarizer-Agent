try:
    from tavily import TavilyClient
except:
    from tavily.client import TavilyClient

from groq import Groq
from langchain_core.prompts import PromptTemplate
from utils.api_keys import get_groq_key, get_tavily_key

client = Groq(api_key=get_groq_key())
tavily = TavilyClient(api_key=get_tavily_key())

filter_prompt = PromptTemplate(
    input_variables=["results"],
    template="""
You are a news filtering agent.
Given the search results:
{results}

Pick ONLY the 3–5 most relevant URLs.
Return only URLs, one per line.
"""
)

def perform_web_search(query: str):
    try:
        response = tavily.search(query=query, max_results=10)
        return response.get("results", [])
    except Exception as e:
        print("❌ Tavily error:", e)
        return []

def select_relevant_articles(search_results):
    try:
        formatted = ""
        for r in search_results:
            formatted += f"Title: {r.get('title')}\nURL: {r.get('url')}\nSnippet: {r.get('snippet')}\n\n"

        prompt = filter_prompt.format(results=formatted)

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )

        # ✅ Correct extraction
        raw_output = response.choices[0].message.content.strip()

        urls = raw_output.split("\n")
        urls = [u.strip() for u in urls if u.startswith("http")]

        return urls

    except Exception as e:
        print("❌ Error in select_relevant_articles:", e)
        return []
