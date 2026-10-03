from datetime import datetime
from analyzer import generate_report
def display_report(report):

    print("========== FINANCIAL REPORT ==========")

    print(f"Total Expense : ₹{report['Total']}")
    print(f"Average       : ₹{report['Average']}")
    print(f"Highest       : ₹{report['Highest']}")
    print(f"Lowest        : ₹{report['Lowest']}")

    print("\nPayment Analysis:")

    for payment, amount in report["Payment"].items():
        print(f"{payment} : ₹{amount}")

    print("\nMonthly Analysis:")

    for month, amount in report["Monthly"].items():
        print(f"{month} : ₹{amount}")