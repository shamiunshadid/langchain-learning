from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimension=32)


# single text or document
response = embedding.embed_query("Dhaka is the capital of Bangladesh.")


# multiple
docs = [
    "Dhaka is the capital of Bangladesh",
    "Paris is the capital of France",
    "Bali is a place in Indonasia"
]

multiresponse = embedding.embed_documents(docs)


print(str(response, multiresponse))
