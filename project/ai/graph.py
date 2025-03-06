from langgraph.graph import START, END
from project.ai.model.state import State
from langgraph.graph.state import StateGraph, CompiledStateGraph
from project.ai.node.events_fetcher_agent import events_fetcher_agent
from project.ai.node.touristic_attractions_agent import touristic_attractions_agent


def create_graph() -> CompiledStateGraph:
    graph = StateGraph(State)
    
    graph.add_node("events_fetcher_agent", events_fetcher_agent)
    graph.add_node("touristic_attractions_agent", touristic_attractions_agent)
    
    graph.add_edge(START, "events_fetcher_agent")
    graph.add_edge("events_fetcher_agent", "touristic_attractions_agent")
    graph.add_edge("touristic_attractions_agent", END)
    
    return graph.compile()