from pydantic import BaseModel, Field
from typing import Optional

class TouristicAttraction(BaseModel):
    name: Optional[str] = Field(description="The name of the touristic attraction")
    description: Optional[str] = Field(description="A brief description of the touristic attraction")
    address: Optional[str] = Field(description="The address of the touristic attraction, let empty if it is not available")