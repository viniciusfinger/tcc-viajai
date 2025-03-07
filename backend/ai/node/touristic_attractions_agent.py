from backend.ai.model.state import State
from langchain_openai import ChatOpenAI
from backend.ai.model.touristic_attraction import TouristicAttraction
import json

def touristic_attractions_agent(state: State) -> dict[str, list[TouristicAttraction]]:
    """Fetch in LLM for touristic attractions in the location of travel."""
    
    llm = ChatOpenAI(model="gpt-4o")
    
    prompt = f"""
    Você é um especialista em turismo e está ajudando um cliente a planejar sua viagem.
    
    Liste os principais pontos turísticos em {state.get('destination')}.
    
    Obrigatoriamente retorne a resposta no seguinte formato JSON:
    [
        {{
            "name": "Nome do local",
            "description": "Descrição detalhada do local",
            "address": "Endereço completo"
        }},
        ...
    ]
    """
    
    response = llm.invoke(prompt)
    
    attractions = []
    for attraction_data in json.loads(response.content.replace("```json\n", "").replace("\n```", "")):
        touristic_attraction = TouristicAttraction()
        
        touristic_attraction.name = attraction_data["name"]
        touristic_attraction.description = attraction_data["description"] 
        touristic_attraction.address = attraction_data["address"]
        attractions.append(touristic_attraction)
        
    return {"touristic_attractions": attractions}