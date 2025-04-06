import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { TravelInput } from '../commons/travel-input';
import { TravelItinerary } from '../commons/travel-itinerary';


@Injectable({
  providedIn: 'root'
})
export class TravelItineraryService {
  private readonly apiUrl = 'http://localhost:8000';

  constructor(private readonly http: HttpClient) { }

  getTravelPlan(travelInput: TravelInput): Observable<TravelItinerary> {
    return this.http.post<TravelItinerary>(`${this.apiUrl}/travel-itineraries`, travelInput);
  }
}
