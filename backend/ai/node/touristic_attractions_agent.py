from backend.ai.model.state import State
from langchain_openai import ChatOpenAI
from backend.ai.model.touristic_attraction import TouristicAttraction
from langchain_core.output_parsers import PydanticOutputParser
from typing import List
from pydantic import BaseModel, Field

def touristic_attractions_agent(state: State) -> dict[str, list[TouristicAttraction]]:
    """Fetch in LLM for touristic attractions in the location of travel."""
    
    llm = ChatOpenAI(model="gpt-4o")
    
    parser = PydanticOutputParser(pydantic_object=TouristicAttractionListWrapper)
    
    prompt = f"""
    Você é um especialista em turismo e está ajudando um cliente a planejar sua viagem.
    
    Liste os principais pontos turísticos em {state.get('destination')}.
    
    Traga ao menos 10 pontos turísticos diferentes. Caso não encontre, traga o máximo que conseguir.
    
    Responda no seguinte formato, ignorando textos ou explicações adicionais:
    {parser.get_format_instructions()}
    """
    
    response = llm.invoke(prompt)
    attractions_list_wrapper = parser.parse(response.content)
    
    return {"touristic_attractions": attractions_list_wrapper.attractions}


class TouristicAttractionListWrapper(BaseModel):
    """A wrapper class necesseary to handle pydantic list schema."""
    
    attractions: List[TouristicAttraction] = Field(description="A list of touristic attractions")