from pydantic import BaseModel, Field
from datetime import date

class Expense(BaseModel):
    dateExpense: date = Field(default_factory=date.today)
    description: str
    amount: int