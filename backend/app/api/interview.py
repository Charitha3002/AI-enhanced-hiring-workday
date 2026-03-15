from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..services.generative_video import generate_avatar_interview_session, analyze_interview_video
from ..services.code_llama import validate_code_submission

router = APIRouter()

class SessionRequest(BaseModel):
    candidate_id: str
    job_role: str

class CodeSubmissionRequest(BaseModel):
    candidate_id: str
    expected_language: str
    task_description: str
    candidate_code: str

@router.post("/avatar/session")
def create_avatar_session(request: SessionRequest):
    """
    Initializes a simulated Generative AI voice/avatar screening session.
    """
    session_data = generate_avatar_interview_session(request.candidate_id, request.job_role)
    return session_data

@router.post("/avatar/analyze")
def analyze_avatar_video(session_id: str):
    """
    Analyzes the video feed from the candidate's interview session.
    (Mocked with a simple request without actual bytes).
    """
    analysis = analyze_interview_video(session_id, b"mock_video_data")
    return analysis

@router.post("/code/validate")
def validate_code(request: CodeSubmissionRequest):
    """
    Passes candidate code submissions to the Code Llama service for automated validation.
    """
    validation_result = validate_code_submission(
        candidate_code=request.candidate_code,
        expected_language=request.expected_language,
        task_description=request.task_description
    )
    return {
        "candidate_id": request.candidate_id,
        "evaluation": validation_result
    }
