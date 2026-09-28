from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b")


# schema
class Review(TypedDict):
    
    summery: Annotated[str, "A brief summery of the review"]
    sentiment: Annotated[str, "A sentiment of the review, either positive or negetive or neutral"]
    
    
structured_mode = model.with_structured_output(Review)

result = structured_mode.invoke("""The hardware is great but the software feels bloted. There are too many pre installed apps that I can't remove. Also the ui looks outdated compare to other brands.""")

print(result)
