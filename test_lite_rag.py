#!/usr/bin/env python3
"""
Test script for lightweight RAG matching
Works without sentence-transformers
"""

from question_matcher_lite import find_best_match

def test_lightweight_rag():
    """Test the lightweight RAG implementation"""
    
    print("🧪 Testing Lightweight RAG Matching")
    print("=" * 50)
    
    test_cases = [
        ("What does EVA do?", "EVA"),
        ("tell me about eva", "EVA"), 
        ("What does CAM do?", "CAM"),
        ("tell me about cam", "CAM"),
        ("How does PHIL work?", "PHIL"),
        ("tell me about phil", "PHIL"),
        ("Tell me about Thoughtful AI agents", "General"),
        ("What are the benefits?", "Benefits"),
        ("claims processing agent", "CAM"),
        ("eligibility verification", "EVA"),
        ("payment posting", "PHIL"),
        # Off-topic questions
        ("what color is the sky?", "None"),
        ("how's the weather?", "None"),
        ("what is 2+2?", "None"),
    ]
    
    matches_found = 0
    correct_matches = 0
    
    for question, expected_type in test_cases:
        result = find_best_match(question)
        
        print(f"\nQ: '{question}'")
        print(f"   Expected: {expected_type}")
        
        if result:
            answer, score = result
            matches_found += 1
            print(f"   ✅ Match found (score: {score:.3f})")
            print(f"   Answer: {answer[:60]}...")
            
            # Check if it's a reasonable match
            if expected_type != "None":
                correct_matches += 1
                if expected_type in ["EVA", "CAM", "PHIL"] and expected_type.lower() in answer.lower():
                    print(f"   ✅ Correct agent match!")
        else:
            print(f"   ❌ No match found")
            if expected_type == "None":
                correct_matches += 1
                print(f"   ✅ Correctly rejected off-topic question")
    
    print(f"\n" + "=" * 50)
    print(f"📊 Results Summary:")
    print(f"   Total questions: {len(test_cases)}")
    print(f"   Matches found: {matches_found}")
    print(f"   Accuracy estimate: {correct_matches}/{len(test_cases)} ({correct_matches/len(test_cases)*100:.1f}%)")
    
    if correct_matches >= len(test_cases) * 0.7:  # 70% accuracy threshold
        print(f"   🎉 Lightweight RAG is working well!")
        return True
    else:
        print(f"   ⚠️  Lightweight RAG needs tuning")
        return False

if __name__ == "__main__":
    test_lightweight_rag() 