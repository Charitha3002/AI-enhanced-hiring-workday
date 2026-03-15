from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import resume, interview, workday

app = FastAPI(
    title="AI-Enhanced Hiring API",
    description="Backend API for AI-Enhanced Hiring in WorkDay system",
    version="1.0.0"
)

# Allow CORS for the dashboard frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(resume.router, prefix="/api/resume", tags=["resume"])
app.include_router(interview.router, prefix="/api/interview", tags=["interview"])
app.include_router(workday.router, prefix="/api/workday", tags=["workday"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI-Enhanced Hiring API"}
