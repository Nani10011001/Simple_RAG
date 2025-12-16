# 📚 RAG Chatbot using LangGraph, LangChain & Groq

A **Retrieval-Augmented Generation (RAG)** based chatbot built with **LangGraph** and **LangChain**, using **Groq LLMs** for fast inference.  
The chatbot answers user queries **only from provided documents** (PDF / CSV), ensuring accurate and grounded responses.

---

## 🚀 Features

- 📄 Load documents (PDF / CSV)
- ✂️ Chunk & embed documents using HuggingFace embeddings
- 🧠 Store embeddings in **Chroma Vector Database**
- 🔎 Retrieve relevant context based on user query
- 🤖 Generate responses using **Groq LLM**
- 🕸️ Built with **LangGraph** for structured agent flow
- ❌ No hallucination – answers strictly from document data

---

## 🏗️ Tech Stack

| Layer | Technology |
|-----|-----------|
| LLM | Groq (LLaMA 3.1) |
| Agent Framework | LangGraph |
| Orchestration | LangChain |
| Embeddings | HuggingFace |
| Vector DB | Chroma |
| Language | Python |
| Environment | Python Virtual Environment |

---

## 📂 Project Structure


RAGChat/
│
├── data/
│   ├── sample.pdf
│   ├── data.csv
│
├── rag_agent/
│   ├── main.py
│   ├── graph.py
│   ├── retriever.py
│   └── tools.py
│
├── vectorstore/
│   └── chroma_db/
│
├── .env
├── requirements.txt
└── README.md
⚙️ Installation & Setup
1️⃣ Clone the repository

git clone https://github.com/your-username/rag-chatbot-langgraph.git
cd rag-chatbot-langgraph
2️⃣ Create & activate virtual environment
python -m venv .venv
windows:
.venv\Scripts\activate
3️⃣ Install dependencies
req.txt for the python things and the 
frontend dependecies 
npm i axios
npm i create vite@latest
(react)
backend dependecies

npm i express ,nodemon ,dotenv

4️⃣ Environment Variables

Create a .env file:
GROQ_API_KEY=your_groq_api_key_here
🧠 How It Works (RAG Flow)

📄 Load documents (PDF / CSV)

✂️ Split documents into chunks

🔢 Convert chunks into embeddings

🗄️ Store embeddings in Chroma DB

🔍 Retrieve relevant chunks for user query

🤖 Pass context + question to Groq LLM

✅ Generate accurate answer from documents only

🧪 Example Query:
User: What is the climate of Chennai?
Bot: Chennai has an average temperature of 28.5°C with high humidity
and moderate rainfall, based on the provided dataset.
🧩 Key Concepts Used

Retrieval-Augmented Generation (RAG)

Vector Similarity Search

LangGraph Nodes & Edges

Tool-based Retrieval

Stateless Chat (for now)

---

### 🔥 Want next?
If you want, I can:
- 🔹 Rewrite this README **for recruiters**
- 🔹 Add **architecture diagram (ASCII or image)**
- 🔹 Make a **frontend + backend README**
- 🔹 Create a **memory-enabled RAG README**
- 🔹 Optimize it for **internship/job shortlisting**

Just tell me 👍
