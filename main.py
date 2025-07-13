"""
Thoughtful AI Customer Support Agent
Entry point for the Streamlit application
"""

import streamlit as st
from question_matcher import find_best_match
from llm_service import get_llm_response, get_llm_response_streaming
from config import APP_TITLE, WELCOME_MESSAGE


def configure_streamlit_page():
    """Configure Streamlit page settings and styling"""
    st.set_page_config(
        page_title="Thoughtful AI Support",
        page_icon="🤖",
        layout="centered",
        initial_sidebar_state="collapsed"
    )


def initialize_session_state():
    """Initialize chat history in session state if not exists"""
    if "messages" not in st.session_state:
        st.session_state.messages = []


def should_display_welcome_message():
    """Check if welcome message should be displayed"""
    return len(st.session_state.messages) == 0


def add_welcome_message_to_chat():
    """Add welcome message to chat history"""
    st.session_state.messages.append({
        "role": "assistant",
        "content": WELCOME_MESSAGE
    })


def add_user_message_to_chat(user_input):
    """Add user message to chat history"""
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })


def add_assistant_message_to_chat(response):
    """Add assistant response to chat history"""
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })


def find_rag_response(user_input):
    """Attempt to find a match using RAG-based matching"""
    match_result = find_best_match(user_input)
    if match_result:
        answer, confidence_score = match_result
        return answer
    return None


def display_chat_message(message):
    """Display a single chat message with appropriate styling"""
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


def display_all_chat_messages():
    """Display all messages in chat history"""
    for message in st.session_state.messages:
        display_chat_message(message)


def display_streaming_response(user_input):
    """Display streaming LLM response with visual feedback"""
    response_placeholder = st.empty()
    complete_response = ""
    
    for chunk in get_llm_response_streaming(user_input):
        complete_response += chunk
        response_placeholder.markdown(complete_response + "▌")
    
    response_placeholder.markdown(complete_response)
    return complete_response


def handle_user_input(user_input):
    """Process user input and generate response with streaming support"""
    add_user_message_to_chat(user_input)
    
    with st.chat_message("user"):
        st.markdown(user_input)
    
    rag_response = find_rag_response(user_input)
    
    with st.chat_message("assistant"):
        if rag_response:
            st.markdown(rag_response)
            add_assistant_message_to_chat(rag_response)
        else:
            streaming_response = display_streaming_response(user_input)
            add_assistant_message_to_chat(streaming_response)


def create_main_chat_interface():
    """Create the main chat interface with input handling"""
    st.title(APP_TITLE)
    
    initialize_session_state()
    
    if should_display_welcome_message():
        add_welcome_message_to_chat()
    
    display_all_chat_messages()
    
    user_input = st.chat_input("Ask me about Thoughtful AI's healthcare automation solutions...")
    
    if user_input:
        handle_user_input(user_input)


def main():
    """Main application entry point"""
    configure_streamlit_page()
    create_main_chat_interface()


if __name__ == "__main__":
    main() 