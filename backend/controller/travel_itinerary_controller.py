from fastapi import APIRouter
from backend.model.TravelInput import TravelInput
import backend.service.ai_service as ai_service

travel_itinerary = APIRouter(prefix="/travel_itinerary")

@travel_itinerary.get("")
async def get_travel_itinerary(travel_input: TravelInput):
    return ai_service.invoke(travel_input)
