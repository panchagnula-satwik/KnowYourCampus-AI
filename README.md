# 🎓 KnowYourCampus AI

An AI-powered assistant that answers college academic and policy-related queries using Retrieval-Augmented Generation (RAG).

---

## 🚀 Overview

KnowYourCampus AI allows students to upload their college handbook and ask questions in natural language.
The system retrieves relevant information from the document and generates accurate answers using AI.

---

## 🧠 Features

* 📄 Upload any college handbook (PDF)
* 🔍 Semantic search using embeddings
* 🤖 AI-powered answers using Gemini
* 🧾 Source-based responses (no hallucination)
* ⚡ Fast retrieval using FAISS
* 🌐 Interactive UI using Streamlit

---

## 🏗️ Architecture

```
User Upload PDF
      ↓
Ingestion (Text Extraction)
      ↓
Chunking
      ↓
Embeddings (MiniLM)
      ↓
FAISS Vector Store
      ↓
Retriever
      ↓
Gemini (LLM)
      ↓
Final Answer
```

---

## 🛠️ Tech Stack

* Python
* Streamlit
* FAISS
* Sentence Transformers (all-MiniLM-L6-v2)
* Google Gemini API
* PyPDF

---

## 📂 Project Structure

```
Know Your Campus/
│
├── app/
│   └── app.py
│
├── src/
│   ├── ingest.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── retriever.py
│   └── rag_pipeline.py
│
├── data/
│   ├── raw_pdfs/
│   └── processed/
│
├── vectorstore/
│
├── .env.example
├── requirements.txt
├── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd KnowYourCampus
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Add API Key

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

---

### 4. Run the app

```bash
streamlit run app/app.py
```

---

## 🧪 How It Works

1. Upload your college handbook PDF
2. Click **"Build Knowledge Base"**
3. Ask questions like:

   * What is attendance requirement?
   * How many credits are needed?
4. Get accurate AI-generated answers

---

## 🚫 Hallucination Control

The system strictly answers only from provided context.
If information is not available, it responds:

> "I don't have enough information to answer this question."

---

## 📌 Future Improvements

* Multi-document support
* Chat history
* Deployment (Streamlit Cloud)
* Voice input

---

## 👨‍💻 Author

**Satwik Panchagnula**

---

## ⭐ If you like this project, give it a star!