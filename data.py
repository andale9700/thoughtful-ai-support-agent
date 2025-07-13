"""
Hardcoded Q&A dataset for Thoughtful AI Support Agent
Contains the 5 predefined questions and answers from project requirements
"""

THOUGHTFUL_AI_QA = [
    {
        "question": "What does the eligibility verification agent (EVA) do?",
        "answer": "EVA automates the process of verifying a patient's eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."
    },
    {
        "question": "What does the claims processing agent (CAM) do?",
        "answer": "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements."
    },
    {
        "question": "How does the payment posting agent (PHIL) work?",
        "answer": "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden."
    },
    {
        "question": "Tell me about Thoughtful AI's Agents.",
        "answer": "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others."
    },
    {
        "question": "What are the benefits of using Thoughtful AI's agents?",
        "answer": "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
    }
]

def get_all_questions():
    """Helper function to get all questions for display purposes"""
    return [qa["question"] for qa in THOUGHTFUL_AI_QA]

def get_all_answers():
    """Helper function to get all answers for reference"""
    return [qa["answer"] for qa in THOUGHTFUL_AI_QA]

def get_question_count():
    """Helper function to get the total number of predefined questions"""
    return len(THOUGHTFUL_AI_QA) 