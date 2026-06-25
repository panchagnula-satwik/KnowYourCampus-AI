import sys
import os
import subprocess

# Fix import paths
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.retriever import retrieve
from src.rag_pipeline import generate_answer

st.set_page_config(page_title="KnowYourCampus AI")

st.title("🎓 KnowYourCampus AI")
st.write("Upload your college handbook and ask questions about it.")

# -----------------------------
# SESSION STATE
# -----------------------------

if "db_ready" not in st.session_state:
    st.session_state.db_ready = False

# -----------------------------
# FILE UPLOAD
# -----------------------------

uploaded_file = st.file_uploader(
    "Upload your college handbook (PDF)",
    type="pdf"
)

if uploaded_file is not None:

    save_folder = "data/raw_pdfs"
    os.makedirs(save_folder, exist_ok=True)

    file_path = os.path.join(save_folder, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("PDF uploaded successfully!")

# -----------------------------
# BUILD KNOWLEDGE BASE
# -----------------------------

if uploaded_file is not None:

    if st.button("Build Knowledge Base"):

        with st.spinner("Processing document... ⏳"):

            subprocess.run([sys.executable, "src/ingest.py"], check=True)
            subprocess.run([sys.executable, "src/chunking.py"], check=True)
            subprocess.run([sys.executable, "src/embeddings.py"], check=True)

        st.session_state.db_ready = True
        st.success("Knowledge base ready! ✅")

# -----------------------------
# QUESTION SECTION
# -----------------------------

st.divider()
st.subheader("Ask a question")

question = st.text_input("Enter your question:")

if not st.session_state.db_ready:
    st.warning("⚠️ Please upload a PDF and build the knowledge base first.")
else:
    if st.button("Ask"):

        if question.strip() != "":

            with st.spinner("Thinking... 🤖"):

                retrieved_chunks = retrieve(question)
                answer = generate_answer(question, retrieved_chunks)

            st.subheader("Answer")
            st.write(answer)

            # Show sources
            st.subheader("Source Document")
            st.write("Answer derived from uploaded handbook")

            with st.expander("See retrieved context"):
                for chunk in retrieved_chunks:
                    st.write(chunk)