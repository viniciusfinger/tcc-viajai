import { Routes } from '@angular/router';

export const routes: Routes = [
    {
        path: '',
        redirectTo: 'create-itinerary',
        pathMatch: 'full'
    },
    {
        path: 'create-itinerary',
        loadComponent: () => import('./pages/create-itinerary/create-itinerary.component')
            .then(m => m.CreateItineraryComponent)
    },
    {
        path: 'travel-itinerary',
        loadComponent: () => import('./pages/travel-itinerary/travel-itinerary.component')
            .then(m => m.TravelItineraryComponent)
    }
];

