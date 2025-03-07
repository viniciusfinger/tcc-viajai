from langchain import hub
from langchain_openai import ChatOpenAI
from backend.ai.model.state import State
from backend.ai.model.event import Event
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.agent_toolkits.load_tools import load_tools
import json
from datetime import datetime

def events_fetcher_agent(state: State) -> dict[str, list[Event]]:
    """Fetch in DuckDuckGo and Wikipedia for events occurring in the period and location of travel."""
    llm = ChatOpenAI(model="gpt-4", temperature=0.2)
    
    tools = load_tools(["ddg-search"], llm=llm)
    
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    
    response = agent_executor.invoke({
        "input": f"""
        Você é um especialista em eventos e está ajudando um cliente a encontrar eventos durante sua viagem.
        
        Use a ferramenta de busca para encontrar eventos que acontecerão em {state.get('destination')} 
        entre {state.get('start_date')} e {state.get('end_date')}.
        
        Ignore possíveis erros na data e busque por eventos que acontecerão nesse período.
        
        Obrigatoriamente retorne a resposta no seguinte formato JSON:
        [
            {{
                "name": "Nome do evento",
                "description": "Descrição detalhada do evento", 
                "address": "Local/endereço do evento",
                "date": "YYYY-MM-DD",
                "time": "HH:MM",
                "source": "URL da fonte"
            }},
            ...
        ]
        """
    })
    
    events = []
    
    result = response["output"]
    json_str = result[result.find('['):result.rfind(']')+1]
    
    for event_data in json.loads(json_str):
        event = Event()
        event.name = event_data["name"]
        event.description = event_data["description"]
        event.address = event_data["address"]
        event.date = datetime.strptime(event_data["date"], "%Y-%m-%d").date()
        event.time = event_data["time"]
        
        events.append(event)
    
    return {"events": events}