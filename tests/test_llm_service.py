"""
Test suite for LLM service functionality
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from llm_service import get_llm_response, is_api_key_configured


def get_test_questions():
    """Test questions for LLM service"""
    return [
        'How can AI help in healthcare?',
        'Tell me about automation technology',
        'What is the weather like today?',
        'I need help with claims processing',
        'How do I cook pasta?'
    ]


def test_api_key_configuration():
    """Test that API key is properly configured"""
    print('✅ TESTING API KEY CONFIGURATION:')
    api_configured = is_api_key_configured()
    print(f'  API Key Configured: {api_configured}')
    return api_configured


def test_llm_responses():
    """Test that LLM service returns reasonable responses"""
    questions = get_test_questions()
    results = []
    
    print('✅ TESTING LLM RESPONSES:')
    for question in questions:
        response = get_llm_response(question)
        is_valid_response = response and len(response) > 10 and response != question
        
        results.append((question, is_valid_response, len(response)))
        status = '✓' if is_valid_response else '✗'
        print(f'  {status} "{question}"')
        print(f'    Response length: {len(response)} chars')
        print(f'    Valid response: {is_valid_response}')
    
    return results


def test_healthcare_context():
    """Test that healthcare questions mention Thoughtful AI context"""
    healthcare_questions = [
        'How can AI help in healthcare?',
        'Tell me about automation in healthcare',
        'I need help with claims processing'
    ]
    results = []
    
    print('\n✅ TESTING HEALTHCARE CONTEXT:')
    for question in healthcare_questions:
        response = get_llm_response(question)
        mentions_thoughtful_ai = 'thoughtful ai' in response.lower()
        mentions_agents = any(agent in response.lower() for agent in ['eva', 'cam', 'phil'])
        has_context = mentions_thoughtful_ai or mentions_agents
        
        results.append((question, has_context))
        status = '✓' if has_context else '✗'
        print(f'  {status} "{question}"')
        print(f'    Has healthcare context: {has_context}')
    
    return results


def test_edge_cases():
    """Test edge cases and error handling"""
    edge_cases = ['', '   ', 'x']
    results = []
    
    print('\n✅ TESTING EDGE CASES:')
    for case in edge_cases:
        response = get_llm_response(case)
        handles_gracefully = response and len(response) > 10
        
        results.append((case, handles_gracefully))
        status = '✓' if handles_gracefully else '✗'
        case_display = f'"{case}"' if case.strip() else 'empty/whitespace'
        print(f'  {status} {case_display}')
        print(f'    Handles gracefully: {handles_gracefully}')
    
    return results


def calculate_simplified_test_statistics(api_result, response_results, healthcare_results, edge_results):
    """Calculate simplified test statistics"""
    valid_responses = sum(1 for _, valid, _ in response_results if valid)
    healthcare_context = sum(1 for _, has_context in healthcare_results if has_context)
    edge_handling = sum(1 for _, handles in edge_results if handles)
    
    total_tests = len(response_results) + len(healthcare_results) + len(edge_results) + (1 if api_result else 0)
    total_passed = valid_responses + healthcare_context + edge_handling + (1 if api_result else 0)
    
    return {
        'api_configured': api_result,
        'valid_responses': valid_responses,
        'response_total': len(response_results),
        'healthcare_context': healthcare_context,
        'healthcare_total': len(healthcare_results),
        'edge_handling': edge_handling,
        'edge_total': len(edge_results),
        'overall_success': total_passed,
        'overall_total': total_tests,
        'success_rate': (total_passed / total_tests) * 100 if total_tests > 0 else 0
    }


def display_simplified_test_summary(stats):
    """Display simplified test summary"""
    print(f'\n=== LLM SERVICE TEST SUMMARY ===')
    print(f'API Key Configured: {stats["api_configured"]}')
    print(f'Valid Responses: {stats["valid_responses"]}/{stats["response_total"]}')
    print(f'Healthcare Context: {stats["healthcare_context"]}/{stats["healthcare_total"]}')
    print(f'Edge Case Handling: {stats["edge_handling"]}/{stats["edge_total"]}')
    print(f'Overall Success Rate: {stats["success_rate"]:.1f}%')
    
    if stats['success_rate'] >= 75:
        print('✅ TESTS PASSED - LLM service working correctly')
    else:
        print('❌ TESTS FAILED - LLM service needs improvement')


def run_all_llm_tests():
    """Run complete simplified LLM service test suite"""
    print('=== LLM SERVICE TEST SUITE ===')
    
    api_result = test_api_key_configuration()
    response_results = test_llm_responses()
    healthcare_results = test_healthcare_context()
    edge_results = test_edge_cases()
    
    stats = calculate_simplified_test_statistics(api_result, response_results, healthcare_results, edge_results)
    display_simplified_test_summary(stats)
    
    return stats


if __name__ == '__main__':
    run_all_llm_tests() 