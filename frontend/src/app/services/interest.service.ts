import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class InterestService {
  private readonly apiUrl = 'http://localhost:8000';

  constructor(private readonly http: HttpClient) { }

  getInterests(): Observable<string[]> {
    return this.http.get<string[]>(`${this.apiUrl}/interests`);
  }
}
