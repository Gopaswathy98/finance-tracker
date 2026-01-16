from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import ExpenseModel
from pydantic import BaseModel

router = APIRouter()

# Schema for incoming data (POST)
class ExpenseSchema(BaseModel):
    item: str
    amount: float
    category: str

    class Config:
        from_attributes = True

# 1. GET ALL EXPENSES
@router.get("/")
def get_expenses(db: Session = Depends(get_db)):
    # This pulls data from your finance.db file
    return db.query(ExpenseModel).all()

# 2. ADD AN EXPENSE
@router.post("/")
def add_expense(expense: ExpenseSchema, db: Session = Depends(get_db)):
    # This saves data permanently to your finance.db file
    new_expense = ExpenseModel(
        item=expense.item, 
        amount=expense.amount, 
        category=expense.category
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

# 3. DELETE AN EXPENSE (The New "Action" Step)
@router.delete("/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    # Look for the specific expense using its unique ID
    expense = db.query(ExpenseModel).filter(ExpenseModel.id == expense_id).first()
    
    # If the ID doesn't exist, return an error
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    # Remove it from the database
    db.delete(expense)
    db.commit()
    
    return {"message": f"Expense {expense_id} deleted successfully"}
