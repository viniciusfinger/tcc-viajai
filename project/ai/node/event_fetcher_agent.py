from langchain import hub
from langchain_openai import ChatOpenAI
from project.ai.model.state import State
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.agent_toolkits.load_tools import load_tools

def event_fetcher_agent(state: State) -> dict[str, str]:
    """Fetch events occurring in the period and location of travel."""
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
    tools = load_tools(['ddg-search', 'wikipedia'], llm=llm)
    prompt = hub.pull("hwchase17/react")
    
    texto = f"Estou indo viajar para {state.get('destination')} entre os dias {state.get('start_date')} e {state.get('end_date')}. Busque eventos ocorrendo nesse período e local."
    
    agent = create_react_agent(llm=llm, prompt=prompt, tools=tools)
    
    executor = AgentExecutor(agent=agent, tools=tools, prompt=prompt, handle_parsing_errors=True, verbose=True)
    result = executor.invoke({"input": texto})
    return {"events": result['output']}
    