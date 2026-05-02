import gradio as gr
import os
from pathlib import Path

# Check if OpenAI API key is available
has_api_key = bool(os.getenv("OPENAI_API_KEY"))

def query_documents(query, history):
    if not has_api_key:
        return history + [[query, "Please set OPENAI_API_KEY in Space settings to use this demo."]]
    
    # Simplified demo response
    return history + [[query, f"Demo response for: {query}\n\nTo use the full RAG system, install: pip install ai-rag-system"]]

def ingest_docs(files):
    if not has_api_key:
        return "Please set OPENAI_API_KEY in Space settings."
    return f"Ingested {len(files)} files (demo mode)"

with gr.Blocks(title="AI RAG System - Demo") as demo:
    gr.Markdown("# 🤖 AI RAG System Demo")
    gr.Markdown("Ask questions about your documents. Install locally: `pip install ai-rag-system`")
    
    if not has_api_key:
        gr.Warning("⚠️ OPENAI_API_KEY not set. This is a demo mode.")
    
    with gr.Tab("Query"):
        chatbot = gr.Chatbot()
        query = gr.Textbox(label="Ask a question")
        btn = gr.Button("Submit")
        btn.click(query_documents, [query, chatbot], [chatbot])
    
    with gr.Tab("Ingest"):
        files = gr.File(label="Upload Documents", file_count="multiple", type="filepath")
        ingest_btn = gr.Button("Ingest")
        output = gr.Textbox(label="Result")
        ingest_btn.click(ingest_docs, [files], [output])
    
    gr.Markdown("## 📦 Install")
    gr.Code("pip install ai-rag-system", language="bash")
    gr.Markdown("GitHub: https://github.com/my-ai-stack/ai-rag-system")

if __name__ == "__main__":
    demo.launch()
