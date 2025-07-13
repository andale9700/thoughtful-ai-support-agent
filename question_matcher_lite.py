"""
Lightweight RAG-based question matching using tiny embeddings
Optimized for Replit's disk space constraints
"""

from typing import Optional, Tuple, List
import numpy as np
from data import THOUGHTFUL_AI_QA

embedding_model = None
precomputed_qa_embeddings = None
qa_dataset = None


def initialize_lightweight_embeddings():
    """Initialize with the smallest possible embedding model"""
    global embedding_model, precomputed_qa_embeddings, qa_dataset
    
    if embedding_model is None:
        try:
            # Try the smallest sentence transformer model first
            from sentence_transformers import SentenceTransformer
            embedding_model = SentenceTransformer('paraphrase-MiniLM-L3-v2')  # Much smaller than L6
            
            question_texts = [qa["question"] for qa in THOUGHTFUL_AI_QA]
            precomputed_qa_embeddings = embedding_model.encode(question_texts)
            qa_dataset = THOUGHTFUL_AI_QA
            print("✅ Using tiny sentence transformer model")
            
        except ImportError:
            # Fallback to even simpler approach
            print("⚠️ Sentence transformers not available, using keyword matching")
            initialize_keyword_matching()


def initialize_keyword_matching():
    """Fallback: Use simple keyword-based matching"""
    global embedding_model, precomputed_qa_embeddings, qa_dataset
    
    # Create simple keyword vectors for each Q&A pair
    from collections import Counter
    import re
    
    def create_keyword_vector(text):
        # Simple tokenization and keyword extraction
        words = re.findall(r'\b\w+\b', text.lower())
        # Focus on important healthcare terms
        important_keywords = [
            'eva', 'cam', 'phil', 'eligibility', 'verification', 'claims', 
            'processing', 'payment', 'posting', 'agent', 'automates', 
            'benefits', 'thoughtful', 'ai', 'healthcare', 'automation'
        ]
        
        # Create a simple vector based on keyword presence
        vector = []
        for keyword in important_keywords:
            vector.append(words.count(keyword))
        
        # Add total word count as a feature
        vector.append(len(words))
        return np.array(vector, dtype=float)
    
    question_texts = [qa["question"] for qa in THOUGHTFUL_AI_QA]
    precomputed_qa_embeddings = [create_keyword_vector(q) for q in question_texts]
    precomputed_qa_embeddings = np.array(precomputed_qa_embeddings)
    qa_dataset = THOUGHTFUL_AI_QA
    embedding_model = "keyword_matching"
    print("✅ Using lightweight keyword matching")


def calculate_cosine_similarity(vector_a: np.ndarray, vector_b: np.ndarray) -> float:
    """Calculate cosine similarity between two vectors"""
    dot_product = np.dot(vector_a, vector_b)
    magnitude_a = np.linalg.norm(vector_a)
    magnitude_b = np.linalg.norm(vector_b)
    
    if magnitude_a == 0 or magnitude_b == 0:
        return 0
    
    return dot_product / (magnitude_a * magnitude_b)


def calculate_keyword_similarity(question1: str, question2: str) -> float:
    """Simple keyword-based similarity for fallback"""
    from collections import Counter
    import re
    
    def get_keywords(text):
        words = re.findall(r'\b\w+\b', text.lower())
        return Counter(words)
    
    keywords1 = get_keywords(question1)
    keywords2 = get_keywords(question2)
    
    # Calculate Jaccard similarity
    intersection = sum((keywords1 & keywords2).values())
    union = sum((keywords1 | keywords2).values())
    
    return intersection / union if union > 0 else 0


def find_best_match(user_question: str, similarity_threshold: float = 0.3) -> Optional[Tuple[str, float]]:
    """
    Find the best matching answer using lightweight semantic similarity
    
    Args:
        user_question: The user's input question
        similarity_threshold: Minimum similarity score required for a match
        
    Returns:
        Tuple of (answer, similarity_score) if match found, None otherwise
    """
    if not user_question or not user_question.strip():
        return None
    
    initialize_lightweight_embeddings()
    
    highest_similarity_score = 0
    best_matching_answer = None
    
    if embedding_model == "keyword_matching":
        # Use keyword-based matching
        for index, qa in enumerate(qa_dataset):
            current_similarity = calculate_keyword_similarity(user_question, qa["question"])
            
            if current_similarity > highest_similarity_score:
                highest_similarity_score = current_similarity
                best_matching_answer = qa["answer"]
    
    else:
        # Use embedding-based matching
        user_question_embedding = embedding_model.encode(user_question)
        
        for index, qa_embedding in enumerate(precomputed_qa_embeddings):
            current_similarity = calculate_cosine_similarity(user_question_embedding, qa_embedding)
            
            if current_similarity > highest_similarity_score:
                highest_similarity_score = current_similarity
                best_matching_answer = qa_dataset[index]["answer"]
    
    # Lower threshold for keyword matching since it's less precise
    effective_threshold = similarity_threshold * 0.7 if embedding_model == "keyword_matching" else similarity_threshold
    
    if highest_similarity_score >= effective_threshold:
        return (best_matching_answer, highest_similarity_score)
    
    return None 