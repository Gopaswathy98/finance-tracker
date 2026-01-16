📊 Finance Tracker
A full-stack web application designed to help users track and manage their daily expenses. This project demonstrates a complete CRUD (Create, Read, Update, Delete) lifecycle using a modern Python backend and a responsive JavaScript frontend.

🚀 Features
Data Persistence: Expenses are stored securely in a local SQLite database using SQLAlchemy ORM.

RESTful API: A high-performance backend built with FastAPI featuring automated Swagger documentation.

Dynamic UI: A clean, user-friendly interface that updates in real-time using the JavaScript Fetch API without needing page reloads.

Expense Management: Users can add items with categories and delete them instantly.

🛠️ Tech Stack
Backend: FastAPI (Python 3.x)

Database: SQLite

ORM: SQLAlchemy

Frontend: HTML5, CSS3, Vanilla JavaScript

Server: Uvicorn

📂 Project Structure
Plaintext

finance-tracker/
├── backend/            # Python FastAPI source code
│   └── app/
│       ├── routes/     # API endpoints (GET, POST, DELETE)
│       ├── models.py   # Database schema definitions
│       └── main.py     # Application entry point
├── frontend/           # Web interface
│   └── index.html      # Main dashboard and logic
├── venv/               # Virtual environment (ignored by git)
└── README.md           # Project documentation
⚙️ Setup & Installation
Clone the repository:

Bash

git clone https://github.com/Gopaswathy98/finance-tracker.git
cd finance-tracker
Set up the Virtual Environment:

Bash

python -m venv venv
.\venv\Scripts\activate
Install Dependencies:

Bash

pip install fastapi uvicorn sqlalchemy
Run the Backend Server:

Bash

cd backend
python -m uvicorn app.main:app --reload
Open the Frontend: Simply open frontend/index.html in your preferred web browser.
