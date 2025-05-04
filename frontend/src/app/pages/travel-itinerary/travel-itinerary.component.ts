import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TravelItineraryService } from '../../services/travel-itinerary.service';
import { TravelInput } from '../../commons/travel-input';
import { TravelItinerary } from '../../commons/travel-itinerary';
import { RouterModule } from '@angular/router';
@Component({
  selector: 'app-travel-itinerary',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './travel-itinerary.component.html',
  styleUrl: './travel-itinerary.component.css'
})
export class TravelItineraryComponent implements OnInit {
  travelItinerary: TravelItinerary | null = null;
  isLoading: boolean = false;
  error: string | null = null;

  constructor(
    private readonly travelItineraryService: TravelItineraryService
  ) { }

  ngOnInit() {
    const state = history.state as { travelInput: TravelInput };

    console.log('State: ', state);

    if (!state?.travelInput) {
      this.error = 'Dados de viagem não encontrados';
      return;
    }

    this.isLoading = true;

    this.travelItineraryService.getTravelPlan(state.travelInput).subscribe({
      next: (itinerary) => {
        this.travelItinerary = itinerary;
        this.isLoading = false;
      },
      error: (error) => {
        console.error('Error getting travel plan:', error);
        this.error = 'Ocorreu um erro ao gerar o roteiro. Por favor, tente novamente.';
        this.isLoading = false;
      }
    });
  }
}
