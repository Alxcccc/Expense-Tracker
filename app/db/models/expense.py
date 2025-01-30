from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Expenses(Base):
    __tablename__ = "expenses"
    idExpense = Column(Integer, primary_key=True, autoincrement=True)
    dateExpense = Column(Date)
    description = Column(String(50))
    amount = Column(Integer)