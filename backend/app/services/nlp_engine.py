import random

def extract_skills_from_resume(resume_text: str) -> list[str]:
    """
    Mock function simulating an NLP engine that reads text and extracts skills.
    In a real system, this would use model like BERT, SpaCy, or an LLM.
    """
    possible_skills = ["Python", "Java", "Docker", "AWS", "Machine Learning", "NLP", "React", "SQL", "WorkDay", "Generative AI", "C++", "Go", "Cybersecurity"]
    
    # Simulate extraction by checking for keywords and adding a little randomness
    extracted = []
    text_lower = resume_text.lower()
    for skill in possible_skills:
        if skill.lower() in text_lower:
            extracted.append(skill)
            
    # Simulate finding hidden or implicit skills via AI inference
    if len(extracted) > 0 and random.random() > 0.5:
         extra = random.choice([s for s in possible_skills if s not in extracted])
         extracted.append(extra)
         
    return extracted

def calculate_candidate_score(resume_text: str, job_description: str) -> float:
    """
    Mock function simulating a predictive analytics scoring system.
    Returns a score between 0 and 100 based on keyword overlap and semantic matching.
    """
    resume_skills = set(extract_skills_from_resume(resume_text))
    job_skills = set(extract_skills_from_resume(job_description))
    
    if not job_skills:
        return 50.0 # Default if job description is empty/generic
        
    overlap = len(resume_skills.intersection(job_skills))
    
    # Base score on direct match overlap
    base_score = (overlap / len(job_skills)) * 100 if len(job_skills) > 0 else 0
    
    # Add semantic "AI" variance (simulating reasoning capability)
    ai_variance = random.uniform(-10.0, 15.0)
    
    final_score = max(0.0, min(100.0, base_score + ai_variance))
    return round(final_score, 1)

def generate_chatbot_response(user_message: str, candidate_context: dict) -> str:
    """
    Mock function for the HR chatbot logic simulating Generative AI interactions.
    """
    message = user_message.lower()
    
    if "status" in message:
         return f"The current status for candidate {candidate_context.get('name', 'Unknown')} is '{candidate_context.get('status', 'Pending Review')}'."
    elif "score" in message:
         return f"{candidate_context.get('name', 'The candidate')} received an AI matching score of {candidate_context.get('score', 'N/A')}."
    elif "skills" in message:
         skills = ", ".join(candidate_context.get("skills", []))
         return f"The detected skills for {candidate_context.get('name', 'the candidate')} include: {skills if skills else 'None detected'}."
    else:
         return "I am the AI Hiring Assistant. I can help you check candidate status, scores, or skills. How can I assist you with this profile?"
