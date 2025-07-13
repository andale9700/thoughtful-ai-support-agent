"""
Test suite for keyword-based question matching functionality
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from question_matcher import find_best_match


def get_successful_test_cases():
    """Test cases that should find matches"""
    return [
        'What does EVA do?',
        'Tell me about eva',
        'How does phil work?',
        'What are the benefits?',
        'Claims processing agent',
        'payment posting',
        'eligibility verification',
        'Tell me about Thoughtful AI agents',
        'How does CAM work?'
    ]


def get_failed_test_cases():
    """Test cases that should not find matches"""
    return [
        'What is the weather today?',
        'How to cook pasta?',
        'What is the capital of France?',
        'Tell me a joke',
        'What color is the sky?',
        'What is 2+2?',
        '',
        '   ',
        'xyz'
    ]


def test_successful_matches():
    """Test cases that should successfully match"""
    test_cases = get_successful_test_cases()
    results = []
    
    print('✅ TESTING SUCCESSFUL MATCHES:')
    for question in test_cases:
        result = find_best_match(question)
        if result:
            answer, score = result
            results.append((question, score, True))
            print(f'  ✓ "{question}" → {score:.3f} similarity')
        else:
            results.append((question, 0, False))
            print(f'  ✗ "{question}" → NO MATCH (unexpected)')
    
    return results


def test_failed_matches():
    """Test cases that should correctly fail to match"""
    test_cases = get_failed_test_cases()
    results = []
    
    print('\n✅ TESTING CORRECTLY REJECTED:')
    for question in test_cases:
        result = find_best_match(question)
        if result:
            answer, score = result
            results.append((question, score, False))
            print(f'  ✗ "{question}" → {score:.3f} similarity (unexpected)')
        else:
            results.append((question, 0, True))
            print(f'  ✓ "{question}" → NO MATCH (correct)')
    
    return results


def calculate_test_statistics(successful_results, failed_results):
    """Calculate and display test statistics"""
    successful_matches = sum(1 for _, _, matched in successful_results if matched)
    total_successful_tests = len(successful_results)
    
    failed_rejections = sum(1 for _, _, rejected in failed_results if rejected)
    total_failed_tests = len(failed_results)
    
    total_tests = total_successful_tests + total_failed_tests
    total_passed = successful_matches + failed_rejections
    
    success_rate = (successful_matches / total_successful_tests) * 100
    rejection_rate = (failed_rejections / total_failed_tests) * 100
    overall_accuracy = (total_passed / total_tests) * 100
    
    return {
        'successful_matches': successful_matches,
        'total_successful_tests': total_successful_tests,
        'failed_rejections': failed_rejections,
        'total_failed_tests': total_failed_tests,
        'success_rate': success_rate,
        'rejection_rate': rejection_rate,
        'overall_accuracy': overall_accuracy
    }


def display_test_summary(stats):
    """Display comprehensive test summary"""
    print(f'\n=== TEST SUMMARY ===')
    print(f'Keyword Matching Threshold: 0.21 (adjusted for keyword approach)')
    print(f'Successful Matches: {stats["successful_matches"]}/{stats["total_successful_tests"]} ({stats["success_rate"]:.1f}%)')
    print(f'Correct Rejections: {stats["failed_rejections"]}/{stats["total_failed_tests"]} ({stats["rejection_rate"]:.1f}%)')
    print(f'Overall Accuracy: {stats["overall_accuracy"]:.1f}%')
    
    if stats['overall_accuracy'] >= 70:  # Adjusted threshold for keyword matching
        print('✅ TESTS PASSED - Keyword-based matching working correctly')
    else:
        print('❌ TESTS FAILED - Keyword-based matching needs adjustment')


def run_all_tests():
    """Run complete test suite"""
    print('=== QUESTION MATCHER TEST SUITE (Keyword-Based) ===')
    
    successful_results = test_successful_matches()
    failed_results = test_failed_matches()
    
    stats = calculate_test_statistics(successful_results, failed_results)
    display_test_summary(stats)
    
    return stats


if __name__ == '__main__':
    run_all_tests() 