"""
RAG-based question matching using semantic embeddings
"""

from typing import Optional, Tuple, List
import numpy as np
from sentence_transformers import SentenceTransformer
from data import THOUGHTFUL_AI_QA

embedding_model = None
precomputed_qa_embeddings = None
qa_dataset = None


def initialize_embedding_model():
    """Initialize the embedding model and pre-compute embeddings for Q&A pairs"""
    global embedding_model, precomputed_qa_embeddings, qa_dataset
    
    if embedding_model is None:
        embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        
        question_texts = [qa["question"] for qa in THOUGHTFUL_AI_QA]
        precomputed_qa_embeddings = embedding_model.encode(question_texts)
        qa_dataset = THOUGHTFUL_AI_QA


def calculate_cosine_similarity(vector_a: np.ndarray, vector_b: np.ndarray) -> float:
    """Calculate cosine similarity between two vectors"""
    dot_product = np.dot(vector_a, vector_b)
    magnitude_a = np.linalg.norm(vector_a)
    magnitude_b = np.linalg.norm(vector_b)
    
    if magnitude_a == 0 or magnitude_b == 0:
        return 0
    
    return dot_product / (magnitude_a * magnitude_b)


def find_best_match(user_question: str, similarity_threshold: float = 0.4) -> Optional[Tuple[str, float]]:
    """
    Find the best matching answer using semantic similarity
    
    Args:
        user_question: The user's input question
        similarity_threshold: Minimum similarity score required for a match (0-1)
        
    Returns:
        Tuple of (answer, similarity_score) if match found, None otherwise
    """
    if not user_question or not user_question.strip():
        return None
    
    initialize_embedding_model()
    
    user_question_embedding = embedding_model.encode(user_question)
    
    highest_similarity_score = 0
    best_matching_answer = None
    
    for index, qa_embedding in enumerate(precomputed_qa_embeddings):
        current_similarity = calculate_cosine_similarity(user_question_embedding, qa_embedding)
        
        if current_similarity > highest_similarity_score:
            highest_similarity_score = current_similarity
            best_matching_answer = qa_dataset[index]["answer"]
    
    if highest_similarity_score >= similarity_threshold:
        return (best_matching_answer, highest_similarity_score)
    
    return None 