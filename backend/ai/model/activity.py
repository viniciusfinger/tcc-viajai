from pydantic import BaseModel, Field
from datetime import date as date_type


class Activity(BaseModel):
    name: str = Field(description="The name of the activity")
    description: str = Field(description="The description of the activity")
    address: str = Field(description="The address of the activity, let empty if it is not available")
    date: date_type = Field(description="The date of the activity, let empty if it is not available")
    time: str = Field(description="The time of the activity, let empty if it is not available")
    source: str = Field(description="The source of the activity, let empty if it is not available")