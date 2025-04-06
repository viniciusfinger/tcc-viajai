import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TravelItinerary } from '../../commons/travel-itinerary';
import { Router } from '@angular/router';

@Component({
  selector: 'app-travel-itinerary',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './travel-itinerary.component.html',
  styleUrl: './travel-itinerary.component.css'
})
export class TravelItineraryComponent implements OnInit {
  travelItinerary: TravelItinerary | null = null;
  isLoading: boolean = true;

  constructor(
    private readonly router: Router
  ) { }

  ngOnInit() {
    const navigation = this.router.getCurrentNavigation();
    if (navigation?.extras.state) {
      this.travelItinerary = navigation.extras.state['travelItinerary'];
    }
    this.isLoading = false;
  }

  formatDate(date: string): string {
    return new Date(date).toLocaleDateString('pt-BR', {
      weekday: 'long',
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });
  }
}
