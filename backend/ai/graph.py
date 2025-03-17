from langgraph.graph import START, END
from backend.ai.model.state import State
from langgraph.graph.state import StateGraph, CompiledStateGraph
from backend.ai.node.events_fetcher_agent import events_fetcher_agent
from backend.ai.node.touristic_attractions_agent import touristic_attractions_agent


def create_graph() -> CompiledStateGraph:
    graph = StateGraph(State)
    
    graph.add_node("events_fetcher_agent", events_fetcher_agent)
    graph.add_node("touristic_attractions_agent", touristic_attractions_agent)
    
    graph.add_edge(START, "events_fetcher_agent")
    graph.add_edge(START, "touristic_attractions_agent")
    graph.add_edge("events_fetcher_agent", END)
    graph.add_edge("touristic_attractions_agent", END)
    
    # todo: adicionar node de criação de itinerário
    
    return graph.compile()