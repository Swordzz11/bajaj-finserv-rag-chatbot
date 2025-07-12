# bajaj-finserv-rag-chatbot
# 🤖 Bajaj Finserv RAG Chatbot

A hybrid Retrieval-Augmented Generation (RAG) chatbot that can answer queries about:

- 📈 **Stock prices** from CSV (e.g., highest/average/lowest by month)
- 🧾 **Earnings call transcripts** (e.g., Allianz stake sale, Hero partnership, BAGIC performance)

Built using **FastAPI**, **LangChain**, **OpenAI/Gemini**, and **ChromaDB**.

---

## 🔧 Tech Stack

| Layer           | Tech                                |
|-----------------|-------------------------------------|
| 💬 LLM           | OpenAI GPT-3.5 / Gemini Pro (fallback) |
| 🔍 Embeddings    | Sentence Transformers + Gemini      |
| 📦 Vector DB     | ChromaDB                            |
| 🧠 Framework     | LangChain                           |
| 🖥 Frontend      | FastAPI + Jinja2 HTML                |
| 🛠 Deployment     | Local (uvicorn) / Cloud via Render  |

---

## 📁 Project Structure


Bajaj Finserv/
│
├── app.py # Main FastAPI app
├── requirements.txt # Python dependencies
├── .env # API keys (OpenAI & Gemini)
├── data/
│ └── BFS_Share_Price.csv # Stock data
│
├── scripts/
│ ├── query_engine.py # Agent + tools setup
│ ├── stock_tools.py # Stock data functions
│ ├── transcript_qa.py # Transcript RAG logic
│ └── init.py # Makes it a module
│
├── templates/
│ └── index.html # Chat UI

---

## 🚀 Features

- 📊 Stock price Q&A from structured CSV
- 📄 Transcript Q&A using vector search + Gemini/OpenAI
- 🔁 LLM Fallback (OpenAI → Gemini if quota exhausted)
- 🔐 `.env`-based secure config
- 🌐 Simple HTML interface via FastAPI

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/Swordzz11/bajaj-finserv-rag-chatbot.git
cd bajaj-finserv-rag-chatbot
OPENAI_API_KEY=your_openai_key
GEMINI_API_KEY=your_gemini_key
