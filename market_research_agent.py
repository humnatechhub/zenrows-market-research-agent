from langchain_zenrows import ZenRowsUniversalScraper
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
import os

# Set these in your environment before running
# export ZENROWS_API_KEY=your_key_here
# export OPENAI_API_KEY=your_key_here

def market_research_agent():
    llm = ChatOpenAI(model="gpt-4o-mini")
    zenrows_tool = ZenRowsUniversalScraper(autoparse=True)

    agent = create_react_agent(llm, [zenrows_tool])

    try:
        result = agent.invoke(
            {
                "messages": [{"role": "user", "content": "Visit https://www.scrapingcourse.com/ecommerce/ and scrape the page. Return the 4 cheapest products as JSON with title, price, and url fields."}]
            }
        )
        for message in result["messages"]:
            print(f"{message.content}")
    except Exception as e:
        print(f"Error running agent: {e}")

market_research_agent()
