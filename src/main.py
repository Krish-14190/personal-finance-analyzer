from analyzer import (
    generate_report,
    category_analysis,
    high_expense,
    spending_percentage,
    payment_analysis
)

from expense import load_expenses, add_expense
from utils import display_report


expenses = load_expenses()


while True:

    print("\n========== PERSONAL FINANCE ANALYZER ==========")
    print("1. Add Expense")
    print("2. Generate Report")
    print("3. Category Analysis")
    print("4. Payment Analysis")
    print("5. High Expenses")
    print("6. Spending Percentage")
    print("7. Exit")

    choice = input("Enter your choice : ")

    if choice == "1":

        add_expense()
        expenses = load_expenses()

    elif choice == "2":

        report = generate_report(expenses)
        display_report(report)

    elif choice == "3":

        amount = category_analysis(expenses)
        print(f"Category Total : ₹{amount}")

    elif choice == "4":

        payment = payment_analysis(expenses)

        for method, amount in payment.items():
            print(f"{method} : ₹{amount}")

    elif choice == "5":

        high_expenses = high_expense(expenses)

        for value in high_expenses:
            print(f"Category : {value['Category']}")
            print(f"Amount : ₹{value['Amount']}")
            print(f"Payment : {value['Payment']}")
            print()

    elif choice == "6":

        category_total = {}

        for value in expenses:
            category = value["Category"]
            amount = value["Amount"]

            if category in category_total:
                category_total[category] += amount
            else:
                category_total[category] = amount

        percentage = spending_percentage(category_total, expenses)

        for category, value in percentage.items():
            print(f"{category} : {value:.2f}%")

    elif choice == "7":

        print("Thank you for using Personal Finance Analyzer!")
        break

    else:

        print("Invalid choice. Please try again.")