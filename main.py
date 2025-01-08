import numpy as np
import pandas as pd
from datetime import datetime

# Data Structure to hold expenses in the form of DataFrame
expenses = pd.DataFrame(columns=["Date", "Amount", "Category"])

def add_expense():
    """
    Function to add an expense entry.
    """
    global expenses
    amount = float(input("Enter the expense amount: "))
    category = input("Enter the category (e.g., food, transportation, etc.): ")
    date = input("Enter the date of the expense (YYYY-MM-DD): ")

    # Append the new expense to the DataFrame
    expense = pd.DataFrame([[date, amount, category]], columns=["Date", "Amount", "Category"])
    expenses = pd.concat([expenses, expense], ignore_index=True)
    
    print("Expense added successfully!")

def generate_report():
    """
    Generate report of total expenses by category.
    """
    global expenses
    # Group by category and sum the expenses
    category_expenses = expenses.groupby("Category")["Amount"].sum().reset_index()
    print("\nTotal expenses by category:")
    print(category_expenses)

def view_expenses_by_date():
    """
    View expenses filtered by date range.
    """
    global expenses
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    try:
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
        
        # Filter expenses between the start and end date
        filtered_expenses = expenses[(pd.to_datetime(expenses['Date']) >= start_date) &
                                     (pd.to_datetime(expenses['Date']) <= end_date)]

        if not filtered_expenses.empty:
            print("\nExpenses between", start_date.date(), "and", end_date.date())
            print(filtered_expenses)
        else:
            print("No expenses found in the given date range.")
    except Exception as e:
        print(f"Error: {e}")

def main_menu():
    """
    Show the main menu to the user and execute the desired operation.
    """
    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add an Expense")
        print("2. View Total Expenses by Category")
        print("3. View Expenses by Date Range")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            generate_report()
        elif choice == '3':
            view_expenses_by_date()
        elif choice == '4':
            print("Exiting the application...")
            break
        else:
            print("Invalid choice. Please choose between 1-4.")

if __name__ == "__main__":
    main_menu()
