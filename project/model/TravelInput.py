from pydantic import BaseModel

class TravelInput(BaseModel):
    destination: str
    start_date: str
    end_date: str

    def get_as_dict(self):
        return {
            "destination": self.destination,
            "start_date": self.start_date,
            "end_date": self.end_date
        }