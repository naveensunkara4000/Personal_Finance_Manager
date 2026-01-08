import csv
from expense import Expense

def save_expense(expense, filename="data/expenses.csv"):
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([expense.date, expense.category, expense.amount, expense.description])


def load_expenses(filename="data/expenses.csv"):
    expenses = []
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)  # ✅ SKIP HEADER ROW

            for row in reader:
                if row:
                    expense = Expense(
                        amount=row[2],
                        category=row[1],
                        date=row[0],
                        description=row[3]
                    )
                    expenses.append(expense)

    except FileNotFoundError:
        print("⚠️ No expense file found yet.")

    return expenses
