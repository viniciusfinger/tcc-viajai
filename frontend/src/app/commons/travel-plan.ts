import { TouristicAttraction } from "./touristic-attraction";

export interface TravelPlan {
    trace_id: string;
    destination: string;
    start_date: string;
    end_date: string;
    events: Event[];
    touristic_attractions: TouristicAttraction[];
    interests: string[];
}