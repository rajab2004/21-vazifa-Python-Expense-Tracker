import csv
import os

FILENAME = "expenses.csv"

def add_expense(date, category, amount):
    """Yangi xarajatni faylga qo'shadi"""
    with open(FILENAME, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

def read_all_expenses():
    """Barcha xarajatlarni o'qib ro'yxatda qaytaradi"""
    if not os.path.exists(FILENAME):
        return []
    
    with open(FILENAME, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        return list(reader)

def calculate_total(expenses):
    """Jami summa hisoblaydi"""
    total = 0
    for row in expenses:
        try:
            total += float(row[2])
        except (IndexError, ValueError):
            continue
    return total

def filter_by_date(expenses, search_date):
    """Sanaga qarab filtrlash"""
    return [row for row in expenses if row[0] == search_date]

def filter_by_category(expenses, search_category):
    """Turkumga qarab filtrlash"""
    return [row for row in expenses if row[1].lower() == search_category.lower()]

def format_expense(row):
    """Xarajatni chiroyli rinishda chiqarish"""
    try:
        date, category, amount = row
        return f"{date} | {category} | {amount} so'm"
    except:
        return "❌ Noto'g'ri formatlangan xarajat"
