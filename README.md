# Huggingface

# 🧠 RAG Chatbot Demo

A simple AI chatbot powered by GPT-2 using Hugging Face's `transformers` library and Flask. It supports contextual Q&A using retrieval-augmented generation (RAG) techniques.

---

## 🚀 Features

- Frontend chat interface built with HTML/CSS/JS
- Flask backend with endpoints for:
  - `/chat`: Generate answers
  - `/train`: Train document embeddings (retrieval)
  - `/history`: View previous chat history
- Uses GPT-2 (`gpt2` model from Hugging Face) for generating responses

---

## 🏗️ Tech Stack

| Layer      | Technology            |
|------------|------------------------|
| Frontend   | HTML, CSS, JavaScript |
| Backend    | Flask (Python)        |
| AI Model   | GPT-2 via Hugging Face Transformers |
| Retriever  | Custom `retriever.py` logic using embeddings |
| Storage    | Python file or memory-based history (`chat_history.py`) |

---

## 📦 Requirements

Install the following Python libraries:

```bash
pip install flask transformers huggingface_hub

To run the project start python main.py
and run index.html


🧠 Model Details
Model: gpt2

Type: Causal Language Model

Provider: Hugging Face

Agent Type: Stateless text-generation via Transformers Pipeline

This model is not instruction-tuned. For better results, consider using mistralai/Mistral-7B-Instruct or gpt-3.5-turbo.
