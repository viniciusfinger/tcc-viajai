from langgraph.graph import START, END
from backend.ai.model.state import State
from langgraph.graph.state import StateGraph, CompiledStateGraph
from backend.ai.node.events_fetcher_agent import events_fetcher_agent
from backend.ai.node.touristic_attractions_agent import touristic_attractions_agent
from backend.ai.node.travel_itinerary_maker_agent import travel_itinerary_maker_agent   


def create_graph() -> CompiledStateGraph:
    graph = StateGraph(State)
    
    graph.add_node("events_fetcher_agent", events_fetcher_agent)
    graph.add_node("touristic_attractions_agent", touristic_attractions_agent)
    graph.add_node("travel_itinerary_maker_agent", travel_itinerary_maker_agent)
    
    graph.add_edge(START, "events_fetcher_agent")
    graph.add_edge(START, "touristic_attractions_agent")
    
    graph.add_edge("events_fetcher_agent", END)
    graph.add_edge("touristic_attractions_agent", END)
    
    # graph.add_edge("events_fetcher_agent", "travel_itinerary_maker_agent")
    # graph.add_edge("touristic_attractions_agent", "travel_itinerary_maker_agent")
    # graph.add_edge("travel_itinerary_maker_agent", END)
    
    return graph.compile()  