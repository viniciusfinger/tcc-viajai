import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
@Component({
  selector: 'app-create-itinerary',
  imports: [CommonModule],
  templateUrl: './create-itinerary.component.html',
  styleUrl: './create-itinerary.component.css'
})
export class CreateItineraryComponent {
  //todo: pegar interesses do backend
  interests: string[] = ['Esportes', 'Música', 'História'];
  selectedInterests: string[] = [];

  toggleInterest(interest: string) {
    const index = this.selectedInterests.indexOf(interest);
    if (index === -1) {
      this.selectedInterests.push(interest);
    } else {
      this.selectedInterests.splice(index, 1);
    }
  }
}
