from config import llm
from langchain.prompts import ChatPromptTemplate

def make_itinerary(start_date: str, end_date: str, destination: str, touristic_points: str, events: str):
    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You're a helpful travel agent helping a customer plan a trip, you make a itinerary day by day using the data provided by the customer."),
            ("human", """
            Do a itinerary to {destination}, between {start_date} and {end_date}. The touristic points I want to visit are {touristic_points} and the events are {events}.
            """)
        ]
    )
    
    prompt = prompt_template.format(destination=destination, start_date=start_date, end_date=end_date, touristic_points=touristic_points, events=events)
    
    return llm.invoke(prompt).content
    
    