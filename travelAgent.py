import os
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent 

llm = ChatOpenAI(model="gpt-3.5-turbo")

tools = load_tools(['ddg-search', 'wikipedia'], llm=llm)

agent = initialize_agent(
    tools=tools, 
    llm=llm, 
    agent='zero-shot-react-description',
    verbose=True
    )

query = """
Vou viajar para londres em agosto de 2024. Quero que faça um roteiro de viagem para mim com eventos que irão ocorrer na data e com o preço da passagem de São Paulo para Londres em real brasileiro
"""

agent.run(query)