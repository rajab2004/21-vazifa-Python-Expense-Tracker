from utils import (
    add_expense,
    read_all_expenses,
    calculate_total,
    filter_by_date,
    filter_by_category,
    format_expense
)

def handle_add_expense():
    pass

def handle_view_all():
    pass

def handle_total():
    pass

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
