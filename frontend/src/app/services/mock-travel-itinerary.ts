import { TravelItinerary } from '../commons/travel-itinerary';

export const mockTravelItinerary: TravelItinerary = {
  destination: 'New York',
  start_date: '2024-09-25',
  end_date: '2024-10-29',
  travel_days: [
    {
      date: '2024-09-25',
      activities: [
        {
          name: 'Arrival at JFK Airport',
          description: 'Welcome to New York! Transfer to your hotel and get settled in.',
          address: 'JFK International Airport, Queens, NY',
          type: 'TOURISTIC_ATTRACTION',
          date: '2024-09-25',
          time: '14:00',
          source: null
        },
        {
          name: 'Times Square',
          description: 'Experience the vibrant heart of New York City with its bright lights and bustling atmosphere.',
          address: 'Times Square, Manhattan, NY',
          type: 'TOURISTIC_ATTRACTION',
          date: '2024-09-25',
          time: '18:00',
          source: null
        }
      ]
    },
    {
      date: '2024-09-26',
      activities: [
        {
          name: 'Central Park',
          description: 'Morning walk through the iconic Central Park, visiting famous landmarks like Bethesda Terrace and Bow Bridge.',
          address: 'Central Park, Manhattan, NY',
          type: 'TOURISTIC_ATTRACTION',
          date: '2024-09-26',
          time: '09:00',
          source: null
        },
        {
          name: 'Metropolitan Museum of Art',
          description: 'Explore one of the world\'s largest and finest art museums.',
          address: '1000 5th Ave, New York, NY',
          type: 'TOURISTIC_ATTRACTION',
          date: '2024-09-26',
          time: '13:00',
          source: null
        }
      ]
    },
    {
      date: '2024-09-27',
      activities: [
        {
          name: 'Statue of Liberty',
          description: 'Visit the iconic symbol of freedom and take a ferry to Liberty Island.',
          address: 'Liberty Island, New York, NY',
          type: 'TOURISTIC_ATTRACTION',
          date: '2024-09-27',
          time: '10:00',
          source: null
        },
        {
          name: 'Empire State Building',
          description: 'Take in breathtaking views of the city from the observation deck.',
          address: '20 W 34th St, New York, NY',
          type: 'TOURISTIC_ATTRACTION',
          date: '2024-09-27',
          time: '15:00',
          source: null
        }
      ]
    },
    {
      date: '2024-09-28',
      activities: [
        {
          name: 'Broadway Show',
          description: 'Experience a world-class Broadway performance in the Theater District.',
          address: 'Various theaters in Manhattan',
          type: 'EVENT',
          date: '2024-09-28',
          time: '19:00',
          source: null
        },
        {
          name: 'High Line Park',
          description: 'Walk along this elevated park built on a historic freight rail line.',
          address: 'The High Line, Manhattan, NY',
          type: 'TOURISTIC_ATTRACTION',
          date: '2024-09-28',
          time: '14:00',
          source: null
        }
      ]
    },
    {
      date: '2024-09-29',
      activities: [
        {
          name: 'Brooklyn Bridge',
          description: 'Walk across this iconic bridge connecting Manhattan and Brooklyn.',
          address: 'Brooklyn Bridge, New York, NY',
          type: 'TOURISTIC_ATTRACTION',
          date: '2024-09-29',
          time: '10:00',
          source: null
        },
        {
          name: 'DUMBO',
          description: 'Explore this trendy neighborhood known for its cobblestone streets and waterfront views.',
          address: 'DUMBO, Brooklyn, NY',
          type: 'TOURISTIC_ATTRACTION',
          date: '2024-09-29',
          time: '13:00',
          source: null
        }
      ]
    }
  ]
};