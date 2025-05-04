import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TravelItineraryService } from '../../services/travel-itinerary.service';
import { TravelInput } from '../../commons/travel-input';
import { TravelItinerary } from '../../commons/travel-itinerary';
import { RouterModule } from '@angular/router';
import { interval, Subscription } from 'rxjs';
import { takeWhile } from 'rxjs/operators';

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
  
  loadingProgress: number = 0;
  currentMessageIndex: number = 0;
  loadingMessages: string[] = [
    "🎉 Looking for fun events for you...",
    "🍦 Calculating how much ice cream you can eat...", 
    "🍽️ Persuading restaurants to reserve your table...",
    "☀️ Asking the sun to shine during your trip...",
    "🐬 Sending messages to dolphins to welcome you...",
    "🐠 Checking if the fish are in the sea...",
    "☁️ Convincing clouds not to rain...",
    "🐦 Asking birds to sing when you arrive...",
    "📸 Finding the most Instagrammable spots...",
    "☕ Mapping the best routes while having coffee...",
    "👽 Negotiating with martians to let you pass...",
    "⛰️ Asking mountains not to grow until you arrive...",
    "🏖️ Counting sand grains for your perfect beach...",
    "🤵 Training waiters to remember your name...",
    "🚗 Teaching cars to drive themselves for you...",
    "🛣️ Enchanting streets to prevent traffic jams...",
    "🦄 Feeding unicorns that will pull your carriage...",
    "⭐ Asking stars to shine brighter at night...",
    "🚦 Programming traffic lights to stay green on your way...",
    "🌈 Arranging weather to match your mood..."
  ];
  private loadingSubscription?: Subscription;

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

    this.shuffleMessages();
    
    this.isLoading = true;
    this.startLoadingAnimation();

    this.travelItineraryService.getTravelPlan(state.travelInput).subscribe({
      next: (itinerary) => {
        this.ensureFullLoadingAnimation(() => {
          this.travelItinerary = itinerary;
          this.isLoading = false;
        });
      },
      error: (error) => {
        console.error('Error getting travel plan:', error);
        this.error = 'Ocorreu um erro ao gerar o roteiro. Por favor, tente novamente.';
        this.isLoading = false;
        if (this.loadingSubscription) {
          this.loadingSubscription.unsubscribe();
        }
      }
    });
  }

  private startLoadingAnimation() {
    const progressPerMessage = 90 / this.loadingMessages.length;
    
    this.loadingSubscription = interval(2100).subscribe(() => {
      this.currentMessageIndex = (this.currentMessageIndex + 1) % this.loadingMessages.length;
      
      if (this.loadingProgress < 90) {
        this.loadingProgress = Math.min(90, (this.currentMessageIndex + 1) * progressPerMessage);
      }
    });
  }

  private ensureFullLoadingAnimation(callback: () => void) {
    if (this.loadingProgress >= 100) {
      this.completeLoading(callback);
      return;
    }
    
    const remaining = 100 - this.loadingProgress;
    const steps = 10;
    const incrementStep = remaining / steps;
    
    interval(200)
      .pipe(takeWhile(() => this.loadingProgress < 100))
      .subscribe({
        next: () => {
          this.loadingProgress += incrementStep;
          if (this.loadingProgress > 100) this.loadingProgress = 100;
        },
        complete: () => this.completeLoading(callback)
      });
  }

  private shuffleMessages() {
    for (let i = this.loadingMessages.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [this.loadingMessages[i], this.loadingMessages[j]] = [this.loadingMessages[j], this.loadingMessages[i]];
    }
  }

  private completeLoading(callback: () => void) {
    this.currentMessageIndex = this.loadingMessages.length - 1;
    
    setTimeout(() => {
      if (this.loadingSubscription) {
        this.loadingSubscription.unsubscribe();
      }
      callback();
    }, 800);
  }

  ngOnDestroy() {
    if (this.loadingSubscription) {
      this.loadingSubscription.unsubscribe();
    }
  }
}
