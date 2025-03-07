from fastapi import FastAPI
from backend.controller.travel_itinerary_controller import travel_itinerary

app = FastAPI()
app.include_router(travel_itinerary)