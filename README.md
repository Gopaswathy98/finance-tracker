📊 Finance Tracker Pro

A full-stack, real-time expense management dashboard. This application allows users to track their spending with a polished user interface, featuring dynamic data calculation and persistent database storage.

## 🔗 Live Preview

**Check out the UI here:**  
https://gopaswathy98.github.io/finance-tracker/

*(Note: The live link demonstrates the UI/UX. Full CRUD functionality requires the backend server to be running locally.)*

🚀 Technical Highlights
Reactive State Management: Implemented custom JavaScript logic to handle real-time expenditure calculations and DOM updates without the overhead of heavy frameworks.

RESTful API Design: Developed a structured backend using FastAPI to handle concurrent requests and maintain a clean separation of concerns.

Asynchronous Communication: Utilized modern Fetch API patterns with async/await to ensure a non-blocking, smooth User Experience.

Relational Mapping: Employed SQLAlchemy ORM to manage database interactions, ensuring data integrity and scalable schema design.

🛠️ Core Technology
Backend: FastAPI (Python 3.x)

ORM: SQLAlchemy (Object Relational Mapper)

Database: SQLite3 (Persistent Storage)

Frontend: Vanilla ECMAScript 6+, HTML5, CSS3 (Modern Flexbox/Grid)

## 📂 Project Structure

```text
finance-tracker/
├── backend/            # FastAPI Source Code
│   └── app/
│       ├── routes/     # API Endpoints (GET, POST, DELETE)
│       ├── models.py   # Database Schema
│       └── main.py     # Server Entry Point
├── docs/               # Frontend (Hosted on GitHub Pages)
│   └── index.html      # Pro Dashboard & JS Logic
├── finance.db          # SQLite Database (Local only)
└── README.md           # Documentation

```

## ⚙️ Installation & Setup

1. **Clone & Navigate**:
```bash
git clone https://github.com/Gopaswathy98/finance-tracker.git
cd finance-tracker

```


2. **Start the Backend**:
```bash
.\venv\Scripts\activate
cd backend
python.exe -m uvicorn app.main:app --reload

```


3. **View the App**:
Open `docs/index.html` in any web browser to start tracking expenses!

---
