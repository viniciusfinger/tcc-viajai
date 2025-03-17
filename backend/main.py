from fastapi import FastAPI
from backend.controller.travel_itinerary_controller import travel_itinerary
from backend.config.logger_config import setup_logger

setup_logger()
app = FastAPI()
app.include_router(travel_itinerary)