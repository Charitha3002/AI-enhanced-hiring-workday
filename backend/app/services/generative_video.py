import uuid
import random

def generate_avatar_interview_session(candidate_id: str, job_role: str) -> dict:
    """
    Mock function simulating the generation of an interactive generative AI-powered
    voice and avatar screening session.
    """
    session_id = str(uuid.uuid4())
    
    # Simulate selecting an appropriate avatar and generating questions
    interview_questions = [
        f"Can you explain your experience related to {job_role}?",
        "Describe a time you solved a complex problem under pressure.",
        "How do you handle disagreements within a team setting?"
    ]
    
    return {
        "session_id": session_id,
        "candidate_id": candidate_id,
        "avatar_profile": {
            "name": "Alex (AI Interviewer)",
            "voice_style": "professional, empathetic",
            "video_stream_url": f"https://mock-ai-video-stream.internal/stream/{session_id}"
        },
        "questions": interview_questions,
        "status": "Ready",
        "message": "Generative Video session initialized successfully."
    }

def analyze_interview_video(session_id: str, candidate_video_feed_data: bytes) -> dict:
    """
    Mock function simulating the analysis of the candidate's video responses
    for behavioral and sentimental analysis.
    """
    
    # Simulate behavioral analysis via Generative AI
    confidence = random.uniform(60.0, 95.0)
    clarity = random.uniform(70.0, 99.0)
    
    overall_sentiment = "Positive" if (confidence + clarity) / 2 > 75 else "Neutral"
    
    return {
         "session_id": session_id,
         "behavioral_score": {
             "confidence": round(confidence, 1),
             "clarity_of_speech": round(clarity, 1)
         },
         "overall_sentiment": overall_sentiment,
         "recommendation_engine": "Strongly Consider" if overall_sentiment == "Positive" else "Needs Secondary Review"
    }
