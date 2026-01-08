from expense import Expense
from file_manager import save_expense, load_expenses
from menu import show_menu

def main():
    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            amount = float(input("Amount: "))
            category = input("Category: ")
            date = input("Date (YYYY-MM-DD): ")
            desc = input("Description: ")

            expense = Expense(amount, category, date, desc)
            save_expense(expense)
            print("✅ Expense added successfully!")

        elif choice == "2":
            expenses = load_expenses()
            for e in expenses:
                print(e)

        elif choice == "3":
            print("Goodbye!")
            break

main()
