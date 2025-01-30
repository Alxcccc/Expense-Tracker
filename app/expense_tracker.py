import typer
from rich.console import Console
from rich.table import Table

# Database Services
from db.services import expense_tracker_service
db = expense_tracker_service.DataBase()

# Models
from models.expense import Expense

app = typer.Typer()
console = Console()


@app.command()
def add(description: str = "", amount: int = 0):
    if description and amount:
        new_expense = Expense(description=description, amount=amount)
        result = db.add_expense(new_expense)
        if result is True:
            typer.secho("Your new expense was added successfully", fg=typer.colors.BRIGHT_GREEN)
            return None
        typer.secho(f"It have error: {result}", fg=typer.colors.BRIGHT_RED)
        
@app.command()
def list():
    result = db.get_expenses()
    table = Table("ID", "Date", "Description", "Amount")
    for expense in result:
        table.add_row(str(expense.idExpense), str(expense.dateExpense), expense.description, str(expense.amount))
    console.print(table)
    
@app.command()
def summary(month: int = 0):
    if not month:
        result = db.summary_amount()
        table = Table("Total Amount")
        table.add_row(str(result))
        console.print(table)
    else:
        result = db.summary_amount_month(month)
        table = Table("Month","Total Amount")
        table.add_row(str(month), str(result))
        console.print(table)
    
@app.command()
def delete(id: int = 0):
    if id:
        result = db.delete_expense(id)
        if result is True:
            typer.secho("Expense deleted successfully", fg=typer.colors.BRIGHT_GREEN)
            return None
        typer.secho(f"Delete: {result}", fg=typer.colors.BRIGHT_RED)
        


if __name__ == "__main__":
    app()