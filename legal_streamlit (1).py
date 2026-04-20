
import streamlit as st
import uuid
import chromadb
from dotenv import load_dotenv
from typing import TypedDict, List

from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()

st.set_page_config(
    page_title="LexGuide — Indian Legal Awareness Assistant",
    page_icon="⚖️",
    layout="centered"
)

st.title("⚖️ LexGuide — Indian Legal Awareness Assistant")
st.caption("Evidence-based plain-language legal awareness for Indian citizens.")

class DummyEmbedder:
    def encode(self, texts):
        return [[float(len(t))] * 5 for t in texts]

@st.cache_resource
def load_agent():
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0
    )

    embedder = DummyEmbedder()
    client = chromadb.Client()

    try:
        client.delete_collection("capstone_kb")
    except:
        pass

    collection = client.create_collection("capstone_kb")

    DOCUMENTS = [
        {"id": "doc_001", "topic": "Consumer Protection Act 2019",
         "text": "District: up to ₹1 crore, State: ₹1–10 crore, National: above ₹10 crore."},

        {"id": "doc_002", "topic": "RTI Act",
         "text": "RTI fee ₹10. Reply within 30 days."},

        {"id": "doc_003", "topic": "Police Rights",
         "text": "FIR must be registered. Produce accused within 24 hours."},
    ]

    texts = [d["text"] for d in DOCUMENTS]

    collection.add(
        documents=texts,
        embeddings=embedder.encode(texts),
        ids=[d["id"] for d in DOCUMENTS],
        metadatas=[{"topic": d["topic"]} for d in DOCUMENTS]
    )

    class State(TypedDict):
        question: str
        answer: str

    def answer_node(state):
        msgs = [SystemMessage(content="You are a legal assistant.")]
        msgs.append(HumanMessage(content=state["question"]))

        response = llm.invoke(msgs).content
        return {"answer": response}

    g = StateGraph(State)
    g.add_node("answer", answer_node)
    g.set_entry_point("answer")
    g.add_edge("answer", END)

    app = g.compile()
    return app


try:
    agent_app = load_agent()
    st.success("✅ System Ready")
except Exception as e:
    st.error(f"Error: {e}")
    st.stop()


if "messages" not in st.session_state:
    st.session_state.messages = []

if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())[:8]


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


if prompt := st.chat_input("Ask your legal question..."):

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            result = agent_app.invoke({"question": prompt})
            answer = result["answer"]

        st.write(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
