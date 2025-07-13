"""
RAG-based question matching using keyword vectors
Optimized for reliability and minimal dependencies
"""

from typing import Optional, Tuple, List
import numpy as np
from data import THOUGHTFUL_AI_QA

embedding_model = None
precomputed_qa_embeddings = None
qa_dataset = None


def initialize_question_matching():
    """Initialize keyword-based question matching system"""
    global embedding_model, precomputed_qa_embeddings, qa_dataset
    
    if embedding_model is None:
        from collections import Counter
        import re
        
        def create_keyword_vector(text):
            words = re.findall(r'\b\w+\b', text.lower())
            important_keywords = [
                'eva', 'cam', 'phil', 'eligibility', 'verification', 'claims', 
                'processing', 'payment', 'posting', 'agent', 'automates', 
                'benefits', 'thoughtful', 'ai', 'healthcare', 'automation'
            ]
            
            vector = []
            for keyword in important_keywords:
                vector.append(words.count(keyword))
            
            vector.append(len(words))
            return np.array(vector, dtype=float)
        
        question_texts = [qa["question"] for qa in THOUGHTFUL_AI_QA]
        precomputed_qa_embeddings = [create_keyword_vector(q) for q in question_texts]
        precomputed_qa_embeddings = np.array(precomputed_qa_embeddings)
        qa_dataset = THOUGHTFUL_AI_QA
        embedding_model = "keyword_vectors"


def calculate_cosine_similarity(vector_a: np.ndarray, vector_b: np.ndarray) -> float:
    """Calculate cosine similarity between two vectors"""
    dot_product = np.dot(vector_a, vector_b)
    magnitude_a = np.linalg.norm(vector_a)
    magnitude_b = np.linalg.norm(vector_b)
    
    if magnitude_a == 0 or magnitude_b == 0:
        return 0
    
    return dot_product / (magnitude_a * magnitude_b)


def calculate_keyword_similarity(question1: str, question2: str) -> float:
    """Calculate keyword-based similarity between two questions"""
    from collections import Counter
    import re
    
    def get_keywords(text):
        words = re.findall(r'\b\w+\b', text.lower())
        return Counter(words)
    
    keywords1 = get_keywords(question1)
    keywords2 = get_keywords(question2)
    
    intersection = sum((keywords1 & keywords2).values())
    union = sum((keywords1 | keywords2).values())
    
    return intersection / union if union > 0 else 0


def find_best_match(user_question: str, similarity_threshold: float = 0.3) -> Optional[Tuple[str, float]]:
    """
    Find the best matching answer using keyword-based similarity
    
    Args:
        user_question: The user's input question
        similarity_threshold: Minimum similarity score required for a match
        
    Returns:
        Tuple of (answer, similarity_score) if match found, None otherwise
    """
    if not user_question or not user_question.strip():
        return None
    
    initialize_question_matching()
    
    highest_similarity_score = 0
    best_matching_answer = None
    
    for index, qa in enumerate(qa_dataset):
        current_similarity = calculate_keyword_similarity(user_question, qa["question"])
        
        if current_similarity > highest_similarity_score:
            highest_similarity_score = current_similarity
            best_matching_answer = qa["answer"]
    
    effective_threshold = similarity_threshold * 0.7
    
    if highest_similarity_score >= effective_threshold:
        return (best_matching_answer, highest_similarity_score)
    
    return None 