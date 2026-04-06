from crewai import Agent
from langchain_groq import ChatGroq
from rag_setup import retriever
from crewai.tools import BaseTool
from dotenv import load_dotenv
load_dotenv()
import os

#1 Creating the LLM

llm = ChatGroq(
    model="groq/llama-3.1-8b-instant",
    temperature=0.3
)

#2 Creating a RAG tool
class StartupKnowledgeSearchTool(BaseTool):
    name:str = "startup_knowledge_search"
    description:str = "Search startup and technology knowledge base"

    def _run(self,query: str)-> str:
        docs = retriever.get_relevent_documents(query)
        context = "\n".join([doc.page_content for doc in docs])
        return context


#3 Creating the Tool Instance
startup_tool = StartupKnowledgeSearchTool()

market_oracle = Agent(
    role = "Market Oracle",
    goal=  "Understand market demand for startup ideas",
    backstory = "A legendary venture analyst who understands startup market and trends",
    tools=[startup_tool],
    llm = "groq/llama-3.1-8b-instant",
    verbose = True
) 

feature_architect = Agent(
    role = "Feature Architect",
    goal = "Design product features for startup ideas",
    backstory = "A product designer who turns ideas into real product features",
    tools=[startup_tool],
    llm = "groq/llama-3.1-8b-instant",
    verbose = True
)

tech_stack_architect = Agent(
    role = "Tech Stack Architect",
    goal = "Recommend technologies for building the product",
    backstory = "A senior software architect with deep knowledge of modern tech stacks",
    tools = [startup_tool],
    llm = "groq/llama-3.1-8b-instant",
    verbose = True
)

product_strategist = Agent(
    role = "Product Strategist",
    goal = "Create a complete product roadmap",
    backstory = "An experienced startup founder who plans product launches",
    tools = [startup_tool],
    llm = "groq/llama-3.1-8b-instant",
    verbose = True
)