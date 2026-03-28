from crewai import Task
from agents import research_agent, analysis_agent, summary_agent

research_task = Task(
    description="Research the topic:{topic}.Collect important facts and explanations",
    expected_output="A detailed research report with key facts about the topic.",
    agent=research_agent
)

analysis_task = Task(
    description="Analyse the research findings and identify the key insights.",
    expected_output="A list of important insights derived from the research.",
    agent=analysis_agent
)

summary_task = Task(
    description="Explain the insights in a simple way that students can understand",
    expected_output="A simple explanation that students can easily understand.",
    agent=summary_agent
)