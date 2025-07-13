# Thoughtful AI Agent - Implementation Task List

## Overview
This task list is organized by dependencies to ensure efficient implementation within the 20-30 minute timeframe. Each task includes estimated time and verification criteria.

## Phase 1: Project Setup (3 minutes)

### 1.1 Create Project Structure ⏱️ 1 min
- [x] Create `main.py` (entrypoint requirement ✓)
- [x] Create `requirements.txt`
- [x] Create `.env` file (using setup instructions instead due to security restrictions)
- [x] Create supporting Python files:
  - [x] `data.py`
  - [x] `config.py`
  - [x] `question_matcher.py`
  - [x] `llm_service.py`

### 1.2 Define Dependencies ⏱️ 1 min
- [x] Add to `requirements.txt`:
  ```
  streamlit==1.28.1
  openai==1.3.0
  python-dotenv==1.0.0
  thefuzz==0.19.0
  ```

### 1.3 Environment Configuration ⏱️ 1 min
- [x] Create `.env` with placeholder: `OPENAI_API_KEY=your-key-here` (via setup instructions)
- [x] Create `config.py` with constants:
  - [x] Fuzzy matching threshold (70%)
  - [x] LLM model name (gpt-3.5-turbo)
  - [x] Max tokens (500)

## Phase 2: Core Data Layer (3 minutes)

### 2.1 Implement Hardcoded Dataset ⏱️ 3 min
**File:** `data.py`
- [x] Create `THOUGHTFUL_AI_QA` list with all 5 Q&A pairs from requirements
- [x] Ensure exact questions and answers as provided
- [x] Add helper function to get all questions for display

**Verification:** All 5 questions from project spec are included ✓

## Phase 3: Question Matching Logic (5 minutes)

### 3.1 Implement Fuzzy Matcher ⏱️ 5 min
**File:** `question_matcher.py`
- [x] Import thefuzz and required types
- [x] Create `find_best_match()` function:
  - [x] Accept user question and threshold
  - [x] Iterate through Q&A dataset
  - [x] Use `fuzz.token_sort_ratio()` for matching
  - [x] Return tuple of (answer, confidence_score)
  - [x] Return None if no match above threshold
- [x] Add docstrings and type hints

**Verification:** Can handle variations like "What does EVA do?" ✓

## Phase 4: LLM Integration (5 minutes)

### 4.1 Implement OpenAI Service ⏱️ 5 min
**File:** `llm_service.py`
- [x] Import openai and handle environment variables
- [x] Create `get_llm_response()` function:
  - [x] Set system prompt mentioning Thoughtful AI context
  - [x] Handle API errors gracefully
  - [x] Return fallback message if API fails
- [x] Add function to check if API key exists
- [x] Implement timeout handling

**Verification:** Fallback to generic LLM responses works ✓

## Phase 5: User Interface (7 minutes)

### 5.1 Build Streamlit Chat UI ⏱️ 7 min
**File:** `main.py`
- [x] Import all modules and set page config
- [x] Initialize session state for messages
- [x] Create UI structure:
  - [x] Page title: "Thoughtful AI Support Assistant"
  - [x] Display chat history from session state
  - [x] Add chat input component
- [x] Implement main chat logic:
  - [x] Capture user input
  - [x] Try fuzzy matching first
  - [x] Fall back to LLM if no match
  - [x] Add messages to session state
  - [x] Display responses
- [x] Add welcome message on first load

**Verification:** User-friendly chat interface ✓

## Phase 6: Integration & Error Handling (5 minutes)

### 6.1 Connect All Components ⏱️ 3 min
- [x] Create main `get_response()` function that:
  - [x] Calls question matcher
  - [x] Falls back to LLM if needed
  - [x] Handles all errors gracefully
- [x] Add logging for debugging (via test suites)
- [x] Ensure proper imports across files

### 6.2 Robustness & Error Handling ⏱️ 2 min
- [x] Handle empty/whitespace input
- [x] Handle missing OpenAI API key
- [x] Add try-except blocks for all external calls
- [x] Display user-friendly error messages
- [x] Ensure app doesn't crash on errors

**Verification:** Robust error handling for edge cases ✓

## Phase 7: Testing & Polish (2 minutes)

### 7.1 Functional Testing ⏱️ 1 min
- [x] Test each predefined question exactly
- [x] Test variations: "EVA?", "Tell me about EVA"
- [x] Test unrelated question: "What's the weather?"
- [x] Test empty input
- [x] Test without API key

### 7.2 Code Quality Check ⏱️ 1 min
- [x] Verify clean code structure
- [x] Check variable naming clarity
- [x] Ensure proper type hints where used
- [x] Verify no hardcoded secrets

## Final Checklist - Project Requirements

### ✅ Functional Requirements
- [x] Accepts user input and answers conversationally
- [x] Retrieves relevant answers from hardcoded responses
- [x] Falls back to LLM for non-matching questions
- [x] Displays answers in user-friendly format

### ✅ Technical Requirements
- [x] Uses Python (any language allowed)
- [x] Uses Streamlit (web-based framework)
- [x] Has `main.py` as entry point
- [x] Ready for Replit deployment

### ✅ Evaluation Criteria
- [x] **Functionality**: Correct conversation logic implementation
- [x] **Code Quality**: Clean, readable, well-structured code
- [x] **Robustness**: Error handling for invalid inputs and edge cases

## Running the Application
```bash
streamlit run main.py
```

## Time Summary
- Setup: 3 min
- Core Logic: 13 min
- Testing: 2 min
- **Total: 18 minutes** (leaving buffer for unexpected issues) 