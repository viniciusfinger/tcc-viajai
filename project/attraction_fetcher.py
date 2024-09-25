from config import llm
from langchain.prompts import ChatPromptTemplate

# TODO: ESSE FEW SHOT ESTÁ ERRADO, NÃO ESTÁ USANDO FewShotPromptTemplate, refatorar
# TODO: Usar um formatter ao invés de pedir no prompt
# TODO: Pensar em um nome melhor pra esse módulo
# TODO: Na engenharia de prompt, adicionar uma parte para ignorar eventos que ocorrem apenas em uma determinada
#época, como no caso de canoas, que está retornando a feira do livro.
def fetch_in_gpt_by_location(location: str):
    examples = [
    {
        "location": "Toronto",
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
        "location": "New York",
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

    example_template = '''
    Location: {location}
    Response: {response}
    '''

    few_shot_examples = "\n".join(
        example_template.format(location=ex["location"], response=ex["response"]) for ex in examples
    )

    prompt_template = ChatPromptTemplate.from_template(few_shot_examples + """
    You are a travel agent helping a customer plan a trip to {location}. 
    The customer asks you to recommend some tourist attractions in the area.
    Return a list with at least 10 locations of the main tourist attractions of {location} in JSON format.

    Make sure the response is correctly formatted with JSON.
    """)

    location_prompt = prompt_template.format(location=location)

    return llm.invoke(location_prompt).content