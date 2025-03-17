from pydantic import BaseModel
from typing import Optional

class TravelInput(BaseModel):
    trace_id: Optional[str] = None
    destination: str
    start_date: str
    end_date: str

    def get_as_dict(self):
        return {
            "trace_id": self.trace_id,
            "destination": self.destination,
            "start_date": self.start_date,
            "end_date": self.end_date
        }