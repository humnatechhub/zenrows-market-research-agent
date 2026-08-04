# ZenRows Market Research Agent

A LangChain agent that scrapes real web pages — including bot-protected sites — using ZenRows and returns structured data for market research.

Built with ZenRows, LangChain, and LangGraph.

## What it does

- Bypasses anti-bot protection on real websites
- Scrapes product listings and returns structured JSON
- Uses GPT-4o-mini to format and reason over scraped data

## Setup

1. Clone this repo
2. Install dependencies:
   pip install -r requirements.txt
3. Copy `.env.example` to `.env` and add your API keys
4. Run the agent:
   python market_research_agent.py

## Environment Variables

ZENROWS_API_KEY - Get yours at zenrows.com  
OPENAI_API_KEY - Get yours at platform.openai.com

## Read the full tutorial

[How to Build a Market Research Agent with ZenRows and LangChain](https://dev.to/zenrows/how-to-build-a-market-research-agent-with-zenrows-and-langchain-1mck)
