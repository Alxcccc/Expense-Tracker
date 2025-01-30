from sqlalchemy import func, extract
from sqlalchemy.exc import SQLAlchemyError

# Database
from db import database as db

# Models Database
from db.models.expense import Expenses as expenses_db

# Models app
from models.expense import Expense


class DataBase:
    def add_expense(self, expense: Expense) -> bool:
        try:
            new_expense = expenses_db(
                dateExpense=expense.dateExpense,
                description=expense.description,
                amount=expense.amount,
            )
            with db.get_session() as session:
                session.add(new_expense)
                session.commit()
                return True

        except SQLAlchemyError as e:
            session.rollback()
            return str(e)

    def get_expenses(self) -> list[Expense]:
        try:
            with db.get_session() as session:
                result = session.query(expenses_db).all()
                return result

        except SQLAlchemyError as e:
            session.rollback()
            return str(e)

    def summary_amount(self) -> int:
        try:
            with db.get_session() as session:
                result = session.query(func.sum(expenses_db.amount)).scalar()
                return result

        except SQLAlchemyError as e:
            session.rollback()
            return str(e)

    def summary_amount_month(self, month: int):
        try:
            with db.get_session() as session:
                result = (
                    session.query(func.sum(expenses_db.amount))
                    .filter(extract("month", expenses_db.dateExpense) == month)
                    .scalar()
                )
                return result
        except SQLAlchemyError as e:
            session.rollback()
            return str(e)

    def delete_expense(self, id: int):
        try:
            with db.get_session() as session:
                result = (
                    session.query(expenses_db)
                    .filter(expenses_db.idExpense == id)
                    .delete()
                )
                if result == 0:
                    raise SQLAlchemyError(f"The expense not found {id}")
                session.commit()
                return True
        except SQLAlchemyError as e:
            session.rollback()
            return str(e)
