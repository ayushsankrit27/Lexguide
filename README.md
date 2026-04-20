# ⚖️ LexGuide — Indian Legal Awareness Assistant

An Agentic AI system that delivers plain-language legal awareness to Indian citizens using **RAG, LangGraph, and live web search.**

## 📌 Overview

LexGuide is an AI-powered legal awareness assistant designed to help Indian citizens understand their legal rights in simple language.

It provides **actionable awareness, not legal advice**, by combining:

- Retrieval-Augmented Generation (RAG)
- LangGraph Agent Workflow
- ChromaDB Vector Search
- Live Web Search (DuckDuckGo)
- Self-Reflection / Hallucination Checking
- Streamlit Chat Interface

---

## 🚀 Features

- ✅ 12-document legal knowledge base
- ✅ 8-node LangGraph agent pipeline
- ✅ Intelligent query routing
- ✅ Live legal web search
- ✅ Conversation memory
- ✅ Automatic faithfulness evaluation (RAGAS)
- ✅ Streamlit-based chatbot deployment
- ✅ 10/10 test cases passed

---

## 🏗️ System Architecture

### LangGraph Nodes

```text
memory
  ↓
router
 ├── retrieve → answer → eval → save
 ├── tool     → answer → eval → save
 └── skip     → answer → eval → save
```

### Routing Types

- `retrieve` → Knowledge base questions  
- `memory_only` → Conversational follow-ups  
- `tool` → Queries requiring live web data

---

## 🧠 Tech Stack

| Component | Technology |
|----------|------------|
| LLM | LLaMA 3.3 70B (Groq API) |
| Framework | LangGraph |
| Vector DB | ChromaDB |
| Embeddings | all-MiniLM-L6-v2 |
| Web Search | DuckDuckGo (ddgs) |
| Frontend | Streamlit |
| Evaluation | RAGAS |
| Language | Python |

---

## 📂 Knowledge Base Covers

- Consumer Protection
- Tenant Rights
- Right to Information (RTI)
- Fundamental Rights
- Labour Laws
- Criminal Procedure
- Domestic Violence
- Motor Vehicle Claims
- Cybercrime Laws
- Property & Inheritance
- Environmental Laws
- Free Legal Aid

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/LexGuide.git
cd LexGuide
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Add your API key in `.env`:

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run legal_streamlit.py
```

App will run at:

```text
http://localhost:8501
```

---

## 📊 Evaluation Results

### Functional Tests

- 10/10 Tests Passed ✅

### RAGAS Metrics

| Metric | Score |
|--------|-------|
| Faithfulness | 0.90 |
| Answer Relevancy | 0.87 |
| Context Precision | 0.83 |

---

## 📁 Project Files

```text
LexGuide/
│
├── legal_streamlit.py
├── Capstone_Project_Ayush_23052070.ipynb
├── requirements.txt
├── .env
└── README.md
```

---

## 🔍 Challenges Solved

- Hallucination prevention with retry loop
- Query misclassification handling
- Web search fallback mechanism
- Context window management
- Streamlit session persistence

---

## 🎯 Future Improvements

- Support for multilingual legal guidance
- Voice-based assistance
- Government portal integration
- Expanded legal knowledge base
- Fine-tuned legal LLM

---

## 👨‍💻 Author

**Ayush Sankrit**  
Roll No: 23052070  
B.Tech CSE  
Agentic AI Hands-On Course

---

## 📜 Disclaimer

LexGuide provides **legal awareness only** and does **not** substitute professional legal advice.

---

## ⭐ If you like this project

Give it a star on GitHub!
