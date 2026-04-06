from crew_setup import product_crew
idea = input("Enter your startup idea:")
result = product_crew.kickoff(inputs={"idea":idea})
print(result)