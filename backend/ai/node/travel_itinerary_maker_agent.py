from backend.ai.model.state import State
from backend.ai.model.travel_itinerary import TravelItinerary
from langchain_openai import ChatOpenAI
import logging
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


def travel_itinerary_maker_agent(state: State) -> dict[str, TravelItinerary]:
    """ Make a travel itinerary based on the events and touristic attractions. """
    
    logging.info(f"[Travel Itinerary Maker Agent] Making travel itinerary. Trace: {state.get('trace_id')}")
    
    llm = ChatOpenAI(model="gpt-4o", max_retries=5)
    
    parser = PydanticOutputParser(pydantic_object=TravelItineraryWrapper)
    
    prompt = f"""
    Você é um especialista em turismo com muito conhecimento em planejamento de viagens e organização de dias.
    
    Você recebeu uma lista de eventos e pontos turísticos de uma cidade e precisa organizar um roteiro de viagem.
    
    O seu cliente viajará de {state.get('start_date')} até {state.get('end_date')} e irá visitar {state.get('destination')}.
    
    Organize os eventos e pontos turísticos em dias de viagem, de forma que o cliente possa aproveitar ao máximo sua viagem e visitar os eventos.
    
    Os eventos são:
    {state.get('events')}
    
    Os pontos turísticos são:
    {state.get('touristic_attractions')}
    
    Responda no seguinte formato, ignorando textos ou explicações adicionais:
    {parser.get_format_instructions()}
    """
    
    response = llm.invoke(prompt)
    

    travel_itinerary_wrapper = parser.parse(response.content)
    
    return {"travel_itinerary": travel_itinerary_wrapper.travel_itinerary}

class TravelItineraryWrapper(BaseModel):
    """A wrapper class necesseary to handle pydantic list schema."""
    
    travel_itinerary: TravelItinerary = Field(description="The travel itinerary")