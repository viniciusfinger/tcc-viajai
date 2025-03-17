from fastapi import APIRouter
from backend.model.TravelInput import TravelInput
import backend.service.ai_service as ai_service
import logging
import uuid

travel_itinerary = APIRouter(prefix="/travel_itinerary")

@travel_itinerary.get("")
async def get_travel_itinerary(travel_input: TravelInput):
    travel_input.trace_id = str(uuid.uuid4())
    logging.info(f"[Travel Itinerary Controller] Generating travel itinerary. Trace: {travel_input.trace_id}")
    
    response = ai_service.invoke(travel_input)
    
    logging.info(f"[Travel Itinerary Controller] 200 OK - Success generating travel itinerary. Trace: {travel_input.trace_id}")
    
    return response