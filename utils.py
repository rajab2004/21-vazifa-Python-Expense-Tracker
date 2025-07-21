import os
import csv

FILENAME = "expenses.csv"

def add_expense(date, category, amount):
    if not os.path.exists(FILENAME):
        open(FILENAME, 'x').close()

    fieldnames = ['date', 'category', 'amount']
    with open(FILENAME) as csvfile:
        reader = csv.DictReader(csvfile, fieldnames)

        next(reader)

        rows = list(reader)
    
    rows.append({
        'date': date,
        'category': category,
        'amount': amount
    })

    with open(FILENAME, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def read_all_expenses():
    if not os.path.exists(FILENAME):
        open(FILENAME, 'x').close()

    rows = []
    fieldnames = ['date', 'category', 'amount']
    with open(FILENAME) as csvfile:
        reader = csv.DictReader(csvfile, fieldnames)

        next(reader)

        rows = list(reader)

    return rows

def calculate_total(expenses):
    total = sum(map(lambda expense: float(expense['amount']), expenses))
    return total

def filter_by_date(expenses, search_date):
    filtered_expenses = list(filter(
        lambda expense: expense['date'] == search_date,
        expenses
    ))
    return filtered_expenses

def filter_by_category(expenses, search_category):
    pass

def format_expense(row):
    pass
