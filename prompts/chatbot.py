
# ------------v2--------------
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












## ------------v1-------------
# import os
# from langchain_groq import ChatGroq
# # from langchain_core.prompts import PromptTemplate, load_prompt
# from dotenv import load_dotenv


# load_dotenv()

# if not os.getenv("GROQ_API_KEY"):
#     raise RuntimeError("GROQ_API_KEY is missing. Add it to .env or your environment.")

# model = ChatGroq(
#     model="openai/gpt-oss-20b",
#     temperature=0,
# )

# chat_history = []

# while True:
#     user_input = input("You: ")
#     chat_history.append(user_input)
#     if user_input == 'exit':
#         break
#     llm_resul = model.invoke(chat_history)
#     chat_history.append(llm_resul)
#     print("AI: ",llm_resul.content)
