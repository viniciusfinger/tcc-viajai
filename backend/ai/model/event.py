from datetime import date as date_type
from pydantic import BaseModel, Field

class Event(BaseModel):
    name: str = Field(description="The name of the event")
    description: str = Field(description="The description of the event")
    address: str = Field(description="The address of the event")
    date: date_type = Field(description="The date of the event")
    time: str = Field(description="The time of the event")
    source: str = Field(description="URL of the event source")