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
    pass

def calculate_total(expenses):
    pass

def filter_by_date(expenses, search_date):
    pass

def filter_by_category(expenses, search_category):
    pass

def format_expense(row):
    pass
