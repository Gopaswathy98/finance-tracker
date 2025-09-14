from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/expenses", tags=["Expenses"])

# Data model
class Expense(BaseModel):
    id: int
    description: str
    amount: float

# Fake in-memory DB
expenses_db: List[Expense] = []

@router.get("/", response_model=List[Expense])
def list_expenses():
    return expenses_db

@router.post("/", response_model=Expense)
def create_expense(expense: Expense):
    expenses_db.append(expense)
    return expense

@router.get("/{expense_id}", response_model=Expense)
def get_expense(expense_id: int):
    for expense in expenses_db:
        if expense.id == expense_id:
            return expense
    return {"error": "Expense not found"}

@router.delete("/{expense_id}")
def delete_expense(expense_id: int):
    global expenses_db
    expenses_db = [e for e in expenses_db if e.id != expense_id]
    return {"message": f"Expense {expense_id} deleted"}
