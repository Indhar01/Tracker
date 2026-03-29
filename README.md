# 🚀 AI Engineer Switch Tracker

A 14-week interactive progress tracker for mid-level AI engineers switching to Big Tech, startups, or mid-size companies.

## Features
- Daily task checklist across 14 weeks
- Streak tracking & overall progress stats
- 14-week heatmap view
- Phase-based week filtering
- Progress auto-saved locally to `tracker_data.json`

## Deploy to Streamlit Community Cloud (free, ~3 minutes)

### Step 1 — Push to GitHub
```bash
# Create a new repo on github.com, then:
git init
git add .
git commit -m "Initial commit: AI Engineer Switch Tracker"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ai-engineer-tracker.git
git push -u origin main
```

### Step 2 — Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click **"New app"**
4. Select your repo → branch: `main` → main file: `app.py`
5. Click **"Deploy"** — live in ~60 seconds ✅

Your app will be available at:
`https://YOUR_USERNAME-ai-engineer-tracker-app-XXXX.streamlit.app`

## Run Locally
```bash
pip install streamlit
streamlit run app.py
```

## Files
```
├── app.py              # Main Streamlit app
├── requirements.txt    # Dependencies
├── tracker_data.json   # Auto-created on first run (stores your progress)
└── README.md
```

> Note: On Streamlit Community Cloud, `tracker_data.json` resets on redeploy.
> For persistent cloud storage, consider adding a free Supabase or Firebase backend.
