import csv
import os
from utils import (
    add_expense,
    read_all_expenses,
    calculate_total,
    filter_by_date,
    filter_by_category,
    format_expense
)

def handle_add_expense():
    sana = input(" Sanani kiriting (Yil-oy-kun): ")
    summa = float(input(" Summani kiriting: "))
    turkum = input(" Turkumni kiriting: ")
    izoh = input(" Izoh: ")
    add_expense(sana, turkum, summa, izoh)
    print(" Xarajat muvaffaqiyatli qo'shildi.")

def handle_view_all():
    xarajatlar = read_all_expenses()
    if not xarajatlar:
        print(" Hech qanday xarajat topilmadi.")
    for xarajat in xarajatlar:
        print(format_expense(xarajat))

def handle_total():
    xarajatlar = read_all_expenses()
    jami = calculate_total(xarajatlar)
    print(f" Jami xarajatlar: {jami} so'm")

def handle_filter_by_date():
    sana = input(" Qanday sana bo'yicha? (Yil-oy-kun): ")
    xarajatlar = read_all_expenses()
    filtrlangan = filter_by_date(xarajatlar, sana)
    if not filtrlangan:
        print(" Ushbu sana bo'yicha xarajat topilmadi.")
    for xarajat in filtrlangan:
        print(format_expense(xarajat))

def handle_filter_by_category():
    turkum = input(" Qanday turkum bo'yicha? ")
    xarajatlar = read_all_expenses()
    filtrlangan = filter_by_category(xarajatlar, turkum)
    if not filtrlangan:
        print(" Ushbu turkum bo'yicha xarajat topilmadi.")
    for xarajat in filtrlangan:
        print(format_expense(xarajat))

def main():
    while True:
        print("\n Xarajatlar Nazorati")
        print("1. Xarajat qo'shish")
        print("2. Barcha xarajatlarni ko'rish")
        print("3. Jami xarajatlarni ko'rish")
        print("4. Sanaga qarab filtrlash")
        print("5. Turkumga qarab filtrlash")
        print("6. Chiqish")

        tanlov = input(" Bo'limni tanlang: ")

        if tanlov == "1":
            handle_add_expense()
        elif tanlov == "2":
            handle_view_all()
        elif tanlov == "3":
            handle_total()
        elif tanlov == "4":
            handle_filter_by_date()
        elif tanlov == "5":
            handle_filter_by_category()
        elif tanlov == "6":
            print(" Xayr! Dasturdan foydalanganingiz uchun rahmat.")
            break
        else:
            print(" Noto'g'ri tanlov. Qaytadan urinib ko'ring.")

# 👇 BU YERDA asosiy ishga tushirish joyi
if __name__ == "__main__":
    main()
