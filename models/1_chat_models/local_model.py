from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# 1. Connect to your running llama.cpp server API
llm = ChatOpenAI(
    base_url="http://localhost:8080/v1",  # Connects directly to llama-server
    api_key="not-needed",                # Local server doesn't require a real key
    model="qwen2.5-1.5b",                # Can be any identifier string
    temperature=0.7
)

response = llm.invoke("what is ai engineering?")
print(response.content)



# # 2. Build a simple LangChain pipeline
# prompt = ChatPromptTemplate.from_template("Tell me a short joke about {topic}")
# chain = prompt | llm

# # 3. Invoke the pipeline
# response = chain.invoke({"topic": "programming language"})
# print(response.content)

