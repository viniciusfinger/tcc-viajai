from fastapi import FastAPI
from backend.controller.travel_itinerary_controller import travel_itinerary_router
from backend.config.logger_config import setup_logger
from backend.controller.interests_controller import interests_router

from fastapi.middleware.cors import CORSMiddleware

setup_logger()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(travel_itinerary_router)
app.include_router(interests_router)