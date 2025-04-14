from langchain_openai import ChatOpenAI
from backend.ai.model.state import State
from backend.ai.model.event import Event
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.agent_toolkits.load_tools import load_tools
from typing import List
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
import logging
from langchain.prompts import PromptTemplate


def events_fetcher_agent(state: State) -> dict[str, list[Event]]:
    """Fetch in DuckDuckGo for events occurring in the period and location of travel."""
    
    logging.info(f"[Events Fetcher Agent] Fetching events for {state.get('destination')} between {state.get('start_date')} and {state.get('end_date')}. Trace: {state.get('trace_id')}")
    
    llm = ChatOpenAI(model="gpt-4o", temperature=0.0)
    
    tools = load_tools(["ddg-search"], llm=llm)
    
    prompt = PromptTemplate.from_template("""                                      
        Exec. You have access to the following tools:
        {tools}
        
        You must always use the following format, never change it:

        Question: the input question you must answer
        Thought: you should always think about what to do
        Action: the action to take, should be one of [{tool_names}]
        Action Input: the input to the action
        Observation: the result of the action
        ... (this Thought/Action/Action Input/Observation can repeat )
        Thought: I now know the final answer
        Final Answer: the final answer to the original input question

        Begin!

        Question: {input}
        Thought: {agent_scratchpad}
    """)
    
    agent = create_react_agent(llm, tools, prompt)
    
    parser = PydanticOutputParser(pydantic_object=EventListWrapper)
    
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations=10)
    
    prompt_template = PromptTemplate.from_template("""
        Find events in {destination} between {start_date} and {end_date} 
        that match these interests: {interests}.
        Also include some general interest events.
        Find at least 5 events. 
        
        Format the response exactly as specified in the parser instructions:
        {format_instructions}
    """)
    
    prompt = prompt_template.format(
        destination=state.get('destination'), 
        start_date=state.get('start_date'),  
        end_date=state.get('end_date'),     
        interests=state.get('interests'),
        format_instructions=parser.get_format_instructions()
    )
    
    response = agent_executor.invoke({ "input": prompt })
    
    events_list_wrapper = parser.parse(response["output"])
    
    return {"events": events_list_wrapper.events}


class EventListWrapper(BaseModel):
    """A wrapper class necesseary to handle pydantic list schema."""
    
    events: List[Event] = Field(description="A list of events")