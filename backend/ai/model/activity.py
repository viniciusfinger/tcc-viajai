from pydantic import BaseModel, Field
from datetime import date as date_type
from typing import Optional 


class Activity(BaseModel):
    name: str = Field(description="The name of the activity")
    description: str = Field(description="The description of the activity")
    address: Optional[str] = Field(description="The address of the activity, let empty if it is not available")
    type: str = Field(description="The type of the activity, could be 'EVENT' or 'TOURISTIC_ATTRACTION'")
    date: Optional[date_type] = Field(description="The date of the activity, let empty if it is not available")
    time: Optional[str] = Field(description="The time of the activity, let empty if it is not available")
    source: Optional[str] = Field(description="The source of the activity, let empty if it is not available")