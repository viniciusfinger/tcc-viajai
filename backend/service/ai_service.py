import logging
from project.ai.graph import create_graph
from project.model.TravelInput import TravelInput

graph = create_graph()

def invoke(travel_input: TravelInput):
    
    config = {"recursion_limit": 5}
    
    try:
        return graph.invoke(travel_input.get_as_dict(), config=config)
    except Exception as e:
        logging.error(f"Error invoking graph: {e}")
        return {"error": str(e)}