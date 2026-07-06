# 🤖 RAG Chatbot using Python, LangChain & Groq

## 📌 Project Overview

This project is a Retrieval-Augmented Generation (RAG) chatbot built using Python. It answers user questions by retrieving relevant information from PDF documents and generating accurate responses using the Groq API and LangChain.

## ✨ Features

* 📄 Extracts text from PDF documents
* ✂️ Splits text into smaller chunks
* 🧠 Generates embeddings for semantic search
* 💾 Stores embeddings in ChromaDB
* 🔍 Retrieves relevant document chunks
* 🤖 Uses Groq LLM to generate intelligent answers
* 💬 Simple and interactive chatbot interface

## 🛠️ Technologies Used

* Python
* LangChain
* Groq API
* ChromaDB
* PyPDF
* Sentence Transformers

## 📂 Project Structure

* `app.py` – Main chatbot application
* `extract.py` – Extracts text from PDF
* `chunks.py` – Splits text into chunks
* `embedding.py` – Creates embeddings
* `requirements.txt` – Project dependencies
* `sample.pdf` – Sample document

## 🚀 Installation

```bash
git clone https://github.com/your-username/RAG-Chatbot.git
cd RAG-Chatbot
pip install -r requirements.txt
```

Create a `.env` file and add your Groq API key:

```text
GROQ_API_KEY=your_api_key
```

Run the application:

```bash
python app.py
```

## 📖 How It Works

1. Load a PDF document.
2. Extract and split the text into chunks.
3. Generate embeddings.
4. Store embeddings in ChromaDB.
5. Ask questions about the document.
6. Retrieve relevant content and generate answers using Groq.

## 👩‍💻 Author

**Deepika Rahangdale**
