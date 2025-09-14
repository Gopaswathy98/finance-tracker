from fastapi import FastAPI
from app.routes import expenses

app = FastAPI(title="Finance Tracker API")

app.include_router(expenses.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Finance Tracker API 🚀"}
