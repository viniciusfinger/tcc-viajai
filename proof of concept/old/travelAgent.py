from langchain import hub
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_community.agent_toolkits.load_tools import load_tools
import bs4

llm = ChatOpenAI(model="gpt-3.5-turbo")

query = """
I'm going to travel to London in August 2024. 
I want you to make a travel itinerary of 7 days for me with events that will occurs on that date 
and the price of the ticket from São Paulo to London.
"""


def researchAgent(query, llm):
    """
    Create a research agent that will search for information about the query
    """
    
    tools = load_tools(['ddg-search', 'wikipedia'], llm=llm)
    
    prompt = hub.pull("hwchase17/react")
    
    agent = create_react_agent(llm=llm, prompt=prompt, tools=tools)
    agent_executor = AgentExecutor(agent=agent, tools=tools, prompt=prompt, verbose=True)

    web_context = agent_executor.invoke({"input": query})
    return web_context['output']


def loadData():
    """
    Load data from the dicasdeviagem.com using RAG (Retrieval- Augmented Generation)
    """
    loader = WebBaseLoader(
        web_paths=("https://www.dicasdeviagem.com/inglaterra/",),
        bs_kwargs=dict(parse_only=bs4.SoupStrainer(class_=("postcontentwrap", "pagetitleloading background-imaged loading-dark"))),
    )
    
    documents = loader.load()
    
    # Chunk size = doc size in tokens, Chunk overlap = how many tokens overlap between chunks 
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(documents)
    
    vector_store = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())
    
    retriever = vector_store.as_retriever()
    return retriever


def getRelevantDocs(query):
    """
    Get the most relevant documents based on query
    """
    retriever = loadData()
    return retriever.invoke(query)


def supervisorAgent(query, llm, web_context, relevant_documents):
    prompt_template = """
    You are a manager at a travel agency. Your final answer should be a complete and detailed travel itinerary. Use the context of events and ticket prices, user input and relevant documents to develop the itinerary.
    Context: {web_context}
    Relevant documents: {relevant_documents}
    User: {query}
    Assistant:
    """
    
    prompt = PromptTemplate(
        input_variables= ['web_context', 'relevant_documents', 'query'],
        template=prompt_template
    )
    
    sequence = RunnableSequence(prompt | llm)
    
    return sequence.invoke({"web_context": web_context, "relevant_documents": relevant_documents, "query": query})
    
    
def getResponse(query, llm):
    web_context = researchAgent(query, llm)
    relevant_documents = getRelevantDocs(query)
    print(relevant_documents)
    return supervisorAgent(query, llm, web_context, relevant_documents)
    

print("- - - - - - - - - - - - - - - - ")
print(getResponse(query, llm).content)