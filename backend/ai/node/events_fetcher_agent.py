from langchain import hub
from langchain_openai import ChatOpenAI
from backend.ai.model.state import State
from backend.ai.model.event import Event
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.agent_toolkits.load_tools import load_tools
import json
from datetime import datetime


def events_fetcher_agent(state: State) -> dict[str, list[Event]]:
    """Fetch in DuckDuckGo for events occurring in the period and location of travel."""
    
    llm = ChatOpenAI(model="gpt-4o")
    
    tools = load_tools(["ddg-search"], llm=llm)
    
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm, tools, prompt)
    
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=False,
        handle_parsing_errors=True,
        max_iterations=3)
    
    response = agent_executor.invoke({
        "input": f"""
        Você é um especialista em eventos e está ajudando um cliente a encontrar eventos durante sua viagem.
        
        Use a ferramenta de busca para encontrar eventos que acontecerão em {state.get('destination')} 
        entre {state.get('start_date')} e {state.get('end_date')}.
        
        Retorne a resposta no seguinte formato JSON:
        
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
    
    events = _extract_data_from_response(response["output"])
    
    return {"events": events}


def _extract_data_from_response(response: str) -> list[Event]:
    """Convert the LLM response into a list of events."""
    
    events = []
    
    json_str = response[response.find('['):response.rfind(']')+1]
    
    for event_data in json.loads(json_str):
        event = Event(
            name=event_data["name"],
            description=event_data["description"],
            address=event_data["address"],
            date=datetime.strptime(event_data["date"], "%Y-%m-%d").date(),
            time=event_data["time"],
            source=event_data["source"]
        )
        
        events.append(event)
    
    return events

