💰 Personal Finance Analyzer

A Python-based personal finance analysis project that stores expense data in CSV format and provides useful spending insights through a menu-driven application.

📌 Features

* Add new expenses
* Store expenses in CSV
* Load and validate expense data
* Calculate total expenses
* Calculate average expense
* Find highest and lowest expenses
* Analyze spending by category
* Analyze spending by payment method
* Analyze monthly expenses
* Find high-value expenses
* Calculate category-wise spending percentage
* Generate a financial report
* Logging using a custom decorator
* Modular Python project structure

🛠️ Technologies Used

* Python
* CSV File Handling
* Functions
* Lists
* Dictionaries
* Sets
* Exception Handling
* Modules
* Decorators
* `datetime`
* File Handling

📂 Project Structure

```text
personal-finance-analyzer/
│
├── data/
│   └── expenses.csv
│
├── src/
│   ├── main.py
│   ├── expense.py
│   ├── analyzer.py
│   ├── decorators.py
│   └── utils.py
│
├── reports/
│   └── financial_report.txt
│
├── README.md
├── requirements.txt
└── .gitignore
```

⚙️ How It Works

The application follows a simple flow:

```text
User Input
    ↓
CSV File
    ↓
Load & Validate Data
    ↓
Analyze Expenses
    ↓
Generate Results
    ↓
Display Financial Report
```

1. Add Expense

Users can enter:

* Date
* Category
* Amount
* Payment method

The expense is then stored in `expenses.csv`.

2. Load Expenses

The application reads the CSV file and converts each expense into a Python dictionary.

Example:

```python
{
    "Date": "2026-10-03",
    "Category": "Travel",
    "Amount": 300,
    "Payment": "Cash"
}
```

All expense dictionaries are stored inside a list.

3. Analyze Expenses

The analyzer calculates:

* Total spending
* Average spending
* Highest expense
* Lowest expense
* Category-wise spending
* Payment-method spending
* Monthly spending
* High expenses
* Spending percentage

🧾 Example Data

text
Date,Category,Amount,Payment
2026-09-01,Food,250,UPI
2026-09-02,Travel,350,Cash
2026-09-03,Shopping,800,UPI
2026-09-04,Food,300,UPI
2026-09-05,Entertainment,500,UPI
2026-10-03,Travel,300,Cash


📊 Example Report


========== FINANCIAL REPORT ==========

Total Expense : ₹2500
Average       : ₹416.67
Highest       : ₹800
Lowest        : ₹250

Payment Analysis:

UPI : ₹1850
Cash : ₹650

Monthly Analysis:

2026-09 : ₹2200
2026-10 : ₹300
```

▶️ How to Run

Make sure Python 3.10 or later is installed.

Open the project folder in terminal:

bash
cd personal-finance-analyzer


Run the application:

bash
python src/main.py


📋 Menu

```text
========== PERSONAL FINANCE ANALYZER ==========

1. Add Expense
2. Generate Report
3. Category Analysis
4. Payment Analysis
5. High Expenses
6. Spending Percentage
7. Exit
```

🎯 Learning Objectives

This project was built to practice Python concepts in a real-world application:

* File handling
* Data validation
* Lists and dictionaries
* Functions and return values
* Exception handling
* Modules
* Decorators
* Data analysis logic
* Modular project structure

🚀 Future Improvements

Possible future upgrades:

* GUI interface
* Database integration
* Data visualization
* Export reports to PDF
* Budget tracking
* Monthly budget alerts
* Expense editing and deletion
* Web-based dashboard

⚠️ Note

This project is created for learning and personal expense-analysis purposes. It does not provide financial advice.

👨‍💻 Author

Krish

Built with Python 🐍
