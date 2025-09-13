git clone https://github.com/Gopaswathy98/finance-tracker.git
cd finance-tracker

# create README.md from terminal
cat > README.md <<'EOF'
# Finance Tracker

A small full-stack app to track income and expenses (FastAPI + React).

## Demo
(put live demo link here after deployment)

## Features (MVP)
- User signup / login (JWT)
- Add transactions (income / expense, amount, category, date, notes)
- View & filter transactions
- Dashboard with charts (expense breakdown, monthly totals)

## Tech stack
- Backend: FastAPI, SQLAlchemy, Pydantic, PostgreSQL
- Frontend: React, TailwindCSS, Recharts (charts)
- Auth: JWT
- Dev & deploy: Docker, docker-compose, Vercel (frontend), Render (backend)
finance-tracker/
├─ backend/ # FastAPI app, models, routes
├─ frontend/ # React app (Tailwind, Recharts)
├─ docker-compose.yml
└─ README.md

## Getting started (local)
### Backend
```bash
cd backend
python -m venv venv
# On Windows:
# venv\Scripts\activate
# On macOS / Linux:
# source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
cd frontend
npm install
npm run dev


## Project structure
