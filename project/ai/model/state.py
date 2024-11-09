from typing import Annotated
from typing_extensions import TypedDict
from langchain_core.messages import AnyMessage
from langgraph.graph import add_messages
from datetime import date

class State(TypedDict):
    """
    Representação do estado da máquina de estados (StateGraph).
    A função add_messages do langgraph adiciona as mensagens a lista de mensagens.
    """
    destination: str
    start_date: date
    end_date: date
    messages: Annotated[list[AnyMessage], add_messages]
    events: str
    