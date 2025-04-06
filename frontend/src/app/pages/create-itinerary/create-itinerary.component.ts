import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { TravelItineraryService } from '../../services/travel-itinerary.service';
import { TravelInput } from '../../commons/travel-input';
import { TravelItinerary } from '../../commons/travel-itinerary';
import { Router } from '@angular/router';
import { InterestService } from '../../services/interest.service';

@Component({
  selector: 'app-create-itinerary',
  imports: [CommonModule, FormsModule],
  templateUrl: './create-itinerary.component.html',
  styleUrl: './create-itinerary.component.css'
})
export class CreateItineraryComponent {
  interests: string[] = [];
  selectedInterests: string[] = [];

  destination: string = '';
  startDate: string = '';
  endDate: string = '';
  isLoading: boolean = false;

  constructor(
    private readonly travelItineraryService: TravelItineraryService,
    private readonly interestService: InterestService,
    private readonly router: Router
  ) { }

  ngOnInit() {
    console.log('ngOnInit');
    this.interestService.getInterests().subscribe((interests) => {
      this.interests = interests;
    });
  }

  toggleInterest(interest: string) {
    const index = this.selectedInterests.indexOf(interest);
    if (index === -1) {
      this.selectedInterests.push(interest);
    } else {
      this.selectedInterests.splice(index, 1);
    }
  }

  onSubmit() {
    if (!this.destination || !this.startDate || !this.endDate || this.selectedInterests.length === 0) {
      alert('Por favor, preencha todos os campos e selecione pelo menos um interesse.');
      return;
    }

    this.isLoading = true;

    const travelInput: TravelInput = {
      destination: this.destination,
      start_date: this.startDate,
      end_date: this.endDate,
      interests: this.selectedInterests
    };

    this.travelItineraryService.getTravelPlan(travelInput).subscribe({
      next: (travelItinerary: TravelItinerary) => {
        this.isLoading = false;
        console.log('Travel itinerary received:', travelItinerary);
        this.router.navigate(['/travel-itinerary'], { state: { travelItinerary } });
      },
      error: (error) => {
        this.isLoading = false;
        console.error('Error getting travel plan:', error);
        alert('Ocorreu um erro ao criar o roteiro. Por favor, tente novamente.');
      }
    });
  }
}
