import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { TravelInput } from '../commons/travel-input';
import { TravelPlan } from '../commons/travel-plan';


@Injectable({
  providedIn: 'root'
})
export class TravelItineraryService {
  private readonly apiUrl = 'http://localhost:8000';

  constructor(private readonly http: HttpClient) { }

  getTravelPlan(travelInput: TravelInput): Observable<TravelPlan> {
    return this.http.post<TravelPlan>(`${this.apiUrl}/create-itinerary`, travelInput);
  }
}
