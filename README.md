📊**** Finance Tracker Pro****

A full-stack, real-time expense management dashboard. This application allows users to track their spending with a polished user interface, featuring dynamic data calculation and persistent database storage.

## 🔗 Live Preview

**Check out the UI here:**  
https://gopaswathy98.github.io/finance-tracker/

*(Note: The live link demonstrates the UI/UX. Full CRUD functionality requires the backend server to be running locally.)*

## 🚀 Key Features

* **Real-time Data Processing**: Automatically calculates and updates the "Total Expenses" whenever an item is added or removed.
* **Smart Categorization**: Uses JavaScript logic to assign color-coded badges to different expense types (e.g., Food, Rent, Transport).
* **Full CRUD Lifecycle**: Users can **C**reate, **R**ead, and **D**elete entries via a RESTful API.
* **Professional UI**: A clean, responsive dashboard built with modern CSS (Shadows, Flexbox, and Transitions).

## 🛠️ Tech Stack

* **Backend**: FastAPI (Python)
* **Database**: SQLite with SQLAlchemy ORM
* **Frontend**: Vanilla JavaScript (Fetch API), HTML5, CSS3
* **Environment**: Python Virtual Environment (venv)

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
