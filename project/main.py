from attraction_fetcher import fetch_touristic_points
from events_fetcher import fetch_events
from itinerary_maker import make_itinerary

destination = "New York"
start_date = "2024-09-25"
end_date = "2024-10-05"

touristic_points = fetch_touristic_points(destination)
events = fetch_events(start_date, end_date, destination)["output"]

itinerary = make_itinerary(start_date, end_date, destination, touristic_points, events)