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
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(models.Expense).filter(models.Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    db.delete(expense)
    db.commit()
    return {"message": "Expense deleted"}
