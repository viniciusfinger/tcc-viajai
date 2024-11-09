from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

# DEPRECATED
# A versão com ChatOpenAI usando o modelo gpt-4o-mini está performando melhor e trazendo mais resultados.
llm = OpenAI()

prompt_template = PromptTemplate.from_template("""
Return a list of the main tourist attractions of {location}.
""")

location_prompt = prompt_template.format(location="Toronto")

response = llm.invoke(location_prompt)

print(response)