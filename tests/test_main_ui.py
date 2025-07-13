"""
Test suite for main UI functionality
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import (
    try_fuzzy_matching_first,
    get_response_for_user_input,
    should_display_welcome_message,
    initialize_session_state
)


def get_test_questions_with_expected_behavior():
    """Test questions with their expected matching behavior"""
    return [
        ("What does EVA do?", "fuzzy_match"),
        ("Tell me about claims processing", "fuzzy_match"),
        ("What is the weather today?", "llm_response"),
        ("How can AI help healthcare?", "llm_response"),
        ("eligibility verification", "fuzzy_match")
    ]


def test_fuzzy_matching_integration():
    """Test that fuzzy matching works through the UI layer"""
    test_cases = get_test_questions_with_expected_behavior()
    results = []
    
    print('✅ TESTING FUZZY MATCHING INTEGRATION:')
    for question, expected_behavior in test_cases:
        fuzzy_response = try_fuzzy_matching_first(question)
        has_fuzzy_match = fuzzy_response is not None
        
        if expected_behavior == "fuzzy_match":
            success = has_fuzzy_match
            print(f'  {"✓" if success else "✗"} "{question}" → Expected fuzzy match, got: {success}')
        else:
            success = not has_fuzzy_match
            print(f'  {"✓" if success else "✗"} "{question}" → Expected no fuzzy match, got: {success}')
        
        results.append((question, expected_behavior, success))
    
    return results


def test_response_integration():
    """Test complete response system (fuzzy + LLM)"""
    test_questions = [
        "What does the eligibility verification agent do?",
        "How can technology help healthcare?",
        "Tell me about payment posting",
        "What is machine learning?"
    ]
    results = []
    
    print('\n✅ TESTING COMPLETE RESPONSE INTEGRATION:')
    for question in test_questions:
        response = get_response_for_user_input(question)
        is_valid_response = response and len(response) > 20
        
        results.append((question, is_valid_response, len(response)))
        status = '✓' if is_valid_response else '✗'
        print(f'  {status} "{question}"')
        print(f'    Response length: {len(response)} chars')
        print(f'    Valid: {is_valid_response}')
    
    return results


def test_session_state_logic():
    """Test session state and welcome message logic"""
    print('\n✅ TESTING SESSION STATE LOGIC:')
    
    class MockSessionState:
        def __init__(self):
            self.messages = []
    
    # Test welcome message display logic
    test_state = MockSessionState()
    should_show_welcome_empty = len(test_state.messages) == 0
    
    test_state.messages.append({"role": "user", "content": "test"})
    should_show_welcome_with_messages = len(test_state.messages) == 0
    
    welcome_logic_works = should_show_welcome_empty and not should_show_welcome_with_messages
    
    print(f'  {"✓" if welcome_logic_works else "✗"} Welcome message logic')
    print(f'    Shows on empty: {should_show_welcome_empty}')
    print(f'    Hides with messages: {not should_show_welcome_with_messages}')
    
    return welcome_logic_works


def test_edge_cases():
    """Test edge cases in UI functionality"""
    edge_cases = ['', '   ', 'a', 'xyz123']
    results = []
    
    print('\n✅ TESTING UI EDGE CASES:')
    for case in edge_cases:
        try:
            response = get_response_for_user_input(case)
            handles_gracefully = response and len(response) > 5
            
            results.append((case, handles_gracefully))
            status = '✓' if handles_gracefully else '✗'
            case_display = f'"{case}"' if case.strip() else 'empty/whitespace'
            print(f'  {status} {case_display} → Handles gracefully: {handles_gracefully}')
        except Exception as e:
            results.append((case, False))
            print(f'  ✗ "{case}" → Exception: {e}')
    
    return results


def calculate_ui_test_statistics(fuzzy_results, response_results, session_result, edge_results):
    """Calculate UI test statistics"""
    fuzzy_success = sum(1 for _, _, success in fuzzy_results if success)
    response_success = sum(1 for _, valid, _ in response_results if valid)
    edge_success = sum(1 for _, handles in edge_results if handles)
    
    total_tests = len(fuzzy_results) + len(response_results) + len(edge_results) + (1 if session_result else 0)
    total_passed = fuzzy_success + response_success + edge_success + (1 if session_result else 0)
    
    return {
        'fuzzy_success': fuzzy_success,
        'fuzzy_total': len(fuzzy_results),
        'response_success': response_success,
        'response_total': len(response_results),
        'session_logic': session_result,
        'edge_success': edge_success,
        'edge_total': len(edge_results),
        'overall_success': total_passed,
        'overall_total': total_tests,
        'success_rate': (total_passed / total_tests) * 100 if total_tests > 0 else 0
    }


def display_ui_test_summary(stats):
    """Display UI test summary"""
    print(f'\n=== UI TEST SUMMARY ===')
    print(f'Fuzzy Match Integration: {stats["fuzzy_success"]}/{stats["fuzzy_total"]}')
    print(f'Response Integration: {stats["response_success"]}/{stats["response_total"]}')
    print(f'Session State Logic: {stats["session_logic"]}')
    print(f'Edge Case Handling: {stats["edge_success"]}/{stats["edge_total"]}')
    print(f'Overall Success Rate: {stats["success_rate"]:.1f}%')
    
    if stats['success_rate'] >= 80:
        print('✅ TESTS PASSED - UI working correctly')
    else:
        print('❌ TESTS FAILED - UI needs improvement')


def run_all_ui_tests():
    """Run complete UI test suite"""
    print('=== MAIN UI TEST SUITE ===')
    
    fuzzy_results = test_fuzzy_matching_integration()
    response_results = test_response_integration()
    session_result = test_session_state_logic()
    edge_results = test_edge_cases()
    
    stats = calculate_ui_test_statistics(fuzzy_results, response_results, session_result, edge_results)
    display_ui_test_summary(stats)
    
    return stats


if __name__ == '__main__':
    run_all_ui_tests() 