from config import llm
from langchain.prompts import ChatPromptTemplate

#TODO: Adicionar um few shot prompt template aqui
#TODO: deve ser formatado para JSON
#TODO: Melhorar o prompt para inserir melhor os eventos entre os dias e a disposição dos eventos.
def make_itinerary(start_date: str, end_date: str, destination: str, touristic_points: str, events: str):
    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You're a helpful travel agent helping a customer plan a trip, you make a itinerary day by day using the data provided by the customer."),
            ("human", """
            I'm going to visit {destination}, between {start_date} and {end_date}.
            Do a itinerary for me, please.
            The touristic points I want to visit are {touristic_points} and the events I have interest are {events}.
            Organize this touristitcs points and events between days, considering the time I have to visit each place.
            When are an event, insert [EVENT] tag.
            """)
        ]
    )
    
    prompt = prompt_template.format(destination=destination, start_date=start_date, end_date=end_date, touristic_points=touristic_points, events=events)
    
    return llm.invoke(prompt).content
    
    