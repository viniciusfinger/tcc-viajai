from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_community.agent_toolkits.load_tools import load_tools

llm = ChatOpenAI(model="gpt-4o-mini")

destination = input("Destination: ")
start_date = input("Trip start date: ")
end_date = input("Trip end date: ")

query = f"""
I'm going to travel to {destination} between {start_date} and {end_date}.
I want you to make a travel itinerary of these days for me with touristic attractions and events that will occur on that date.
Follow the example below
Day 1: September 17, 2024
- Event name and details
- Event name and details
"""

def researchAgent(query, llm):
    """
    Agente que busca dados do destino da viagem e eventos que ocorrerão no período
    """
    tools = load_tools(['ddg-search', 'wikipedia'], llm=llm)
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, prompt=prompt, tools=tools)
    agent_executor = AgentExecutor(agent=agent, tools=tools, prompt=prompt, verbose=True)

    web_context = agent_executor.invoke({"input": query})
    return web_context['output']

def supervisorAgent(query, llm, web_context):
    """
    Agente que cria o itinerário de viagem de acordo com o que o agente de pesquisa encontrou.
    """

    prompt_template = """
    You are a manager at a travel agency. Your final answer should be a complete and detailed travel itinerary. Use the context of events and user input to develop the itinerary.
    Context: {web_context}
    User: {query}
    Assistant:
    """
    
    prompt = PromptTemplate(
        input_variables=['web_context', 'query'],
        template=prompt_template
    )
    
    sequence = RunnableSequence(prompt | llm)
    
    return sequence.invoke({"web_context": web_context, "query": query})

def getResponse(query, llm):
    """Orquestra as chamadas aos agentes"""

    web_context = researchAgent(query, llm)
    return supervisorAgent(query, llm, web_context)

print("- - - - - - - - - - - - - - - - ")
print(getResponse(query, llm).content)
