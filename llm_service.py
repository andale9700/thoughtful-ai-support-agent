"""
OpenAI LLM integration for fallback responses
"""

import os
from typing import Optional
from dotenv import load_dotenv
from config import LLM_MODEL, MAX_TOKENS

load_dotenv()


def get_openai_api_key() -> Optional[str]:
    """Retrieve OpenAI API key from environment variables"""
    return os.getenv("OPENAI_API_KEY")


def is_openai_api_key_available() -> bool:
    """Check if OpenAI API key is available and configured"""
    api_key = get_openai_api_key()
    return api_key is not None and api_key.strip() != "" and api_key != "your-key-here"


def create_openai_client():
    """Create and return OpenAI client if possible"""
    if not is_openai_api_key_available():
        return None
    
    try:
        from openai import OpenAI
        api_key = get_openai_api_key()
        return OpenAI(api_key=api_key)
    except Exception:
        return None


def build_system_prompt() -> str:
    """Build system prompt with Thoughtful AI context"""
    return """You are a helpful customer support assistant for Thoughtful AI, a company that specializes in healthcare automation. 

Thoughtful AI provides AI-powered automation agents for healthcare processes including:
- EVA (Eligibility Verification Agent) - automates patient eligibility verification
- CAM (Claims Processing Agent) - streamlines claims submission and management  
- PHIL (Payment Posting Agent) - automates payment posting to patient accounts

You should be helpful and professional. If asked about topics outside of healthcare automation or Thoughtful AI, politely redirect the conversation back to how Thoughtful AI can help with healthcare automation needs."""


def call_openai_completion_api(openai_client, user_question: str) -> Optional[str]:
    """Make API call to OpenAI with comprehensive error handling"""
    try:
        conversation_messages = [
            {"role": "system", "content": build_system_prompt()},
            {"role": "user", "content": user_question}
        ]
        
        completion_response = openai_client.chat.completions.create(
            model=LLM_MODEL,
            messages=conversation_messages,
            max_tokens=MAX_TOKENS,
            temperature=0.7,
            timeout=30
        )
        
        return completion_response.choices[0].message.content.strip()
    
    except Exception:
        return None


def call_openai_streaming_api(openai_client, user_question: str):
    """Make streaming API call to OpenAI"""
    try:
        conversation_messages = [
            {"role": "system", "content": build_system_prompt()},
            {"role": "user", "content": user_question}
        ]
        
        streaming_response = openai_client.chat.completions.create(
            model=LLM_MODEL,
            messages=conversation_messages,
            max_tokens=MAX_TOKENS,
            temperature=0.7,
            timeout=30,
            stream=True
        )
        
        for response_chunk in streaming_response:
            if response_chunk.choices[0].delta.content is not None:
                yield response_chunk.choices[0].delta.content
    
    except Exception:
        yield "I'm sorry, I'm currently unable to process your question. Please try again later or contact our support team for assistance with Thoughtful AI's healthcare automation solutions."


def get_error_fallback_message() -> str:
    """Return simple fallback message when LLM is unavailable"""
    return "I'm sorry, I'm currently unable to process your question. Please try again later or contact our support team for assistance with Thoughtful AI's healthcare automation solutions."


def get_llm_response(user_question: str) -> str:
    """
    Get response from OpenAI LLM for questions that don't match predefined Q&A
    
    Args:
        user_question: The user's input question
        
    Returns:
        LLM-generated response or simple fallback message
    """
    if not user_question or not user_question.strip():
        return "Please ask me a question about Thoughtful AI's healthcare automation solutions."
    
    if not is_openai_api_key_available():
        return "API key not configured. Please set up your OpenAI API key to use this feature."
    
    openai_client = create_openai_client()
    if not openai_client:
        return get_error_fallback_message()
    
    llm_generated_response = call_openai_completion_api(openai_client, user_question)
    
    if llm_generated_response:
        return llm_generated_response
    else:
        return get_error_fallback_message() 


def get_llm_response_streaming(user_question: str):
    """
    Get streaming response from OpenAI LLM for questions that don't match predefined Q&A
    
    Args:
        user_question: The user's input question
        
    Returns:
        Generator yielding response chunks
    """
    if not user_question or not user_question.strip():
        yield "Please ask me a question about Thoughtful AI's healthcare automation solutions."
        return
    
    if not is_openai_api_key_available():
        yield "API key not configured. Please set up your OpenAI API key to use this feature."
        return
    
    openai_client = create_openai_client()
    if not openai_client:
        yield get_error_fallback_message()
        return
    
    yield from call_openai_streaming_api(openai_client, user_question) 