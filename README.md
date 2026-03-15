# AI-Enhanced Hiring in WorkDay
**Transforming Talent Acquisition with Intelligent Automation**

This repository contains the mock implementation for the **AI-Enhanced Hiring in WorkDay** system. It demonstrates integrating predictive analytics, Natural Language Processing (NLP), and Generative AI to automate resume screening, technical vetting, and candidate interactions.

## Project Structure

```text
ai_enhanced_hiring/
├── backend/
│   ├── app/
│   │   ├── api/          # API Routers (resume, interview, workday mocks)
│   │   ├── services/     # AI Simulation logic (code llama, nlp engine, gen video)
│   │   └── main.py       # FastAPI application entry point
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── index.html        # Analytics Dashboard & Chatbot UI
│   ├── styles.css        # Premium Dark Mode / Glassmorphism UI
│   └── app.js            # UI Logic and API Integrations
├── docs/                 
│   └── Service_Management_Plan.md # ITIL standard SMP document
├── docker-compose.yml    # Cloud deployment configuration
└── README.md
```

## Features Demonstrated
1. **Resume Screening (NLP):** Extracts technical skills from plain text and compares them contextually to target job roles.
2. **Generative AI Avatar Interviews:** Mocks the creation and analysis of behavioral video interviews.
3. **Technical Vetting (Code Llama):** Evaluates candidate code submissions and scores them based on logic and specific language constructs.
4. **WorkDay Sync:** Simulates writing processed candidate data back to the core ATS.
5. **HR Assistant Chatbot:** Allows recruiters to query candidate statuses and skills interactively via a conversational interface.

## How to Run

### Method 1: Local Docker Deployment (Recommended)
1. Ensure Docker and Docker Compose are installed.
2. From the root directory, run:
   ```bash
   docker-compose up --build
   ```
3. Open `http://localhost` in your browser. The backend API is available at `http://localhost:8000/docs`.

### Method 2: Manual Python + Static HTML
1. Open the backend directory and install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
2. Run the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```
3. Open `frontend/index.html` directly in your browser...
