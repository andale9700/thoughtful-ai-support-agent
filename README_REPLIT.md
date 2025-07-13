# Thoughtful AI Customer Support Agent

A RAG-based customer support agent for Thoughtful AI's healthcare automation solutions.

## Features
- ⚡ Instant responses for known questions using semantic embeddings
- 🌊 Streaming LLM responses for personalized questions  
- 🧠 RAG architecture with sentence transformers
- 🎨 Clean Streamlit interface

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Add OpenAI API key to `.env` file
3. Run: `streamlit run main.py`

## Architecture
- **main.py**: Streamlit UI with streaming support
- **question_matcher.py**: RAG-based semantic matching
- **llm_service.py**: OpenAI integration with streaming
- **data.py**: Q&A dataset
- **config.py**: Configuration constants

