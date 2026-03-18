import os
from dotenv import load_dotenv
from google.genai import Client

# Load API key
load_dotenv()

client = Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_answer(question, retrieved_chunks):

    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
You are a strict academic assistant.

ONLY answer using the provided context.

If the answer is NOT clearly present in the context, say:
"I don't have enough information to answer this question."

Do NOT guess.
Do NOT add extra information.

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    return response.text