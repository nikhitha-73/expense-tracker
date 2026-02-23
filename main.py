import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

def init_file():
    try:
        with open(FILE_NAME, "x", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Category", "Amount", "Note"])
    except FileExistsError:
        pass

def add_expense():
    category = input("Category: ")
    amount = float(input("Amount: "))
    note = input("Note: ")
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, note])

    print("Expense added!")

def view_expenses():
    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def total_spent():
    total = 0
    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            total += float(row[2])
    print("Total spent:", total)

def menu():
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spent")
    print("4. Exit")

init_file()

while True:
    menu()
    choice = input("Choose: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_spent()
    elif choice == "4":
        break
