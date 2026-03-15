import time
import random

def validate_code_submission(candidate_code: str, expected_language: str, task_description: str) -> dict:
    """
    Mock function simulating a call to Code Llama (or similar LLM model)
    to perform automated technical vetting and validation of a candidate's code.
    """
    
    # Simulate processing delay of an LLM
    time.sleep(1)
    
    # In a real system, you would construct a prompt:
    # "Evaluate this {expected_language} code for the task: {task_description}. Here is the code: {candidate_code}"
    # and send it to the Code Llama inference endpoint.
    
    # Mocking the AI's analysis
    if len(candidate_code.strip()) < 10:
        return {
            "is_valid": False,
            "score": 0.0,
            "feedback": "Code submission is empty or too short. Unable to evaluate logic."
        }
        
    base_score = 70.0
    feedback = "Good fundamental understanding. "
    
    if expected_language.lower() in candidate_code.lower():
        base_score += 10.0
        feedback += f"Correctly utilized {expected_language} constructs. "
        
    # Simulate AI finding optimizations or bugs
    ai_evaluation = random.choice([
         {"bonus": 15.0, "msg": "Highly optimized and concise solution!"},
         {"bonus": 5.0, "msg": "Adequate solution, but could be refactored for better performance."},
         {"bonus": -10.0, "msg": "Logical errors found in edge case handling."}
    ])
    
    final_score = base_score + ai_evaluation["bonus"]
    feedback += ai_evaluation["msg"]
    
    return {
        "is_valid": final_score >= 60.0,
        "score": round(min(100.0, max(0.0, final_score)), 1),
        "feedback": feedback
    }
