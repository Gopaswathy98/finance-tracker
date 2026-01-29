📊 Finance Tracker Pro

Finance Tracker Pro is a high-performance, full-stack financial management dashboard. It is designed to provide real-time expenditure tracking with a focus on backend efficiency, data persistence, and a secure user experience.

![Finance Tracker Main Dashboard] 
(finance-tracker-main.png)

### Project Demo
![Finance Tracker in Action]
(finance-tracker-demo.png)

🛠️ Tech Stack
Backend: Python (FastAPI) 
Database: PostgreSQL with SQLAlchemy ORM 
Frontend: React.js & Tailwind CSS 
Security: JWT (JSON Web Tokens) 
Containerization: Docker 

🏗️ Technical Highlights

Asynchronous Backend: Built using FastAPI to handle concurrent data requests with high speed and low latency.
Relational Data Mapping: Implemented PostgreSQL to manage complex financial records with high data integrity.
Secure Authentication: Engineered JWT-based authentication to provide stateless, secure user sessions.
Data Visualization: Developed a dynamic UI using React to visualize spending habits through interactive components.
Standardized Environments: Fully containerized with Docker to ensure the application runs consistently across development and production servers.

📂 Project Structure

Plaintext
├── backend/            # FastAPI Source Code & REST Endpoints
│   ├── app/
│   │   ├── auth/       # JWT Logic
│   │   ├── models/     # Database Schemas
│   │   └── main.py     # API Entry Point
├── frontend/           # React Source Code
│   └── src/            # Components & Visualization Logic
├── docker-compose.yml  # Container orchestration
└── README.md           # Documentation

⚙️ Installation & Setup

Clone the Repository:

Bash
git clone https://github.com/Gopaswathy98/finance-tracker.git
cd finance-tracker
Environment Setup:
Configure your .env file with PostgreSQL credentials and a SECRET_KEY for JWT.

Run with Docker:
Bash
docker-compose up --build
The app will be accessible at http://localhost:3000.
Bash
docker-compose up --build
The app will be accessible at http://localhost:3000.
