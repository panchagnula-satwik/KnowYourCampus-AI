import os
import streamlit as st
from dotenv import load_dotenv
from google.genai import Client

# ---------------------------------------------------------
# Load API Key
# Priority:
# 1. Streamlit Secrets (Cloud Deployment)
# 2. Local .env file (Development)
# ---------------------------------------------------------

try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

client = Client(api_key=api_key)


def generate_answer(question, retrieved_chunks):
    """
    Generates an answer using the retrieved document chunks.
    """

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

    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"""
⚠️ Unable to generate an AI response.

Possible reasons:
• Gemini API quota exceeded
• Invalid API key
• Internet connection issue
• Temporary Google API outage

Error:
{str(e)}
"""