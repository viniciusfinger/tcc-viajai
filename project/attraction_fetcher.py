from config import llm
from langchain.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate

# TODO: Usar um formatter ao invés de pedir no prompt
# TODO: Pensar em um nome melhor pra esse módulo
# TODO: Na engenharia de prompt, adicionar uma parte para ignorar eventos que ocorrem apenas em uma determinada
#época, como no caso de canoas, que está retornando a feira do livro.
def fetch_in_gpt_by_location(location: str):
    examples = [
    {
        "location": """
            The customer asks you to recommend some tourist attractions in the area.
            Return a list with at least 10 locations of the main tourist attractions of Toronto in JSON format.
            Make sure the response is correctly formatted with JSON. 
        """,
        "response": '''
        [
            {{
                "name": "CN Tower",
                "description": "One of the tallest freestanding structures in the world, the CN Tower offers breathtaking views of the city from its observation deck and a glass floor."
            }},
            {{
                "name": "Royal Ontario Museum",
                "description": "A world-renowned museum that features a diverse collection of art, culture, and nature, including dinosaur fossils and ancient artifacts."
            }}
        ]
        '''
    },
    {
        "location": """
            The customer asks you to recommend some tourist attractions in the area.
            Return a list with at least 10 locations of the main tourist attractions of New York in JSON format.
            Make sure the response is correctly formatted with JSON. 
        """,
        "response": '''
        [
            {{
                "name": "Statue of Liberty",
                "description": "An iconic symbol of freedom, the Statue of Liberty stands tall on Liberty Island and offers tours that provide stunning views of New York City."
            }},
            {{
                "name": "Central Park",
                "description": "A large public park in the middle of Manhattan, perfect for outdoor activities, relaxation, and iconic landmarks like the Central Park Zoo and Bethesda Terrace."
            }}
        ]
        '''
    }]

    example_prompt = ChatPromptTemplate.from_messages(
        [
            ("human", "{location}"),
            ("ai", "{response}"),
        ]
    )
    
    few_shot_prompt_template = FewShotChatMessagePromptTemplate(
        example_prompt=example_prompt,
        examples=examples,
        input_variables=["location"]
    )
    
    prompt_tempalte = ChatPromptTemplate.from_messages(
        [
            ("system", "ou are helpful travel agent helping a customer plan a trip."),
            few_shot_prompt_template,
            ("human", """
            The customer asks you to recommend some tourist attractions in the area.
            Return a list with at least 10 locations of the main tourist attractions of {location} in JSON format.
            Make sure the response is correctly formatted with JSON. 
            """)
        ]
    )

    prompt = prompt_tempalte.format(location=location)
    
    return llm.invoke(prompt).content