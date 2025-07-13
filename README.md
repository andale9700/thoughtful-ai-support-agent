# Thoughtful AI Customer Support Agent

A sophisticated RAG-based customer support agent built for Thoughtful AI's healthcare automation solutions, featuring semantic embeddings and streaming responses.

## 🚀 Features

- **⚡ Instant RAG Responses**: Semantic matching for known healthcare questions using sentence transformers
- **🌊 Streaming LLM Integration**: Real-time OpenAI responses for personalized queries
- **🧠 Smart Architecture**: Clean separation between RAG matching and LLM fallback
- **🎨 Modern UI**: Streamlit interface with progressive response display
- **🔒 Robust Error Handling**: Graceful fallbacks and comprehensive error management

## 🏗️ Architecture

```
├── main.py                    # Streamlit UI with streaming support
├── question_matcher.py        # RAG-based semantic matching
├── llm_service.py            # OpenAI integration with streaming
├── data.py                   # Healthcare Q&A dataset
├── config.py                 # Configuration constants
├── requirements.txt          # Dependencies
└── tests/                    # Test suite
```

## 📋 Prerequisites

- Python 3.8+
- OpenAI API key
- Required packages (see requirements.txt)

## 🔧 Setup

### Local Development

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd thoughtful-automation-ai
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   ```

4. **Run the application**:
   ```bash
   streamlit run main.py
   ```

### Replit Deployment

1. **Import from GitHub** in Replit
2. **Run setup script**:
   ```bash
   python replit_setup.py
   ```
3. **Add your OpenAI API key** to the `.env` file
4. **Start the app**:
   ```bash
   streamlit run main.py
   ```

## 🧪 Testing

Run the test suite:
```bash
python tests/test_question_matcher.py
```

Current test performance:
- ✅ **94.4%** overall accuracy
- ✅ **88.9%** success rate on healthcare questions
- ✅ **100%** rejection rate on off-topic questions

## 💡 Usage Examples

### Healthcare Questions (RAG Responses)
- "What does EVA do?" → Instant response about Eligibility Verification Agent
- "Tell me about CAM" → Instant response about Claims Processing Agent
- "How does PHIL work?" → Instant response about Payment Posting Agent

### General Questions (LLM Streaming)
- "What can you do for me?" → Personalized streaming response
- "How can Thoughtful AI help my practice?" → Contextual LLM response

## 🔍 Technical Details

### RAG Implementation
- **Model**: `all-MiniLM-L6-v2` sentence transformer
- **Similarity**: Cosine similarity with 0.4 threshold
- **Performance**: Sub-second response times for known questions

### LLM Integration
- **Model**: GPT-3.5-turbo with streaming
- **Fallback**: Graceful error handling with informative messages
- **UI**: Progressive text display with typing indicators

## 🚀 Deployment

This project is designed to work seamlessly with:
- **Replit**: One-click deployment from GitHub
- **Streamlit Cloud**: Direct deployment support
- **Docker**: Containerization ready
- **Heroku**: Web app deployment

## 🔐 Environment Variables

Create a `.env` file with:
```env
OPENAI_API_KEY=your-openai-api-key-here
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Support

For questions about Thoughtful AI's healthcare automation solutions:
- Visit: [thoughtfulai.com](https://thoughtfulai.com)
- Email: support@thoughtfulai.com

---

Built with ❤️ for healthcare automation 