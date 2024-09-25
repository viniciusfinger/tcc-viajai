from config import llm
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.agent_toolkits.load_tools import load_tools


# TODO: Melhorar para buscar mais resultados, talvez pesquisar no google?
def fetch_events(start_date, end_date, destination):
    few_shot_prompt = """
    You are an expert travel assistant. Given a destination and travel period, you return a list of events happening at that place during the specified time frame.

    Example 1:
    Input: "I'm going to travel to Paris between 2023-07-01 and 2023-07-10. Return a list of events that occur during that period."
    Output: 
    [
        {
            "name": "Bastille Day Parade",
            "description": "A grand parade on the Champs-Élysées celebrating Bastille Day.",
            "date": "2023-07-14"
        },
        {
            "name": "Paris Jazz Festival",
            "description": "A jazz music festival held at Parc Floral.",
            "date": "2023-07-03"
        }
    ]

    Example 2:
    Input: "I'm going to New York City between 2023-12-01 and 2023-12-15. Return a list of events that occur during that period."
    Output:
    [
        {
            "name": "Christmas Tree Lighting at Rockefeller Center",
            "description": "An iconic holiday event with a massive Christmas tree lighting ceremony.",
            "date": "2023-12-05"
        },
        {
            "name": "Winter Village at Bryant Park",
            "description": "An open-air holiday market and ice-skating rink at Bryant Park.",
            "date": "2023-12-02"
        }
    ]

    Now, for the following query:
    """

    query = few_shot_prompt + f"I'm going to travel to {destination} between {start_date} and {end_date}. Return a list of events that occur during that period with name, description, and date in JSON format."

    tools = load_tools(['ddg-search', 'wikipedia'], llm=llm)
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, prompt=prompt, tools=tools)
    
    agent_executor = AgentExecutor(agent=agent, tools=tools, prompt=prompt, verbose=True)

    return agent_executor.invoke({"input": query})

