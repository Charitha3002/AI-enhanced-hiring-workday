document.addEventListener('DOMContentLoaded', () => {
    
    // --- MOCK DATA ---
    const initialCandidates = [
        { id: "wd-001", name: "Alice Chen", role: "Sr. Python Dev", score: 92.5, status: "Interview Scheduled" },
        { id: "wd-002", name: "Marcus Johnson", role: "Backend Engineer", score: 85.0, status: "Tech Vetting" },
        { id: "wd-003", name: "Sarah Lee", role: "Data Scientist", score: 65.5, status: "Under Review" }
    ];
    
    let activeCandidateContext = initialCandidates[0];

    // --- DOM ELEMENTS ---
    const candidatesList = document.getElementById('candidatesList');
    const uploadBtn = document.getElementById('uploadResumeBtn');
    const modal = document.getElementById('uploadModal');
    const closeBtn = document.querySelector('.close-btn');
    const uploadForm = document.getElementById('uploadForm');
    const chatInput = document.getElementById('chatInput');
    const sendChatBtn = document.getElementById('sendChatBtn');
    const chatMessages = document.getElementById('chatMessages');

    // --- RENDER TABLE ---
    function renderTable() {
        candidatesList.innerHTML = '';
        initialCandidates.sort((a,b) => b.score - a.score).forEach(c => {
            const scoreClass = c.score >= 80 ? 'score-high' : 'score-med';
            
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td><strong>${c.name}</strong><br><small style="color:var(--text-muted)">${c.id}</small></td>
                <td>${c.role}</td>
                <td><span class="score-badge ${scoreClass}">${c.score}%</span></td>
                <td>${c.status}</td>
                <td>
                    <button class="secondary-btn" onclick="setActiveContext('${c.id}')">Review</button>
                    ${c.score >= 80 ? '<button class="secondary-btn" style="margin-left: 8px; border-color: var(--accent-primary); color: var(--accent-primary)">GenAI Interview</button>' : ''}
                </td>
            `;
            candidatesList.appendChild(tr);
        });
    }

    renderTable();

    // Context switching for Chatbot
    window.setActiveContext = (id) => {
        activeCandidateContext = initialCandidates.find(c => c.id === id);
        addMessage(`I am now focusing on ${activeCandidateContext.name}. How can I help?`, 'bot');
    };

    // --- MODAL LOGIC ---
    uploadBtn.onclick = () => modal.style.display = "flex";
    closeBtn.onclick = () => modal.style.display = "none";
    window.onclick = (event) => {
        if (event.target == modal) modal.style.display = "none";
    };

    uploadForm.onsubmit = async (e) => {
        e.preventDefault();
        
        const btn = uploadForm.querySelector('button');
        btn.textContent = "Processing with NLP Engine...";
        btn.disabled = true;

        const name = document.getElementById('candidateName').value;
        const jobDesc = document.getElementById('jobDesc').value;
        const resumeText = document.getElementById('resumeText').value;

        try {
            // Using API route if local server is running, otherwise mock
            const response = await fetch('http://127.0.0.1:8000/api/resume/analyze', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    candidate_name: name,
                    target_job_description: jobDesc,
                    resume_text: resumeText
                })
            });
            
            let result;
            if(response.ok) {
                result = await response.json();
            } else {
                throw new Error("Local server not running, using mocked result.");
            }

            addNewCandidateFromAPI(result, jobDesc);

        } catch (error) {
            console.warn(error.message);
            // Mock integration when Fastapi is not running
            setTimeout(() => {
                const mockedScore = Math.floor(Math.random() * 40) + 60; // Random 60-100
                const result = {
                    candidate_name: name,
                    ai_matching_score: mockedScore,
                    recommendation: mockedScore > 80 ? "Fast-track" : "Review"
                };
                addNewCandidateFromAPI(result, jobDesc);
            }, 1500);
        }

        modal.style.display = "none";
        btn.textContent = "Analyze with AI";
        btn.disabled = false;
        uploadForm.reset();
    };

    function addNewCandidateFromAPI(result, role) {
        const id = "wd-nt-" + Math.floor(Math.random() * 1000);
        const newCand = {
            id: id,
            name: result.candidate_name,
            role: role,
            score: result.ai_matching_score,
            status: result.ai_matching_score >= 80 ? "Fast-Tracked" : "Under Review",
            skills: result.extracted_skills || ["Python", "SQL"]
        };
        initialCandidates.push(newCand);
        activeCandidateContext = newCand;
        renderTable();
        addMessage(`Successfully analyzed profile for ${result.candidate_name}. They scored ${result.ai_matching_score}% and have been synced to WorkDay.`, 'bot');
    }

    // --- CHATBOT LOGIC ---
    function addMessage(text, sender) {
        const div = document.createElement('div');
        div.className = `message ${sender}`;
        div.innerHTML = `<div class="msg-bubble">${text}</div>`;
        chatMessages.appendChild(div);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    async function handleChat() {
        const msg = chatInput.value.trim();
        if(!msg) return;

        addMessage(msg, 'user');
        chatInput.value = '';

        try {
            const response = await fetch('http://127.0.0.1:8000/api/resume/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    message: msg,
                    candidate_context: activeCandidateContext
                })
            });
            
            if(response.ok) {
                const data = await response.json();
                addMessage(data.reply, 'bot');
            } else {
                throw new Error("Server not available");
            }
        } catch (error) {
             console.warn("Using offline mock for chat.");
             setTimeout(() => {
                 let reply = "I'm the AI Assistant. How can I help?";
                 if(msg.toLowerCase().includes('score')) reply = `${activeCandidateContext.name}'s AI Match score is ${activeCandidateContext.score}%.`;
                 else if(msg.toLowerCase().includes('status')) reply = `The WorkDay status for ${activeCandidateContext.name} is "${activeCandidateContext.status}".`;
                 else if(msg.toLowerCase().includes('skills') && activeCandidateContext.skills) reply = `Detected skills include: ${activeCandidateContext.skills.join(', ')}.`;
                 addMessage(reply, 'bot');
             }, 600);
        }
    }

    sendChatBtn.onclick = handleChat;
    chatInput.onkeypress = (e) => { if(e.key === 'Enter') handleChat(); };
});
