from typing_extensions import TypedDict
from datetime import date
from backend.ai.model.event import Event
from backend.ai.model.touristic_attraction import TouristicAttraction
from backend.ai.model.travel_itinerary import TravelItinerary
from backend.ai.model.interest import Interest

class State(TypedDict):
    """
    Representation of the state machine (StateGraph) state.
    The langgraph's add_messages function adds messages to the message list.
    """
    trace_id: str
    destination: str
    start_date: date
    end_date: date
    events: list[Event]
    touristic_attractions: list[TouristicAttraction]
    travel_itinerary: TravelItinerary
    interests: list[Interest]