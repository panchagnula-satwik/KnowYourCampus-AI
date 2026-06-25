# 🎓 KnowYourCampus AI

### **An AI-powered Academic Assistant built using Retrieval-Augmented Generation (RAG)**

Transform static college handbooks into an intelligent AI assistant capable of answering academic questions in natural language.

<p align="center">

<a href="https://knowyourcampus-ai.streamlit.app/">
<img src="https://img.shields.io/badge/🌐_Live_Demo-00C853?style=for-the-badge" />
</a>

<a href="https://github.com/panchagnula-satwik/KnowYourCampus-AI">
<img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github" />
</a>

</p>

<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>

<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>

<img src="https://img.shields.io/badge/Google_Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white"/>

<img src="https://img.shields.io/badge/RAG-Retrieval_Augmented_Generation-blueviolet?style=for-the-badge"/>

<img src="https://img.shields.io/badge/FAISS-Vector_Search-009688?style=for-the-badge"/>

<img src="https://img.shields.io/badge/Sentence_Transformers-NLP-orange?style=for-the-badge"/>

<img src="https://img.shields.io/badge/PDF-Document_AI-red?style=for-the-badge"/>

</p>

---

# 📖 Project Overview

Finding information inside lengthy academic handbooks can be frustrating. Students often spend valuable time searching through hundreds of pages to locate attendance rules, grading policies, examination regulations, placement guidelines, hostel rules, and other important information.

**KnowYourCampus AI** eliminates this problem by converting any college handbook into an intelligent AI-powered assistant.

The application combines **Retrieval-Augmented Generation (RAG)** with **semantic search** to understand the contents of uploaded PDF documents and answer user questions using only the relevant information from those documents.

Unlike traditional keyword search, the system understands the **meaning** behind a question, retrieves the most relevant sections using vector embeddings, and generates context-aware responses with **Google Gemini**.

The application is fully cloud-deployed using **Streamlit Community Cloud**, allowing users to upload any college handbook directly from their browser without installing additional software.

---

# ✨ Key Highlights

✅ Upload any college handbook or academic regulation PDF

✅ Automatically build a searchable AI knowledge base

✅ Semantic document search using FAISS vector indexing

✅ Context-aware question answering using Google Gemini

✅ Dynamic document processing (works with different colleges)

✅ Fully browser-based deployment using Streamlit Cloud

✅ Clean, responsive, and interactive web interface

---

> **"Upload once. Ask anything. Learn instantly."**

---

# 📸 Application Preview

## 🏠 Home Page

![Home](assets/home.png)

---

## 💬 AI-Powered Question Answering

![Answer](assets/answer.png)

---

## 📖 Retrieved Context

![Retrieved Context](assets/context.png)

---

# 🚀 Features

<table>
<tr>
<td width="50%">

### 📄 Dynamic PDF Upload

Upload any college handbook or academic regulation document directly through the web interface.

</td>

<td width="50%">

### 🧠 Semantic Search

Retrieves relevant information based on meaning rather than exact keyword matching using vector embeddings.

</td>
</tr>

<tr>
<td>

### 🤖 AI-Powered Responses

Google Gemini generates context-aware answers grounded in the uploaded handbook.

</td>

<td>

### ⚡ Instant Knowledge Base

Automatically extracts text, chunks documents, creates embeddings, and builds a searchable FAISS vector database.

</td>
</tr>

<tr>
<td>

### ☁️ Cloud Deployment

Accessible directly from any browser using Streamlit Community Cloud.

</td>

<td>

### 📚 Source Transparency

Displays the retrieved document context used to generate every response.

</td>
</tr>
</table>

---

# 🏗 System Architecture

```text
                    📄 User Uploads PDF
                             │
                             ▼
                 Text Extraction (PyPDF)
                             │
                             ▼
                  Intelligent Chunking
                             │
                             ▼
     SentenceTransformer Embedding Generation
                             │
                             ▼
               FAISS Vector Database
                             │
                             ▼
                Semantic Similarity Search
                             │
                             ▼
         Relevant Document Chunks Retrieved
                             │
                             ▼
           Google Gemini 2.5 Flash LLM
                             │
                             ▼
           Context-Aware AI Generated Answer
```

---

# 🔄 End-to-End Workflow

```text
            Upload College Handbook
                     │
                     ▼
              Extract PDF Text
                     │
                     ▼
            Split into Chunks
                     │
                     ▼
          Generate Vector Embeddings
                     │
                     ▼
             Store in FAISS Index
                     │
                     ▼
            User Asks a Question
                     │
                     ▼
      Retrieve Relevant Context Chunks
                     │
                     ▼
      Generate Answer using Gemini AI
                     │
                     ▼
        Display Answer + Source Context
```

---

# 🧠 How Retrieval-Augmented Generation (RAG) Works

Traditional Large Language Models answer questions using only their pre-trained knowledge. This often leads to hallucinations or outdated responses when asked about custom documents.

KnowYourCampus AI overcomes this limitation through **Retrieval-Augmented Generation (RAG)**.

Instead of sending the entire PDF directly to the language model, the application first retrieves the most relevant sections of the uploaded handbook using semantic similarity search.

Only those highly relevant document chunks are passed to **Google Gemini**, ensuring that every response is grounded in the uploaded document rather than relying on the model's general knowledge.

This approach provides:

- ✅ Higher answer accuracy
- ✅ Reduced hallucinations
- ✅ Faster response generation
- ✅ Document-specific reasoning
- ✅ Reliable academic information retrieval

---

# ⚙ AI Pipeline

| Stage | Technology |
|--------|------------|
| PDF Processing | PyPDF |
| Text Chunking | Python |
| Embedding Generation | Sentence Transformers |
| Vector Database | FAISS |
| Semantic Retrieval | Cosine Similarity Search |
| Language Model | Google Gemini 2.5 Flash |
| User Interface | Streamlit |
| Deployment | Streamlit Community Cloud |

---