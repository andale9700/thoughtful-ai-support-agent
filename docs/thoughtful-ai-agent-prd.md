# Thoughtful AI Customer Support Agent - Product Requirements Document

## Executive Summary
A lightweight, conversational AI agent that answers questions about Thoughtful AI's healthcare automation products using predefined responses, with fallback to general LLM capabilities for off-topic questions.

## Technical Architecture

### Technology Stack
- **Language**: Python 3.9+
- **UI Framework**: Streamlit (chosen for rapid development and built-in chat components)
- **LLM Integration**: OpenAI API (for fallback responses)
- **Text Matching**: FuzzyWuzzy (for intelligent question matching)
- **Dependencies Management**: requirements.txt

### Why This Stack?
1. **Streamlit**: Provides `st.chat_message` and `st.chat_input` components out-of-the-box, perfect for chat interfaces
2. **OpenAI API**: Industry standard, reliable, easy integration
3. **FuzzyWuzzy**: Simple fuzzy string matching, no vector database needed for 5 questions
4. **Python**: Most common for AI projects, extensive ecosystem

## System Design

### Core Components

1. **Question Matcher (`question_matcher.py`)**
   - Uses fuzzy string matching to find best match from predefined questions
   - Returns confidence score and matched answer
   - Threshold-based decision making (e.g., 70% similarity required)

2. **LLM Service (`llm_service.py`)**
   - Handles OpenAI API integration
   - Provides fallback responses for unmatched questions
   - Includes context about Thoughtful AI in system prompt

3. **Chat Interface (`main.py`)**
   - Streamlit-based UI with chat history
   - Session state management
   - Error handling and graceful degradation

### Data Flow
1. User enters question in chat interface
2. Question matcher attempts to find match in predefined dataset
3. If match found (above threshold), return predefined answer
4. If no match, send to LLM with context about being a Thoughtful AI assistant
5. Display response in chat interface
6. Maintain conversation history

## Implementation Details

### Project Structure
```
thoughtful-ai-agent/
├── main.py                 # Entry point and Streamlit UI
├── question_matcher.py     # Fuzzy matching logic
├── llm_service.py         # OpenAI integration
├── data.py                # Hardcoded Q&A dataset
├── config.py              # Configuration constants
├── requirements.txt       # Dependencies
└── .env.example          # Example environment variables
```

### Key Features
1. **Intelligent Matching**: Handles variations in phrasing (e.g., "What does EVA do?" matches "What does the eligibility verification agent (EVA) do?")
2. **Conversation Memory**: Maintains chat history during session
3. **Error Handling**: Graceful fallback if LLM API fails
4. **Clean UI**: Professional chat interface with Thoughtful AI branding

### Configuration
- Fuzzy matching threshold: 70% (configurable)
- LLM model: gpt-3.5-turbo (for cost efficiency)
- Max response length: 500 tokens
- UI theme: Streamlit default with custom title

## Development Timeline (20-30 minutes)

1. **Setup & Dependencies** (3 min)
   - Create project structure
   - Write requirements.txt
   
2. **Core Logic** (10 min)
   - Implement question matcher
   - Create LLM service
   - Set up data structure

3. **UI Implementation** (10 min)
   - Build Streamlit chat interface
   - Add session state management
   - Implement chat flow

4. **Testing & Polish** (5-7 min)
   - Test various question formats
   - Add error handling
   - Final UI touches

## Success Criteria

1. **Functionality**
   - ✓ Correctly matches and responds to predefined questions
   - ✓ Falls back to LLM for unknown questions
   - ✓ Maintains conversation context

2. **Code Quality**
   - ✓ Clean separation of concerns
   - ✓ Type hints where appropriate
   - ✓ Clear variable naming

3. **Robustness**
   - ✓ Handles API failures gracefully
   - ✓ Validates user input
   - ✓ Provides helpful error messages

## Deployment Notes
- Requires `OPENAI_API_KEY` environment variable
- Run with: `streamlit run main.py`
- Default port: 8501

## Future Enhancements (Out of Scope)
- Vector similarity search for better matching
- Multi-turn conversation tracking
- Analytics and logging
- Authentication
- Rate limiting 