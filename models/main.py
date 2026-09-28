from dotenv import load_dotenv
from groq import Groq

load_dotenv()

print('\n'.join(model.id for model in Groq().models.list().data))