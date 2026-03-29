import streamlit as st
import json
from datetime import date, timedelta
from pathlib import Path

# ─── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Engineer Switch Tracker",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Persist state in a local JSON file ───────────────────────────────────────
DATA_FILE = Path("tracker_data.json")

def load_data():
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text())
        except Exception:
            return {}
    return {}

def save_data(data):
    DATA_FILE.write_text(json.dumps(data))

if "checked" not in st.session_state:
    st.session_state.checked = load_data()

# ─── Plan definition ──────────────────────────────────────────────────────────
CAT_LABELS = {
    "dsa": "DSA", "tech": "Technical", "design": "System Design",
    "portfolio": "Portfolio", "jobsearch": "Job Search", "prep": "Prep/Admin",
}
CAT_COLORS = {
    "dsa": "#d97706", "tech": "#2563eb", "design": "#7c3aed",
    "portfolio": "#059669", "jobsearch": "#dc2626", "prep": "#6b7280",
}
CAT_BG = {
    "dsa": "#fef3c7", "tech": "#dbeafe", "design": "#ede9fe",
    "portfolio": "#d1fae5", "jobsearch": "#fee2e2", "prep": "#f3f4f6",
}

PLAN = [
    {"w": 1, "title": "Audit, Narrative & Setup", "days": [
        {"d": "Mon", "tasks": [
            {"t": "Complete full skill self-audit (rate yourself 1–5 on 20 skills)", "c": "prep"},
            {"t": "Write your professional narrative (3 key answers)", "c": "prep"},
        ]},
        {"d": "Tue", "tasks": [
            {"t": "LeetCode: Arrays & Strings — 2 Easy problems", "c": "dsa"},
            {"t": "Set up LeetCode account, bookmark NeetCode 150", "c": "dsa"},
        ]},
        {"d": "Wed", "tasks": [
            {"t": "Resume audit — list all bullets that lack a metric", "c": "prep"},
            {"t": "Research 5 target companies, note their AI stack", "c": "jobsearch"},
        ]},
        {"d": "Thu", "tasks": [
            {"t": "LeetCode: Sliding window — 2 Medium problems", "c": "dsa"},
            {"t": "DeepLearning.AI: Start RAG short course", "c": "tech"},
        ]},
        {"d": "Fri", "tasks": [
            {"t": "LeetCode: Two pointers — 2 Medium problems", "c": "dsa"},
            {"t": "Rewrite 3 resume bullets with impact metrics", "c": "prep"},
        ]},
        {"d": "Sat", "tasks": [
            {"t": "LinkedIn profile audit — update headline & about section", "c": "jobsearch"},
            {"t": "Set up application tracking spreadsheet", "c": "jobsearch"},
        ]},
        {"d": "Sun", "tasks": [
            {"t": "Review week 1 — what was hardest? Adjust schedule", "c": "prep"},
            {"t": "Plan 5 target companies to apply to next week", "c": "jobsearch"},
        ]},
    ]},
    {"w": 2, "title": "Resume v1 + DSA Hashing", "days": [
        {"d": "Mon", "tasks": [
            {"t": "LeetCode: Hashing — 2 Medium problems", "c": "dsa"},
            {"t": "Complete RAG short course (DeepLearning.AI)", "c": "tech"},
        ]},
        {"d": "Tue", "tasks": [
            {"t": "Finalize resume v1 — run through Jobscan against 1 JD", "c": "prep"},
            {"t": "LeetCode: Prefix sum — 2 Medium problems", "c": "dsa"},
        ]},
        {"d": "Wed", "tasks": [
            {"t": "LangChain: Build a simple RAG chain from scratch", "c": "tech"},
            {"t": "LeetCode: 1 Medium timed (30 min limit)", "c": "dsa"},
        ]},
        {"d": "Thu", "tasks": [
            {"t": "Apply to 3 roles — fully tailored resumes", "c": "jobsearch"},
            {"t": "LeetCode: Linked lists — 2 Medium problems", "c": "dsa"},
        ]},
        {"d": "Fri", "tasks": [
            {"t": "DeepLearning.AI: Functions & Tools with LangChain course", "c": "tech"},
            {"t": "LeetCode: Stacks & queues — 2 Medium problems", "c": "dsa"},
        ]},
        {"d": "Sat", "tasks": [
            {"t": "Portfolio Project 1 kickoff: scaffold RAG chatbot repo", "c": "portfolio"},
            {"t": "Write architecture diagram for Project 1", "c": "portfolio"},
        ]},
        {"d": "Sun", "tasks": [
            {"t": "Review AI system design framework (Phase 4.1 in roadmap)", "c": "design"},
            {"t": "Watch 1 system design video on YouTube", "c": "design"},
        ]},
    ]},
    {"w": 3, "title": "Agents Depth + Binary Search", "days": [
        {"d": "Mon", "tasks": [
            {"t": "LeetCode: Binary search basics — 2 Medium problems", "c": "dsa"},
            {"t": "DeepLearning.AI: AI Agents in LangGraph course", "c": "tech"},
        ]},
        {"d": "Tue", "tasks": [
            {"t": "LeetCode: Binary search on answer space — 2 Medium", "c": "dsa"},
            {"t": "LangGraph: Build a simple ReAct agent with 2 tools", "c": "tech"},
        ]},
        {"d": "Wed", "tasks": [
            {"t": "Apply to 3–4 roles with tailored resumes", "c": "jobsearch"},
            {"t": "LeetCode: 1 timed Medium (30 min limit)", "c": "dsa"},
        ]},
        {"d": "Thu", "tasks": [
            {"t": "Portfolio Project 1: Add ChromaDB + embeddings layer", "c": "portfolio"},
            {"t": "LeetCode: Trees DFS — 2 Medium problems", "c": "dsa"},
        ]},
        {"d": "Fri", "tasks": [
            {"t": "System design: Design a PDF Q&A system (write it out)", "c": "design"},
            {"t": "LeetCode: Trees BFS — 2 Medium problems", "c": "dsa"},
        ]},
        {"d": "Sat", "tasks": [
            {"t": "DeepLearning.AI: Multi-Agent Systems with CrewAI course", "c": "tech"},
            {"t": "Reach out to 2 people at target companies for referrals", "c": "jobsearch"},
        ]},
        {"d": "Sun", "tasks": [
            {"t": "Review week 3 LeetCode — revisit any incorrect solutions", "c": "dsa"},
            {"t": "Polish Project 1: add basic UI (Streamlit or Gradio)", "c": "portfolio"},
        ]},
    ]},
    {"w": 4, "title": "LLM Eval + Tree Patterns", "days": [
        {"d": "Mon", "tasks": [
            {"t": "LeetCode: BST patterns — 2 Medium problems", "c": "dsa"},
            {"t": "RAGAS docs: understand metrics (faithfulness, relevancy)", "c": "tech"},
        ]},
        {"d": "Tue", "tasks": [
            {"t": "Add RAGAS evaluation to Project 1 chatbot", "c": "portfolio"},
            {"t": "LeetCode: Level-order traversal problems — 2 Medium", "c": "dsa"},
        ]},
        {"d": "Wed", "tasks": [
            {"t": "Apply to 4–5 roles — use referral contacts where possible", "c": "jobsearch"},
            {"t": "LeetCode: 1 timed Medium (25 min limit)", "c": "dsa"},
        ]},
        {"d": "Thu", "tasks": [
            {"t": "LangSmith: Integrate tracing into Project 1", "c": "tech"},
            {"t": "LeetCode: Graph BFS — 2 Medium problems", "c": "dsa"},
        ]},
        {"d": "Fri", "tasks": [
            {"t": "System design: Design a real-time AI customer support agent", "c": "design"},
            {"t": "LeetCode: Graph DFS — 2 Medium problems", "c": "dsa"},
        ]},
        {"d": "Sat", "tasks": [
            {"t": "Deploy Project 1 live on Streamlit Cloud or HF Spaces", "c": "portfolio"},
            {"t": "Write README with architecture diagram + benchmark", "c": "portfolio"},
        ]},
        {"d": "Sun", "tasks": [
            {"t": "Read 2 AI engineering blog posts (Eugene Yan / Chip Huyen)", "c": "tech"},
            {"t": "LinkedIn: write a short post about Project 1", "c": "jobsearch"},
        ]},
    ]},
    {"w": 5, "title": "Graph Algorithms + Agent Project", "days": [
        {"d": "Mon", "tasks": [
            {"t": "LeetCode: Topological sort — 2 Medium problems", "c": "dsa"},
            {"t": "Kickoff Portfolio Project 2: LangGraph agent", "c": "portfolio"},
        ]},
        {"d": "Tue", "tasks": [
            {"t": "LeetCode: Union Find — 2 Medium problems", "c": "dsa"},
            {"t": "Build 3 custom tools for Project 2 agent", "c": "portfolio"},
        ]},
        {"d": "Wed", "tasks": [
            {"t": "Apply to 5 roles — track in spreadsheet", "c": "jobsearch"},
            {"t": "LeetCode: Dijkstra shortest path — 1 Medium", "c": "dsa"},
        ]},
        {"d": "Thu", "tasks": [
            {"t": "Add streaming output to Project 2 agent", "c": "portfolio"},
            {"t": "LeetCode: 2 timed Mediums (25 min each)", "c": "dsa"},
        ]},
        {"d": "Fri", "tasks": [
            {"t": "System design: Design a GitHub Copilot-style assistant", "c": "design"},
            {"t": "LeetCode: Graph revision — pick 2 hardest problems this week", "c": "dsa"},
        ]},
        {"d": "Sat", "tasks": [
            {"t": "Finalize Project 2 with retry/fallback logic + README", "c": "portfolio"},
            {"t": "Pin Project 1 & 2 on GitHub profile", "c": "portfolio"},
        ]},
        {"d": "Sun", "tasks": [
            {"t": "Reach out to 3 more referral contacts", "c": "jobsearch"},
            {"t": "System design practice — write out another design", "c": "design"},
        ]},
    ]},
    {"w": 6, "title": "DP Basics + Fine-tuning Kickoff", "days": [
        {"d": "Mon", "tasks": [
            {"t": "LeetCode: DP 1D — Fibonacci pattern, 2 Medium problems", "c": "dsa"},
            {"t": "DeepLearning.AI: Finetuning LLMs short course", "c": "tech"},
        ]},
        {"d": "Tue", "tasks": [
            {"t": "LeetCode: DP — House robber pattern, 2 Medium", "c": "dsa"},
            {"t": "Set up Colab for QLoRA fine-tuning environment", "c": "tech"},
        ]},
        {"d": "Wed", "tasks": [
            {"t": "Apply to 5 roles — increase volume", "c": "jobsearch"},
            {"t": "LeetCode: DP — Coin change pattern, 2 Medium", "c": "dsa"},
        ]},
        {"d": "Thu", "tasks": [
            {"t": "Prepare fine-tuning dataset (100–500 examples in chat format)", "c": "portfolio"},
            {"t": "LeetCode: DP 2D — Longest common subsequence, 1 Medium", "c": "dsa"},
        ]},
        {"d": "Fri", "tasks": [
            {"t": "System design: Design a RAG-based recommendation engine", "c": "design"},
            {"t": "LeetCode: DP revision — 1 timed Medium", "c": "dsa"},
        ]},
        {"d": "Sat", "tasks": [
            {"t": "Run QLoRA fine-tuning on Mistral-7B (Colab)", "c": "portfolio"},
            {"t": "Evaluate before/after model: perplexity + task accuracy", "c": "portfolio"},
        ]},
        {"d": "Sun", "tasks": [
            {"t": "LinkedIn: post about fine-tuning experience & learnings", "c": "jobsearch"},
            {"t": "Review DP patterns — re-attempt any failed problems", "c": "dsa"},
        ]},
    ]},
    {"w": 7, "title": "DP Advanced + Mock Interviews Start", "days": [
        {"d": "Mon", "tasks": [
            {"t": "LeetCode: Heaps / priority queue — 2 Medium problems", "c": "dsa"},
            {"t": "Push fine-tuned model to Hugging Face Hub", "c": "portfolio"},
        ]},
        {"d": "Tue", "tasks": [
            {"t": "LeetCode: Top-K pattern — 2 Medium problems", "c": "dsa"},
            {"t": "Write Project 3 README: why fine-tune vs. prompt?", "c": "portfolio"},
        ]},
        {"d": "Wed", "tasks": [
            {"t": "Apply to 5–6 roles", "c": "jobsearch"},
            {"t": "Schedule 1 mock interview on pramp.com or interviewing.io", "c": "prep"},
        ]},
        {"d": "Thu", "tasks": [
            {"t": "LeetCode: Intervals — merge, insert, 2 Medium problems", "c": "dsa"},
            {"t": "System design: Design a fraud detection ML system", "c": "design"},
        ]},
        {"d": "Fri", "tasks": [
            {"t": "Complete mock interview #1 — debrief + write notes", "c": "prep"},
            {"t": "LeetCode: Greedy — 2 Medium problems", "c": "dsa"},
        ]},
        {"d": "Sat", "tasks": [
            {"t": "AI coding: implement cosine similarity from scratch", "c": "tech"},
            {"t": "Implement softmax, sigmoid, ReLU in pure NumPy", "c": "tech"},
        ]},
        {"d": "Sun", "tasks": [
            {"t": "Write STAR story #1 and #2 (from your story bank)", "c": "prep"},
            {"t": "Review all system designs written so far", "c": "design"},
        ]},
    ]},
    {"w": 8, "title": "Backtracking + Portfolio Project 4", "days": [
        {"d": "Mon", "tasks": [
            {"t": "LeetCode: Backtracking — subsets, permutations, 2 Medium", "c": "dsa"},
            {"t": "Start Portfolio Project 4: LLM Evaluation Framework", "c": "portfolio"},
        ]},
        {"d": "Tue", "tasks": [
            {"t": "LeetCode: Backtracking — N-Queens, word search, 2 Medium", "c": "dsa"},
            {"t": "Integrate DeepEval into evaluation framework", "c": "portfolio"},
        ]},
        {"d": "Wed", "tasks": [
            {"t": "Apply to 5–6 roles — now at full application pace", "c": "jobsearch"},
            {"t": "Implement CI/CD for eval framework (GitHub Actions)", "c": "portfolio"},
        ]},
        {"d": "Thu", "tasks": [
            {"t": "Mock interview #2 — focus on ML/AI depth questions", "c": "prep"},
            {"t": "LeetCode: 2 timed Mediums (20 min each)", "c": "dsa"},
        ]},
        {"d": "Fri", "tasks": [
            {"t": "System design: Design a multimodal image + text search", "c": "design"},
            {"t": "AI coding: implement simple k-NN search with NumPy", "c": "tech"},
        ]},
        {"d": "Sat", "tasks": [
            {"t": "Write STAR stories #3, #4, #5", "c": "prep"},
            {"t": "Improve GitHub profile README + update pinned repos", "c": "portfolio"},
        ]},
        {"d": "Sun", "tasks": [
            {"t": "DSA full review: reattempt 5 hardest problems from weeks 1–7", "c": "dsa"},
            {"t": "Research comp ranges on Levels.fyi for 10 target companies", "c": "jobsearch"},
        ]},
    ]},
    {"w": 9, "title": "Hard Problems + System Design Depth", "days": [
        {"d": "Mon", "tasks": [
            {"t": "LeetCode: 2 Medium problems (focus on weak areas)", "c": "dsa"},
            {"t": "System design: Design a personal AI assistant with memory", "c": "design"},
        ]},
        {"d": "Tue", "tasks": [
            {"t": "LeetCode: 1 Hard problem (attempt, study solution)", "c": "dsa"},
            {"t": "Write full design doc for one of your portfolio projects", "c": "portfolio"},
        ]},
        {"d": "Wed", "tasks": [
            {"t": "Apply to 5–6 roles — follow up on 2-week-old applications", "c": "jobsearch"},
            {"t": "Mock interview #3 — full technical screen simulation", "c": "prep"},
        ]},
        {"d": "Thu", "tasks": [
            {"t": "LeetCode: 1 Hard problem", "c": "dsa"},
            {"t": "AI coding: implement TF-IDF scorer from scratch", "c": "tech"},
        ]},
        {"d": "Fri", "tasks": [
            {"t": "System design mock with a friend — 45 min, whiteboard", "c": "design"},
            {"t": "Debrief + write what you'd improve", "c": "design"},
        ]},
        {"d": "Sat", "tasks": [
            {"t": "Portfolio Project 5 kickoff: AI-powered micro-SaaS idea", "c": "portfolio"},
            {"t": "Scaffold FastAPI backend + define the core feature", "c": "portfolio"},
        ]},
        {"d": "Sun", "tasks": [
            {"t": "Write STAR stories #6 and #7", "c": "prep"},
            {"t": "Reach out to 5 more referral contacts at target companies", "c": "jobsearch"},
        ]},
    ]},
    {"w": 10, "title": "Mock Interview Ramp + Applications Peak", "days": [
        {"d": "Mon", "tasks": [
            {"t": "LeetCode: 2 timed Mediums (15 min each — interview speed)", "c": "dsa"},
            {"t": "Continue Project 5: deploy MVP to real URL", "c": "portfolio"},
        ]},
        {"d": "Tue", "tasks": [
            {"t": "Mock interview #4 — system design round", "c": "prep"},
            {"t": "Debrief: what took too long? What did you skip?", "c": "prep"},
        ]},
        {"d": "Wed", "tasks": [
            {"t": "Apply to 8+ roles (peak application week)", "c": "jobsearch"},
            {"t": "LeetCode: 1 Hard problem", "c": "dsa"},
        ]},
        {"d": "Thu", "tasks": [
            {"t": "AI coding: implement sliding window text chunker", "c": "tech"},
            {"t": "Mock interview #5 — ML conceptual depth round", "c": "prep"},
        ]},
        {"d": "Fri", "tasks": [
            {"t": "System design: Design an A/B testing platform for LLM prompts", "c": "design"},
            {"t": "LeetCode: 2 Medium problems", "c": "dsa"},
        ]},
        {"d": "Sat", "tasks": [
            {"t": "Full mock loop: coding + system design + behavioral (3 hrs)", "c": "prep"},
            {"t": "Write detailed notes on what to improve", "c": "prep"},
        ]},
        {"d": "Sun", "tasks": [
            {"t": "Revisit and finalize all 5 portfolio projects — check live links", "c": "portfolio"},
            {"t": "Update LinkedIn featured section with all live projects", "c": "jobsearch"},
        ]},
    ]},
    {"w": 11, "title": "Interview Active — Execution Mode", "days": [
        {"d": "Mon", "tasks": [
            {"t": "LeetCode: daily 1–2 problems to stay sharp", "c": "dsa"},
            {"t": "Prep company-specific research for any active interviews", "c": "prep"},
        ]},
        {"d": "Tue", "tasks": [
            {"t": "Review all 7 STAR stories — practice out loud", "c": "prep"},
            {"t": "Send follow-ups on any applications 10+ days old", "c": "jobsearch"},
        ]},
        {"d": "Wed", "tasks": [
            {"t": "Apply to 5 more roles", "c": "jobsearch"},
            {"t": "Mock system design with a different partner", "c": "design"},
        ]},
        {"d": "Thu", "tasks": [
            {"t": "LeetCode: 1 Hard problem", "c": "dsa"},
            {"t": "Read 2 engineering blog posts from target companies", "c": "prep"},
        ]},
        {"d": "Fri", "tasks": [
            {"t": "AI coding: build retry wrapper with exponential backoff", "c": "tech"},
            {"t": "Mock behavioral round — record yourself, review", "c": "prep"},
        ]},
        {"d": "Sat", "tasks": [
            {"t": "Write a blog post or LinkedIn thread on something you built", "c": "jobsearch"},
            {"t": "Engage with AI community: comment on 5 posts", "c": "jobsearch"},
        ]},
        {"d": "Sun", "tasks": [
            {"t": "Rest & recover — burnout is real, protect your energy", "c": "prep"},
            {"t": "Light review: go over your system design notes", "c": "design"},
        ]},
    ]},
    {"w": 12, "title": "Interview Loops + Negotiation Prep", "days": [
        {"d": "Mon", "tasks": [
            {"t": "LeetCode: 2 Medium problems — daily warmup", "c": "dsa"},
            {"t": "Research comp: Levels.fyi for every company in final rounds", "c": "jobsearch"},
        ]},
        {"d": "Tue", "tasks": [
            {"t": "Practice negotiation script out loud (salary + equity)", "c": "prep"},
            {"t": "Understand vesting schedules and equity cliff basics", "c": "prep"},
        ]},
        {"d": "Wed", "tasks": [
            {"t": "Apply to 5 roles — keep pipeline full even in final rounds", "c": "jobsearch"},
            {"t": "Mock full interview loop: coding + system design + behavioral", "c": "prep"},
        ]},
        {"d": "Thu", "tasks": [
            {"t": "LeetCode: 1 Hard problem", "c": "dsa"},
            {"t": "Company research: products, tech blog, recent launches", "c": "prep"},
        ]},
        {"d": "Fri", "tasks": [
            {"t": "System design: pick any from list, do under 30 min", "c": "design"},
            {"t": "Behavioral: practice 'Why this company?' answer — be specific", "c": "prep"},
        ]},
        {"d": "Sat", "tasks": [
            {"t": "Write 5 thoughtful questions to ask interviewers per company", "c": "prep"},
            {"t": "Confirm all interview logistics: links, time zones, duration", "c": "prep"},
        ]},
        {"d": "Sun", "tasks": [
            {"t": "Rest, sleep, light review only — do not cram the night before", "c": "prep"},
            {"t": "Visualize a successful interview round", "c": "prep"},
        ]},
    ]},
    {"w": 13, "title": "Final Rounds + Offer Evaluation", "days": [
        {"d": "Mon", "tasks": [
            {"t": "LeetCode: 1 Medium warmup before any interview day", "c": "dsa"},
            {"t": "Execute any scheduled final round interviews", "c": "prep"},
        ]},
        {"d": "Tue", "tasks": [
            {"t": "Send thank-you notes within 24 hrs of every interview", "c": "prep"},
            {"t": "Note any feedback signals from the interview", "c": "jobsearch"},
        ]},
        {"d": "Wed", "tasks": [
            {"t": "Apply to 3–4 more roles — keep pipeline pressure on", "c": "jobsearch"},
            {"t": "Mock coding: 2 timed Mediums", "c": "dsa"},
        ]},
        {"d": "Thu", "tasks": [
            {"t": "Compare offers using total comp framework (base + equity + bonus)", "c": "prep"},
            {"t": "List non-salary factors: remote, team, product, growth", "c": "prep"},
        ]},
        {"d": "Fri", "tasks": [
            {"t": "Negotiate any received offers — use script from roadmap", "c": "prep"},
            {"t": "LeetCode: 1 problem to stay sharp", "c": "dsa"},
        ]},
        {"d": "Sat", "tasks": [
            {"t": "If no offers yet: double-down on applications + referrals", "c": "jobsearch"},
            {"t": "Reach out to 5 new referral contacts", "c": "jobsearch"},
        ]},
        {"d": "Sun", "tasks": [
            {"t": "Evaluate cultural fit: did interviews feel aligned with your values?", "c": "prep"},
            {"t": "Talk to a mentor or peer about offers — get outside perspective", "c": "prep"},
        ]},
    ]},
    {"w": 14, "title": "Offer Decision + Notice Period Prep", "days": [
        {"d": "Mon", "tasks": [
            {"t": "Make final offer decision — don't wait too long", "c": "prep"},
            {"t": "Inform all other companies in final stages", "c": "prep"},
        ]},
        {"d": "Tue", "tasks": [
            {"t": "Submit resignation professionally — give proper notice period", "c": "prep"},
            {"t": "Document your current work thoroughly for handover", "c": "prep"},
        ]},
        {"d": "Wed", "tasks": [
            {"t": "Set up onboarding research: read new company's engineering blog", "c": "prep"},
            {"t": "Identify 1–2 open source tools used by new company", "c": "tech"},
        ]},
        {"d": "Thu", "tasks": [
            {"t": "Continue LeetCode lightly — stay sharp for onboarding", "c": "dsa"},
            {"t": "Set 30-60-90 day goals for your new role", "c": "prep"},
        ]},
        {"d": "Fri", "tasks": [
            {"t": "Update LinkedIn profile: new role (set to start date)", "c": "jobsearch"},
            {"t": "Connect with future teammates on LinkedIn", "c": "jobsearch"},
        ]},
        {"d": "Sat", "tasks": [
            {"t": "Celebrate — you earned it 🎉", "c": "prep"},
            {"t": "Write a reflection: what worked, what you'd do differently", "c": "prep"},
        ]},
        {"d": "Sun", "tasks": [
            {"t": "Rest and recharge before your new role begins", "c": "prep"},
            {"t": "Set up your home office / dev environment for day 1", "c": "prep"},
        ]},
    ]},
]

# ─── Helpers ──────────────────────────────────────────────────────────────────
def task_key(wi, day, ti):
    return f"w{wi}_d{day}_t{ti}"

def week_progress(wi):
    w = PLAN[wi]
    total = sum(len(d["tasks"]) for d in w["days"])
    done = sum(
        1 for d in w["days"]
        for ti in range(len(d["tasks"]))
        if st.session_state.checked.get(task_key(wi, d["d"], ti), False)
    )
    return done, total

def total_progress():
    total = sum(len(d["tasks"]) for w in PLAN for d in w["days"])
    done = sum(1 for v in st.session_state.checked.values() if v)
    return done, total

def current_streak():
    all_days = []
    for wi, w in enumerate(PLAN):
        for d in w["days"]:
            has_any = any(
                st.session_state.checked.get(task_key(wi, d["d"], ti), False)
                for ti in range(len(d["tasks"]))
            )
            all_days.append(has_any)
    streak = 0
    for v in reversed(all_days):
        if v:
            streak += 1
        elif streak > 0:
            break
    return streak

def weeks_active():
    return sum(1 for wi in range(len(PLAN)) if week_progress(wi)[0] > 0)

def toggle_task(wi, day, ti):
    k = task_key(wi, day, ti)
    st.session_state.checked[k] = not st.session_state.checked.get(k, False)
    save_data(st.session_state.checked)

# ─── CSS ──────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}
.block-container {padding-top: 1.5rem; padding-bottom: 2rem; max-width: 860px;}

.stat-grid {display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 1.5rem;}
.stat-box {background: #f8f9fa; border-radius: 10px; padding: 14px 16px; text-align: center;}
.stat-label {font-size: 12px; color: #6b7280; margin-bottom: 4px;}
.stat-val {font-size: 26px; font-weight: 600;}
.streak-val {color: #d97706;}
.done-val {color: #059669;}

.heatmap-grid {display: flex; gap: 5px; flex-wrap: wrap; margin-bottom: 0.5rem;}
.hm-cell {width: 28px; height: 28px; border-radius: 5px; background: #e5e7eb;
          display: flex; align-items: center; justify-content: center;
          font-size: 10px; color: #9ca3af; cursor: default;}
.hm-partial {background: #6ee7b7; color: #065f46;}
.hm-full {background: #059669; color: white;}
.hm-current {outline: 2px solid #d97706; outline-offset: 1px;}

.legend-row {display: flex; gap: 14px; align-items: center; margin-top: 4px;}
.legend-dot {width: 12px; height: 12px; border-radius: 3px; display: inline-block;}
.legend-txt {font-size: 12px; color: #6b7280;}

.week-header-bar {background: #f3f4f6; border-radius: 8px; padding: 10px 14px;
                  margin-bottom: 2px; display: flex; align-items: center; gap: 10px;}
.week-num {font-size: 13px; font-weight: 600; color: #374151; min-width: 60px;}
.week-ttl {font-size: 13px; color: #374151; flex: 1;}
.week-badge-done {background: #d1fae5; color: #065f46; font-size: 11px;
                  padding: 2px 8px; border-radius: 20px; font-weight: 500;}

.cat-pill {font-size: 10px; padding: 2px 7px; border-radius: 20px;
           font-weight: 500; margin-left: 6px; white-space: nowrap;}
.day-sep {font-size: 11px; font-weight: 600; color: #9ca3af;
          margin: 6px 0 2px; text-transform: uppercase; letter-spacing: 0.05em;}
</style>
""", unsafe_allow_html=True)

# ─── Header ───────────────────────────────────────────────────────────────────
st.markdown("## 🚀 AI Engineer Switch Tracker")
st.caption("20-week plan · 3–5 months to your next offer · Mid-level → Big Tech / Startups / Mid-size")

# ─── Stats ────────────────────────────────────────────────────────────────────
done_total, all_total = total_progress()
pct = round(done_total / all_total * 100) if all_total else 0
streak = current_streak()
wactive = weeks_active()

st.markdown(f"""
<div class="stat-grid">
  <div class="stat-box"><div class="stat-label">Current streak</div>
    <div class="stat-val streak-val">{streak}{'&nbsp;day' if streak==1 else '&nbsp;days'}</div></div>
  <div class="stat-box"><div class="stat-label">Tasks done</div>
    <div class="stat-val done-val">{done_total}&nbsp;/&nbsp;{all_total}</div></div>
  <div class="stat-box"><div class="stat-label">Weeks active</div>
    <div class="stat-val">{wactive}&nbsp;/&nbsp;14</div></div>
  <div class="stat-box"><div class="stat-label">Overall progress</div>
    <div class="stat-val">{pct}%</div></div>
</div>
""", unsafe_allow_html=True)

# ─── Heatmap ──────────────────────────────────────────────────────────────────
st.markdown("**14-week progress map**")
cells_html = ""
current_week_idx = next(
    (wi for wi in range(len(PLAN)) if week_progress(wi)[0] < week_progress(wi)[1]),
    len(PLAN) - 1
)
for wi, w in enumerate(PLAN):
    d, t = week_progress(wi)
    cls = "hm-cell"
    if d == t and t > 0:
        cls += " hm-full"
    elif d > 0:
        cls += " hm-partial"
    if wi == current_week_idx:
        cls += " hm-current"
    cells_html += f'<div class="{cls}" title="Week {wi+1}: {d}/{t} done">W{wi+1}</div>'

st.markdown(f"""
<div class="heatmap-grid">{cells_html}</div>
<div class="legend-row">
  <span class="legend-dot" style="background:#e5e7eb;"></span><span class="legend-txt">Not started</span>
  <span class="legend-dot" style="background:#6ee7b7;"></span><span class="legend-txt">Partial</span>
  <span class="legend-dot" style="background:#059669;"></span><span class="legend-txt">Complete</span>
  <span class="legend-dot" style="outline:2px solid #d97706;background:transparent;"></span>
  <span class="legend-txt">Current week</span>
</div>
""", unsafe_allow_html=True)

st.divider()

# ─── Week filter ──────────────────────────────────────────────────────────────
PHASES = {
    "Phase 1–2 (Wk 1–5)": list(range(0, 5)),
    "Phase 3–4 (Wk 6–10)": list(range(5, 10)),
    "Final Push (Wk 11–14)": list(range(10, 14)),
    "All weeks": list(range(0, 14)),
}

col_filter, col_reset = st.columns([4, 1])
with col_filter:
    phase_choice = st.selectbox("Show weeks:", list(PHASES.keys()), label_visibility="collapsed")
with col_reset:
    if st.button("🔄 Reset all", use_container_width=True):
        st.session_state.checked = {}
        save_data({})
        st.rerun()

week_indices = PHASES[phase_choice]

# ─── Category pill helper ─────────────────────────────────────────────────────
def cat_pill(c):
    label = CAT_LABELS.get(c, c)
    bg = CAT_BG.get(c, "#f3f4f6")
    color = CAT_COLORS.get(c, "#374151")
    return f'<span class="cat-pill" style="background:{bg};color:{color};">{label}</span>'

# ─── Week blocks ──────────────────────────────────────────────────────────────
for wi in week_indices:
    w = PLAN[wi]
    done, total = week_progress(wi)
    pct_w = round(done / total * 100) if total else 0
    badge = '<span class="week-badge-done">✓ Done</span>' if done == total else f"<span style='font-size:12px;color:#6b7280;'>{done}/{total}</span>"

    with st.expander(f"Week {wi+1} · {w['title']}  —  {pct_w}%", expanded=(wi == current_week_idx)):
        st.progress(pct_w / 100)
        for day in w["days"]:
            st.markdown(f'<div class="day-sep">{day["d"]}</div>', unsafe_allow_html=True)
            for ti, task in enumerate(day["tasks"]):
                k = task_key(wi, day["d"], ti)
                is_done = st.session_state.checked.get(k, False)
                col_cb, col_text = st.columns([0.05, 0.95])
                with col_cb:
                    checked_val = st.checkbox(
                        label=" ",
                        value=is_done,
                        key=f"cb_{k}",
                        label_visibility="collapsed",
                    )
                    if checked_val != is_done:
                        toggle_task(wi, day["d"], ti)
                        st.rerun()
                with col_text:
                    text_style = "text-decoration:line-through;color:#9ca3af;" if is_done else "color:#1f2937;"
                    st.markdown(
                        f'<div style="{text_style}font-size:14px;padding-top:4px;">'
                        f'{task["t"]}{cat_pill(task["c"])}</div>',
                        unsafe_allow_html=True,
                    )

# ─── Footer ───────────────────────────────────────────────────────────────────
st.divider()
st.caption("Built for: Mid-level AI Engineer switching to Big Tech · Startups · Mid-size · March 2026")
