
import os

from langchain_groq import ChatGroq
from dotenv import load_dotenv


load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    raise RuntimeError("GROQ_API_KEY is missing. Add it to .env or your environment.")

model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
)

response = model.invoke("What is AI engineering? Explain it in one sentence.")
print(response.content)



# ----------- models available in groq -------------
# whisper-large-v3
# openai/gpt-oss-20b
# openai/gpt-oss-safeguard-20b
# qwen/qwen3.8-27b
# meta-llama/llama-prompt-guard-2-86m
# meta-llama/llama-prompt-guard-2-22m
# canopylabs/orpheus-arabic-saudi
# whisper-large-v3-turbo
# openai/gpt-oss-120b
# canopylabs/orpheus-v1-english
# allam-2-7b