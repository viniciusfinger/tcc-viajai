from fastapi import APIRouter

travel_itinerary = APIRouter(prefix="/travel_itinerary")
#graph = create_graph()

@travel_itinerary.get("")
async def get_travel_itinerary():
    return {"travel_itinerary": "travel itinerary"}
