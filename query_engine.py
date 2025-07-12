import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType, Tool
from langchain.chains import RetrievalQA

# OpenAI
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from openai import OpenAIError

# Gemini
from langchain_google_genai import ChatGoogleGenerativeAI

from scripts.stock_tools import (
    get_stock_price_on_date,
    get_highest_price,
    get_lowest_price,
    get_average_price,
)
from scripts.transcript_qa import load_transcript_vectorstore

load_dotenv()

# 🔁 Function to switch between LLMs
def get_llm():
    try:
        return ChatOpenAI(
            temperature=0,
            model="gpt-3.5-turbo",
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
    except Exception as e:
        print(f"[Fallback to Gemini] OpenAI error: {e}")
        return ChatGoogleGenerativeAI(
            model="gemini-pro",
            temperature=0,
            google_api_key=os.getenv("GEMINI_API_KEY")
        )

llm = get_llm()

tools = [
    Tool.from_function(
        name="GetStockPriceOnDate",
        func=get_stock_price_on_date,
        description="Get stock price for a date like '20-01-2023'"
    ),
    Tool.from_function(
        name="GetHighestPrice",
        func=get_highest_price,
        description="Get highest stock price in a month like 'Jan-2024'"
    ),
    Tool.from_function(
        name="GetLowestPrice",
        func=get_lowest_price,
        description="Get lowest stock price in a month like 'Jan-2024'"
    ),
    Tool.from_function(
        name="GetAveragePrice",
        func=get_average_price,
        description="Get average stock price in a month like 'Jan-2024'"
    )
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False
)

def run_agent(query: str) -> str:
    return agent.invoke({"input": query})["output"]

def run_transcript_query(query: str) -> str:
    retriever = load_transcript_vectorstore().as_retriever(search_type="similarity", search_kwargs={"k": 3})
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain.run(query)
