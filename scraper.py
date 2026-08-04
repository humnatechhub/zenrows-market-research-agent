from langchain_zenrows import ZenRowsUniversalScraper
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
import os

# Set these in your environment before running
# export ZENROWS_API_KEY=your_key_here
# export OPENAI_API_KEY=your_key_here

def scraper():
    llm = ChatOpenAI(model="gpt-4o-mini")
    zenrows_tool = ZenRowsUniversalScraper()

    agent = create_react_agent(llm, [zenrows_tool])

    try:
        result = agent.invoke(
            {
                "messages": [{"role": "user", "content": "What is the major highlight on https://www.scrapingcourse.com/antibot-challenge"}]
            }
        )
        for message in result["messages"]:
            print(f"{message.content}")
    except Exception as e:
        print(f"Error running agent: {e}")

scraper()
