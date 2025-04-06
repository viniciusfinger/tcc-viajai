from fastapi import APIRouter, HTTPException
from backend.model.TravelInput import TravelInput
from backend.ai.model.travel_itinerary import TravelItinerary
import backend.service.ai_service as ai_service
import logging
import uuid


travel_itinerary_router = APIRouter(prefix="/travel-itineraries")

@travel_itinerary_router.post("")
async def get_travel_itinerary(travel_input: TravelInput) -> TravelItinerary:
    try:
        travel_input.trace_id = str(uuid.uuid4())
        logging.info(f"[Travel Itinerary Controller] Generating travel itinerary. Trace: {travel_input.trace_id}")
        
        response = ai_service.invoke(travel_input)
        
        logging.info(f"[Travel Itinerary Controller] 200 OK - Success generating travel itinerary. Trace: {travel_input.trace_id}")
        
        return response["travel_itinerary"]
    except Exception as e:
        logging.error(f"[Travel Itinerary Controller] Error generating travel itinerary. Trace: {travel_input.trace_id}. Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error: " + str(e))
