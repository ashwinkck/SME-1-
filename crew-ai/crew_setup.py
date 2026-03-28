from crewai import Crew
from agents import research_agent, analysis_agent, summary_agent
from tasks import research_task, analysis_task, summary_task

crew = Crew(
    agents=[
        research_agent,
        analysis_agent,
        summary_agent
    ],
    tasks=[
        research_task,
        analysis_task,
        summary_task
    ],
    verbose=True
)