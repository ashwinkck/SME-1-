from crew_setup import crew
topic = input("Enter a topic: ")
result = crew.kickoff(
    inputs={"topic":topic}
)
print("\n FINAL RESULT:\n")
print(result)