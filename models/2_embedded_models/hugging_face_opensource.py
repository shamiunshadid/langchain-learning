# -------------first approach-------------
from langchain_huggingface import HuggingFaceEmbeddings


embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text = "Bali is a place in Indonasia."

vector = embedding.embed_query(text)
print(str(vector))




# -----------second approach------------
# from langchain_huggingface import HuggingFaceEmbeddings

# # Point directly to your offline hard drive folder path
# local_model_path = r"D:\llm_models\all-MiniLM-L6-v2"

# embeddings_model = HuggingFaceEmbeddings(
#     model_name=local_model_path,
#     model_kwargs={'device': 'cpu'},
#     encode_kwargs={'normalize_embeddings': True}
# )

# # Test it completely offline!
# query_embedding = embeddings_model.embed_query("Test local folder loading")
# print("Successfully loaded model from D drive path!")
# print(f"Vector Dimensions: {len(query_embedding)}")