from groq import Groq
client = Groq(api_key="api_key")
messages = []
while True:
    user_input = input("You :")
    messages = [
        {"role":"system",
         "content":"you are a senior software engineer. you explain code clearly,fix bugs, and generate clean python functions"}
    ]
    messages.append({"role":"user","content":user_input})
    response = client.chat.completions.create(
    model ="llama-3.1-8b-instant",
    messages=messages
 
)
    reply = response.choices[0].message.content
    print("Ai:", reply)