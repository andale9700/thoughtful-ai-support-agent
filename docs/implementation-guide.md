# Quick Implementation Guide

## Step-by-Step Implementation

### 1. Project Setup
```bash
# Create these files:
main.py
question_matcher.py
llm_service.py
data.py
config.py
requirements.txt
.env
```

### 2. Dependencies (requirements.txt)
```
streamlit==1.28.1
openai==1.3.0
python-dotenv==1.0.0
thefuzz==0.19.0
```

### 3. Key Code Snippets

#### data.py - Predefined Q&A
```python
THOUGHTFUL_AI_QA = [
    {
        "question": "What does the eligibility verification agent (EVA) do?",
        "answer": "EVA automates the process of verifying a patient's eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."
    },
    # ... rest of questions
]
```

#### question_matcher.py - Fuzzy Matching
```python
from thefuzz import fuzz
from typing import Optional, Tuple

def find_best_match(user_question: str, threshold: int = 70) -> Optional[Tuple[str, int]]:
    """Find best matching answer using fuzzy string matching"""
    best_match = None
    best_score = 0
    
    for qa in THOUGHTFUL_AI_QA:
        score = fuzz.token_sort_ratio(user_question.lower(), qa["question"].lower())
        if score > best_score and score >= threshold:
            best_score = score
            best_match = qa["answer"]
    
    return (best_match, best_score) if best_match else None
```

#### main.py - Streamlit UI Structure
```python
import streamlit as st

st.title("Thoughtful AI Support Assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me about Thoughtful AI"):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Get response (from matcher or LLM)
    response = get_response(prompt)
    
    # Add assistant message
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Display
    with st.chat_message("assistant"):
        st.markdown(response)
```

### 4. Environment Setup (.env)
```
OPENAI_API_KEY=your-api-key-here
```

### 5. Running the App
```bash
streamlit run main.py
```

## Testing Checklist
- [ ] Test each predefined question
- [ ] Test variations (e.g., "Tell me about EVA", "What is EVA?")
- [ ] Test unrelated questions (should use LLM)
- [ ] Test with no API key (should show error)
- [ ] Test empty input 