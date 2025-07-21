from utils import (
    add_expense,
    read_all_expenses,
    calculate_total,
    filter_by_date,
    filter_by_category,
    format_expense
)

def handle_add_expense():
    date = input("Date: ")
    category = input("Category: ")
    amount = float(input("Amount: "))

    add_expense(date, category, amount)
    print("A new expenese is added succesfully")

def handle_view_all():
    all_expenses = read_all_expenses()

    if all_expenses:
        print("\n-----All Expenses-----")
        for counter, exepense in enumerate(all_expenses, start=1):
            print(f"{counter}. {exepense['date']}, {exepense['category']}, {exepense['amount']}")
    else:
        print("\n-----NO EXPENSES-----")

def handle_total():
    expenses = read_all_expenses()
    total = calculate_total(expenses)

    print("----Your All Total Expenses----")
    print(f"{total:,.2f}")

def handle_filter_by_date():
    pass

def handle_filter_by_category():
    pass

def main():
    while True:
        print("\n📋 Expense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expenses")
        print("4. Filter by Date")
        print("5. Filter by Category")
        print("6. Exit")

        choice = input("Choose an option: ")

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
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
