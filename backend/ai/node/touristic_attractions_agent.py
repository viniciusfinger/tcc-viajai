from backend.ai.model.state import State
from langchain_openai import ChatOpenAI
from backend.ai.model.touristic_attraction import TouristicAttraction
from langchain_core.output_parsers import PydanticOutputParser
from typing import List
from pydantic import BaseModel, Field
import logging
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os


def touristic_attractions_agent(state: State) -> dict[str, list[TouristicAttraction]]:
    """Fetch in LLM for touristic attractions in the location of travel."""
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    logging.info(f"[Touristic Attractions Agent] Fetching touristic attractions for {state.get('destination')}. Trace: {state.get('trace_id')}")
    
    llm = ChatOpenAI(model="gpt-4o", temperature=0.0, api_key=OPENAI_API_KEY)
    
    parser = PydanticOutputParser(pydantic_object=TouristicAttractionListWrapper)
    
    prompt_template = PromptTemplate.from_template("""
        You are a travel planner. Your task is to list the main touristic attractions in {destination}.
        
        List at least 10 different touristic attractions. If you can't find any, list as many as you can.
        
        The user is interested in {interests}, so bring touristic attractions 
        that are related to the user's interests and also general interest attractions.
        
        Respond in the following format, ignoring additional texts or explanations:
        {format_instructions}
    """)
    
    prompt = prompt_template.format(
        destination=state.get('destination'), 
        interests=state.get('interests'), 
        format_instructions=parser.get_format_instructions()
    )
    
    response = llm.invoke(prompt)
    
    attractions_list_wrapper = parser.parse(response.content)
    
    return { "touristic_attractions": attractions_list_wrapper.attractions }


class TouristicAttractionListWrapper(BaseModel):
    """A wrapper class necesseary to handle pydantic list schema."""
    
    attractions: List[TouristicAttraction] = Field(description="A list of touristic attractions")