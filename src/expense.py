from datetime import datetime

def load_expenses():
  expenses = []
  with open("data/expenses.csv","r") as f:
    text = f.readlines()



  categories = ["Food","Travel","Shopping","Entertainment","Movies","Sports","Bills","Healthcare","Education","Groceries","Rent","Utilities"]
  payment_methods = ["UPI","Card","Cash"]

  for line in text[1:]:
  
    data = line.strip().split(",")
    try:
      amount = int(data[2])
      if data[1] not in categories:
        raise ValueError("Invalid category")    
      if data[3] not in payment_methods:
        raise ValueError("Invalid payment") 
      date = datetime.strptime(data[0], "%Y-%m-%d")
      dictionary1 = {
      "Date" : data[0],
      "Category" : data[1],
      "Amount" : amount,
      "Payment" : data[3]
      }
      expenses.append(dictionary1)
    
    except ValueError as e:
      print(e)
  return expenses

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = input("Enter amount: ")
    payment = input("Enter payment method: ")

    categories = [
        "Food", "Travel", "Shopping", "Entertainment",
        "Movies", "Sports", "Bills", "Healthcare",
        "Education", "Groceries", "Rent", "Utilities"
    ]

    payment_methods = ["UPI", "Card", "Cash"]

    try:
        datetime.strptime(date, "%Y-%m-%d")
        amount = int(amount)

        if category not in categories:
            raise ValueError("Invalid category")

        if payment not in payment_methods:
            raise ValueError("Invalid payment method")

        with open("data/expenses.csv", "a") as f:
            f.write(f"{date},{category},{amount},{payment}\n")

        print("Expense added successfully!")

    except ValueError as e:
        print(e)
    
