from pydantic import BaseModel, Field


class Event(BaseModel):
    name: str = Field(description="The name of the event")
    description: str = Field(description="A detailed description of the event")
    address: str | None = Field(default=None, description="The address or location of the event, let empty if it is not available")
    date: str | None = Field(default=None, description="The date of the event in format dd/mm/yyyy")
    time: str | None = Field(default=None, description="The time of the event in format hh:mm 24h, let empty if it is not available")
    source: str | None = Field(default=None, description="URL of the event source, let empty if it is not available")