import { Routes } from '@angular/router';

export const routes: Routes = [
    {
        path: '',
        redirectTo: 'create',
        pathMatch: 'full'
    },
    {
        path: 'create',
        loadComponent: () => import('./pages/create-itinerary/create-itinerary.component')
            .then(m => m.CreateItineraryComponent)
    },
    {
        path: 'travel-itinerary',
        loadComponent: () => import('./pages/travel-itinerary/travel-itinerary.component')
            .then(m => m.TravelItineraryComponent)
    }
];

