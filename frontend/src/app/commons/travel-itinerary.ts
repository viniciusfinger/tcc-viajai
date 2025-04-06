import { TravelDay } from "./travel-day";

export interface TravelItinerary {
    destination: string;
    start_date: string;
    end_date: string;
    travel_days: TravelDay[];
}
