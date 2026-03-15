# Service Management Plan (SMP)
**Project:** AI-Enhanced Hiring in WorkDay
**Version:** 1.0
**Date:** March 2026

## 1. Executive Summary
This Service Management Plan outlines the strategies and processes for managing the AI-Enhanced Hiring system integrated into the WorkDay HRMS. The system utilizes predictive analytics, NLP, Generative AI video, and Code Llama to automate the talent acquisition pipeline. This plan ensures system reliability, continuous improvement, and seamless user experiences.

## 2. Incident Management Strategy
**Objective:** Restore normal service operation as quickly as possible and minimize the adverse impact on business operations.

- **Categorization:** 
  - **P1 (Critical):** Core AI processing (NLP Engine/Code Llama) offline, directly preventing applicant processing.
  - **P2 (High):** WorkDay sync failure causing data discrepancy.
  - **P3 (Medium):** Dashboard metrics UI glitch or chatbot degraded performance.
  - **P4 (Low):** Minor UI styling issues.
- **Workflow:**
  1. **Detection & Recording:** Automated alerts from monitoring tools (e.g., Datadog, Prometheus/Grafana) logging incidents.
  2. **Initial Support & Resolution:** L1 support attempts resolution using knowledge base articles.
  3. **Escalation:** L2/L3 (Platform Engineering/AI Data Science team) investigating complex model degradations or robust system failures.
  4. **Post-Incident Review (PIR):** Root Cause Analysis (RCA) to be documented within 48 hours for P1/P2 incidents.

## 3. Knowledge Management Strategy
**Objective:** Share perspectives, ideas, experience, and information to ensure that these are available in the right place at the right time.

- **Knowledge Base (KB):** Maintained centrally via internal wiki (e.g., Confluence). 
- **Documentation Types:**
  - *Standard Operating Procedures (SOPs)* for restarting AI pipelines.
  - *Model Training Logs* documenting the continuous feedback loop for NLP and Generative AI.
  - *Troubleshooting Guides* for common Code Llama timeout issues.
- **Review Cycle:** All KBs are reviewed quarterly or immediately following a major release affecting the HR screening workflows.

## 4. Service Transition Management Strategy
**Objective:** Ensure that new, modified, or retired services meet the expectations of the business as documented in the service strategy.

- **Change Advisory Board (CAB):** A board consisting of HR Leadership, IT Ops, and Lead Data Scientists must approve all systemic changes to model algorithms or ATS (Applicant Tracking System) logic.
- **Release Management:**
  - **Staging:** All new AI features (e.g., new generative voice tuning) must be tested in a UAT (User Acceptance Testing) WorkDay Sandbox.
  - **Deployment:** Blue/Green deployment strategy via Kubernetes/Docker to ensure zero downtime during recruitment seasons.
- **Rollback Plan:** Automated failover to the previous stable container image if anomalous behavior (e.g., AI hallucination rates exceeding 1%) is detected within the first 24 hours of release.

## 5. Continuous Improvement
The system utilizes active learning from Recruiter feedback (e.g., disagreeing with an AI score) to fine-tune the predictive analytics weighting. Regular Service Level Agreement (SLA) reviews are conducted monthly.
