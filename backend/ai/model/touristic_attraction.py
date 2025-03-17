from pydantic import BaseModel, Field

class TouristicAttraction(BaseModel):
    name: str = Field(description="The name of the touristic attraction")
    description: str = Field(description="A brief description of the touristic attraction")
    address: str = Field(description="The address of the touristic attraction")