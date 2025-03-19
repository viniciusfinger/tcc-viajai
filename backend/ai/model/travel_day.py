from pydantic import BaseModel, Field
from backend.ai.model.activity import Activity

class TravelDay(BaseModel):
    date: str = Field(description="The date of the day")
    activies: list[Activity] = Field(description="The list of activities of the day")