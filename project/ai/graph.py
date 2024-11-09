from langgraph.graph import START, END
from project.ai.model.state import State
from langgraph.graph.state import StateGraph, CompiledStateGraph
from project.ai.node.event_fetcher_agent import event_fetcher_agent

def create_graph() -> CompiledStateGraph:
    graph = StateGraph(State)
    graph.add_node("event_fetcher_agent", event_fetcher_agent)
    graph.add_edge(START, "event_fetcher_agent")
    graph.add_edge("event_fetcher_agent", END)
    
    return graph.compile()