from typing import Annotated
from typing_extensions import TypedDict
from langchain_core.messages import AnyMessage
from langgraph.graph import add_messages
from datetime import date
from project.ai.model.event import Event
from project.ai.model.touristic_attraction import TouristicAttraction


class State(TypedDict):
    """
    Representation of the state machine (StateGraph) state.
    The langgraph's add_messages function adds messages to the message list.
    """
    destination: str
    start_date: date
    end_date: date
    # messages: Annotated[list[AnyMessage], add_messages] #todo: entender o funcionamento disso
    events: list[Event]
    touristic_attractions: list[TouristicAttraction]