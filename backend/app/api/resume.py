from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from ..services.nlp_engine import extract_skills_from_resume, calculate_candidate_score, generate_chatbot_response

router = APIRouter()

class ResumeUploadRequest(BaseModel):
    candidate_name: str
    resume_text: str
    target_job_description: str

class ResumeAnalysisResponse(BaseModel):
    candidate_name: str
    extracted_skills: List[str]
    ai_matching_score: float
    recommendation: str

class ChatbotRequest(BaseModel):
    message: str
    candidate_context: dict

@router.post("/analyze", response_model=ResumeAnalysisResponse)
def analyze_resume(request: ResumeUploadRequest):
    """
    Endpoint for the AI to screen a candidate's resume against a job description.
    """
    skills = extract_skills_from_resume(request.resume_text)
    score = calculate_candidate_score(request.resume_text, request.target_job_description)
    
    # AI-driven recommendation logic
    if score >= 80:
        recommendation = "Fast-track to Technical Vetting"
    elif score >= 60:
        recommendation = "Schedule AI Avatar Interview"
    else:
        recommendation = "Reject automatically based on predictive analytics"
        
    return ResumeAnalysisResponse(
        candidate_name=request.candidate_name,
        extracted_skills=skills,
        ai_matching_score=score,
        recommendation=recommendation
    )

@router.post("/chat")
def hr_chatbot(request: ChatbotRequest):
    """
    Endpoint for users/recruiters to interact with the AI assistant regarding a candidate.
    """
    response_text = generate_chatbot_response(request.message, request.candidate_context)
    return {"reply": response_text}
