# ViajAI - AI-Powered Personalized Travel Itineraries 🗺️

ViajAI is an artificial intelligence system designed to automate the creation of personalized and detailed travel itineraries. Developed as a final project (TCC) for the Computer Science degree at La Salle University (Brazil), ViajAI leverages state-of-the-art AI to deliver tailored travel plans based on user preferences and real-time data.

---

## Overview

ViajAI combines natural language processing, retrieval-augmented generation (RAG), and real-time data integration to generate engaging, accurate, and highly personalized travel itineraries. The system is built with a modular architecture, featuring a Python backend powered by OpenAI's GPT models and a modern Angular frontend.

## Architecture

ViajAI leverages a multi-agent architecture built with LangGraph, enabling parallel processing and efficient orchestration of specialized agents. Each agent is responsible for a specific aspect of the itinerary generation process, such as fetching events, identifying touristic attractions, or assembling the final travel plan. This design allows for concurrent data retrieval and reasoning, significantly improving performance and scalability.

The system also implements the ReAct (Reasoning + Acting) paradigm, where agents iteratively reason about the current state and take actions (e.g., querying external sources, updating the itinerary) to achieve the best possible outcome. This approach enhances the system's ability to dynamically adapt to user preferences and real-time information, resulting in more relevant and coherent travel recommendations.

### Main Agents

- **Events Fetcher Agent (`events_fetcher_agent.py`)**: Responsible for retrieving up-to-date local events relevant to the user's travel destination and dates, enriching the itinerary with unique experiences.
- **Touristic Attractions Agent (`touristic_attractions_agent.py`)**: Identifies and selects the most suitable touristic attractions based on user interests, preferences, and destination specifics.
- **Travel Itinerary Maker Agent (`travel_itinerary_maker_agent.py`)**: Orchestrates the information gathered by the other agents, assembling a coherent, day-by-day travel plan tailored to the user's profile.

## Features

- **AI-Powered Itinerary Generation**: Uses OpenAI's GPT models for natural language travel planning.
- **Retrieval-Augmented Generation (RAG)**: Enriches responses with up-to-date information from DuckDuckGo and Wikipedia.
- **Flexible User Input**: Accepts diverse prompts to customize itineraries based on preferences, interests, and destinations.
- **Real-Time Data Integration**: Fetches current information to ensure relevant and accurate recommendations.
- **Interactive Experience**: Delivers engaging, informative, and adaptable trip plans for all traveler profiles.

## Tech Stack

- **Backend**: Python, FastAPI (or Flask), OpenAI API
- **Frontend**: Angular
- **Data Sources**: DuckDuckGo, Wikipedia

## Project Structure

```
tcc-viajai/
  ├── backend/         # Python backend (AI, controllers, services)
  ├── frontend/        # Angular frontend
  ├── docs/            # Documentation
  └── proof of concept/ # Early prototypes and experiments
```

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/viniciusfinger/tcc-viajai.git
cd tcc-viajai
```

### 2. Backend Setup
```bash
cd backend
pip install -r requirements.txt
python3 main.py
```

### 3. Frontend Setup
```bash
cd ../frontend
npm install
ng serve
```

The backend will run on the default Python port (e.g., 8000) and the frontend on Angular's default (e.g., 4200).

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements, bug fixes, or new features.

## License

This project is for academic purposes. For other uses, please contact the author.

---

Developed by Vinícius Finger as a final project for La Salle University (Brazil).
