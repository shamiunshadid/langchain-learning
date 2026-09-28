from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b")

messages = [
    SystemMessage(content="You are a helpful assistant! Your name is Bob."),
]

while True:
    user_message = input("You: ")
    
    if user_message == "exit":
        break
    
    messages.append(HumanMessage(content=user_message))
    
    result = model.invoke(messages)

    messages.append(AIMessage(content=result.content))
    
    print("AI: ", result.content)
    
print(messages)
