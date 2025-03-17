from langchain import hub
from langchain_openai import ChatOpenAI
from backend.ai.model.state import State
from backend.ai.model.event import Event
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.agent_toolkits.load_tools import load_tools
from typing import List
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
import logging

def events_fetcher_agent(state: State) -> dict[str, list[Event]]:
    """Fetch in DuckDuckGo for events occurring in the period and location of travel."""
    
    logging.info(f"[Events Fetcher Agent] Fetching events for {state.get('destination')} between {state.get('start_date')} and {state.get('end_date')}. Trace: {state.get('trace_id')}")
    
    llm = ChatOpenAI(model="gpt-4o", temperature=0.2)
    
    tools = load_tools(["ddg-search"], llm=llm)
    
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm, tools, prompt)
    
    parser = PydanticOutputParser(pydantic_object=EventListWrapper)
    
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=False,
        handle_parsing_errors=True,
        max_iterations=5)
    
    response = agent_executor.invoke({
        "input": f"""
        Você é um especialista em eventos e está ajudando um cliente a encontrar eventos durante sua viagem.
        
        Use a ferramenta de busca para encontrar eventos que acontecerão em {state.get('destination')} 
        entre {state.get('start_date')} e {state.get('end_date')}.
        
        Responda no seguinte formato, ignorando textos ou explicações adicionais:
        {parser.get_format_instructions()}
        """
    })
    
    events_list_wrapper = parser.parse(response["output"])
    
    return {"events": events_list_wrapper.events}


class EventListWrapper(BaseModel):
    """A wrapper class necesseary to handle pydantic list schema."""
    
    events: List[Event] = Field(description="A list of events")