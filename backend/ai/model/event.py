from datetime import date as date_type
from pydantic import BaseModel, Field


class Event(BaseModel):
    name: str = Field(description="The name of the event")
    description: str = Field(description="The description of the event")
    address: str | None = Field(default=None, description="The address of the event, let empty if it is not available")
    date: date_type | None = Field(default=None, description="The date of the event, let empty if it is not available")
    time: str | None = Field(default=None, description="The time of the event, let empty if it is not available")
    source: str | None = Field(default=None, description="URL of the event source, let empty if it is not available")