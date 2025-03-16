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
    
    Traga ao menos 10 pontos turísticos diferentes. Caso não encontre, traga o máximo que conseguir.
    
    Retorne diretamente a resposta no seguinte formato JSON, dispensando qualquer outro texto:
    ```json
    [
        {{
            "name": "Nome do local",
            "description": "Descrição detalhada do local",
            "address": "Endereço completo"
        }},
        ...
    ]
    ```
    """
    
    response = llm.invoke(prompt)
    attractions = _extract_data_from_response(response)
    
    return {"touristic_attractions": attractions}


def _extract_data_from_response(response: dict) -> list[TouristicAttraction]:
    """Convert the LLM response into a list of touristic attractions."""
    

    attractions = []
    
    for attraction_data in json.loads(response.content.replace("```json\n", "").replace("\n```", "")):
        touristic_attraction = TouristicAttraction()
        touristic_attraction.name = attraction_data["name"]
        touristic_attraction.description = attraction_data["description"] 
        touristic_attraction.address = attraction_data["address"]
        attractions.append(touristic_attraction)
    
    return attractions
