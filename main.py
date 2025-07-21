from utils import (
    add_expense,
    read_all_expenses,
    calculate_total,
    filter_by_date,
    filter_by_category,
    format_expense
)

def handle_add_expense():
    date = input("sanani kiriting (YYYY-MM-DD): ")
    category = input("categoryani kiriting: ")
    amount = input("miqdorni kiriting: ")
    add_expense(date, category, amount)
    print("✅ Harajat qoshilldi!")

def handle_view_all():
    expenses = read_all_expenses()
    if len(expenses) == 0:
        print("Harajat topilmadi .")
    else:
        for row in expenses:
            print(format_expense(row))

def handle_total():
    expenses = read_all_expenses()
    total = calculate_total(expenses)
    print(f"Umumiy harajat : ${total}")

def handle_filter_by_date():
    search_date = input("Sana ni kiriting  (YYYY-MM-DD): ")
    expenses = read_all_expenses()
    filtered = filter_by_date(expenses, search_date)
    if len(filtered) == 0:
        print("bu sana uchun harajatlar yoq.")
    else:
        for row in filtered:
            print(format_expense(row))

def handle_filter_by_category():
    search_category = input("categoryani kiriting: ")
    expenses = read_all_expenses()
    filtered = filter_by_category(expenses, search_category)
    if len(filtered) == 0:
        print("harajatlar yoq bu categorya uchun.")
    else:
        for row in filtered:
            print(format_expense(row))

def main():
    while True:
        print("\n📋 Expense Tracker\n")
        print("1. Harajatlarni qoshish")
        print("2. hamma Harajatni korish")
        print("3. Umumiy barchasini summasini korish")
        print("4. sana boyicha filtr")
        print("5. Categorya boyicha fiter")
        print("6. Exit")

        choice = input(">: ")

        if choice == "1":
            handle_add_expense()
        elif choice == "2":
            handle_view_all()
        elif choice == "3":
            handle_total()
        elif choice == "4":
            handle_filter_by_date()
        elif choice == "5":
            handle_filter_by_category()
        elif choice == "6":
            print("👋 Hayr salomat boling : !")
            break
        else:
            print("❌ Notog'ri tanlov.")

if __name__ == "__main__":
    main()
