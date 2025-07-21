import os
import csv

FILENAME = "expenses.csv"

def add_expense(date, category, amount):
    with open(FILENAME, mode="a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

def read_all_expenses():
    expenses = []
    if os.path.exists(FILENAME):
        with open(FILENAME, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                    expenses.append(row)
    return expenses

def calculate_total(expenses):
    total = 0
    for row in expenses:
        total += float(row[2])
    return total

def filter_by_date(expenses, search_date):
    result = []
    for row in expenses:
        if row[0] == search_date:
            result.append(row)
    return result

def filter_by_category(expenses, search_category):
    result = []
    for row in expenses:
        if row[1].lower() == search_category.lower():
            result.append(row)
    return result

def format_expense(row):
    return f"📅 Sana: {row[0]}, 🏷️ Categorya: {row[1]}, 💵 Miqdor: ${row[2]}"
