from fastapi import FastAPI

app = FastAPI(title="Finance Tracker API")

@app.get("/")
def read_root():
    return {"message": "Welcome to Finance Tracker API 🚀"}
