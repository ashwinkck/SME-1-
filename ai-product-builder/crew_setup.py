from crewai import Crew
from agents import market_oracle,feature_architect, tech_stack_architect, product_strategist
from tasks import market_task,feature_task,tech_task,strategy_task
product_crew = Crew(
    agents=[
        market_oracle,
        feature_architect,
        tech_stack_architect,
        product_strategist
    ],
    tasks=[
        market_task,
        feature_task,
        tech_task,
        strategy_task
    ],
    verbose=True
)