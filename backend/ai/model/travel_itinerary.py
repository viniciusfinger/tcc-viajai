from pydantic import BaseModel, Field
from backend.ai.model.travel_day import TravelDay


class TravelItinerary(BaseModel):
    destination: str = Field(description="The destination of the travel")
    start_date: str = Field(description="The start date of the travel")
    end_date: str = Field(description="The end date of the travel")
    travel_days: list[TravelDay] = Field(description="The list of travel days with a list of activities of each day")
