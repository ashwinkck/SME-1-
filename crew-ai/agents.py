from dotenv import load_dotenv
load_dotenv()

from crewai import Agent
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="groq/llama-3.1-8b-instant",
    temperature=0.3
)
research_agent = Agent(
    role="Research Specialist",
    goal="Find accurate information about a topic",
    backstory="Expert researcher who gathers reliable information quickly.",
    llm="groq/llama-3.1-8b-instant",
    verbose=True
)

analysis_agent = Agent(
    
    role="Data Analyst",
    goal="Analyse the research findings and extract insights",
    backstory="A highly analytical expert who interprets complex information",
    llm="groq/llama-3.1-8b-instant",
    verbose=True
)
summary_agent = Agent(
    role="Teacher",
    goal = "explain the findings clearly for students",
    backstory = "An experienced educator who simplifies complex ideas",
    llm="groq/llama-3.1-8b-instant",
    verbose=True
)