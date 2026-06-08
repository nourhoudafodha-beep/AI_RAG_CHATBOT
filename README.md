# 📚 Sup'Com AI Study Assistant (LLM + RAG)

An intelligent AI-powered chatbot designed to help Sup'Com students better understand their course materials. The chatbot uses **Retrieval-Augmented Generation (RAG)** and **Large Language Models (LLMs)** to generate summaries, explain difficult concepts, and answer questions based on uploaded documents.

---

## 🚀 Project Overview

Traditional chatbots rely only on the knowledge embedded in their language models, which may not contain institution-specific information.

This project overcomes this limitation by implementing a **RAG (Retrieval-Augmented Generation)** pipeline that retrieves relevant information from Sup'Com course documents before generating an answer.

The assistant can:

- 📄 Summarize lecture notes and PDFs
- 💡 Explain complex concepts in simple terms
- ❓ Answer questions from course materials
- 🔍 Search semantically through documents
- 🎓 Assist students during revision and exam preparation

---

# 🏗️ System Architecture

```
                 PDF Documents
                       │
                       ▼
              Text Extraction
                       │
                       ▼
             Text Chunking Process
                       │
                       ▼
          Embedding Generation Model
                       │
                       ▼
          FAISS Vector Database Index
                       │
                       ▼
          Semantic Similarity Search
                       │
                       ▼
            Retrieved Relevant Chunks
                       │
                       ▼
               LLM (Llama 3 / Mistral)
                       │
                       ▼
            Intelligent Final Response
```

---

# 🛠️ Technologies Used

- Python
- LangChain
- FAISS
- Sentence Transformers
- Ollama
- Llama 3
- Streamlit
- PyPDF
- HuggingFace Embeddings

---

# 📂 Project Structure

```
AI_RAG_CHATBOT/

│
├── data/
│      course1.pdf
│      course2.pdf
│      notes.pdf
│
├── vector_db/
│      FAISS Index
│
├── build_index.py
├── chatbot.py
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Methodology

## Step 1 — Data Collection

Course materials are collected from Sup'Com lecture notes in PDF format.

Example:

- Communication Networks
- Signal Processing
- Artificial Intelligence
- Cybersecurity
- Embedded Systems

---

## Step 2 — Document Loading

All PDF files are automatically loaded using PyPDFLoader.

The extracted text is converted into LangChain Documents.

```
PDF → Raw Text
```

---

## Step 3 — Text Chunking

Large documents are divided into smaller chunks to improve retrieval quality.

Parameters:

- Chunk Size: 500 characters
- Overlap: 50 characters

```
Long PDF

↓

Chunk 1

Chunk 2

Chunk 3

Chunk 4
```

---

## Step 4 — Embedding Generation

Each chunk is transformed into a dense numerical vector using:

```
sentence-transformers/all-MiniLM-L6-v2
```

Example:

```
"The internship lasts one month"

↓

[0.23, -0.81, 0.17, ...]
```

These embeddings capture semantic meaning instead of simple keywords.

---

## Step 5 — Vector Database Construction

The generated embeddings are stored inside a FAISS vector database.

The vector index allows efficient semantic retrieval even with hundreds of documents.

```
Chunk

↓

Embedding

↓

FAISS Index
```

---

## Step 6 — User Query Processing

The user asks a question through the chatbot interface.

Example:

```
"What is supervised learning?"
```

The same embedding model converts the question into a vector.

---

## Step 7 — Semantic Search

FAISS compares the query vector with all stored document vectors and retrieves the most relevant chunks.

```
Question

↓

Vector Search

↓

Top-k Similar Chunks
```

---

## Step 8 — Context Construction

The retrieved chunks are concatenated into a context that will be provided to the LLM.

```
Retrieved Chunks

↓

Context
```

---

## Step 9 — Response Generation

The LLM receives:

- User Question
- Retrieved Context

and generates a natural language answer grounded in the retrieved documents.

```
Question

+

Retrieved Context

↓

LLM

↓

Answer
```

---

## Step 10 — Display the Answer

The chatbot returns:

- A summarized answer
- A detailed explanation
- Information extracted from course documents

through a Streamlit web interface.

---

# 💻 Features

- PDF Document Analysis
- Automatic Text Summarization
- AI-based Course Explanation
- Semantic Search
- Question Answering
- RAG Pipeline
- Streamlit Interface
- Local LLM Inference with Ollama

---

# 🔄 Workflow

```
Load PDFs
      │
      ▼
Extract Text
      │
      ▼
Chunk Documents
      │
      ▼
Generate Embeddings
      │
      ▼
Create FAISS Index
      │
      ▼
User Question
      │
      ▼
Similarity Search
      │
      ▼
Retrieve Context
      │
      ▼
LLM Generation
      │
      ▼
Final Answer
```

---

# 🎯 Future Improvements

- Conversation Memory
- Citation of Source Documents
- Multilingual Support (English, French, Arabic)
- Voice Input and Speech Synthesis
- Upload New Documents from the Interface
- Hybrid Search (BM25 + Vector Search)
- User Authentication
- Chat History
- PDF Export of Answers

---

# 📖 Educational Objective

The main goal of this project is to demonstrate the integration of **Generative AI**, **Natural Language Processing**, **Vector Databases**, and **Retrieval-Augmented Generation (RAG)** into an intelligent educational assistant that helps Sup'Com students understand and review their courses more effectively.

---

## 👩‍💻 Author

**Nour Houda**

Communication Engineering Student at Sup'Com

Interested in:
- Artificial Intelligence
- Machine Learning
- Large Language Models
- Computer Vision
- NLP
- Embedded AI
- Data Science
