from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class CandidateSyncRequest(BaseModel):
    candidate_id: str
    name: str
    status: str
    score: float
    notes: str

@router.post("/sync")
def sync_candidate_to_workday(request: CandidateSyncRequest):
    """
    Mock endpoint simulating the integration with the WorkDay HRMS API.
    In production, this would use OAuth2 to connect to the WorkDay tenant
    and update the applicant tracking system (ATS) record.
    """
    
    # Simulate API interaction delay and logging
    workday_response = {
        "status": "success",
        "workday_record_id": f"WD-{request.candidate_id[-6:]}",
        "message": f"Candidate {request.name} successfully synced to WorkDay Integration Hub.",
        "pushed_data": {
            "status": request.status,
            "ai_score": request.score,
            "recruiter_notes": request.notes
        }
    }
    
    return workday_response

@router.get("/status/{candidate_id}")
def get_workday_status(candidate_id: str):
    """
    Mock endpoint retrieving real-time status from WorkDay.
    """
    return {
        "candidate_id": candidate_id,
        "workday_status": "Interview Scheduled",
        "last_updated": "2026-03-12T10:00:00Z"
    }
