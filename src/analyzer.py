from datetime import datetime
from decorators import log_analysis
def calculate_total(expenses):
  total = 0
  for value in expenses:
    total = total+value["Amount"]
  return total

def calculate_average(expenses):
  total = calculate_total(expenses)
  average = (total)/ len(expenses)
  return average

def find_highest_lowest(expenses):
  val_list = []
  for value in expenses:
    values = value["Amount"]
    val_list.append(values)
  highest = max(val_list)
  lowest = min(val_list) 
  return highest , lowest



def category_analysis(expenses):
  total_amount = 0
  enter_category = input("Enter category : ").lower()
  for value in expenses:
    category = value["Category"]
    if category.lower() == enter_category:
      total_amount = total_amount + value["Amount"]
  return total_amount



def payment_analysis(expenses):
  payment_total = {}

  for value in expenses:
    payment = value["Payment"]
    amount = value["Amount"]
    if payment in payment_total:
      total_payment = payment_total[payment] + amount
      payment_total[payment] = total_payment
    else:
      payment_total[payment] = amount
  return payment_total


def monthly_analysis(expenses):


  monthly_total = {}

  for value in expenses:
    date = datetime.strptime(value["Date"], "%Y-%m-%d")
    amount = value["Amount"]
    year = date.year
    month = date.month
    month_key = f"{year}-{month:02d}"
    if month_key in monthly_total:
      monthly_payment = monthly_total[month_key] + amount
      monthly_total[month_key] = monthly_payment
    else:
      monthly_total[month_key] = amount
  return monthly_total


def high_expense(expenses):
  high_expenses = []
  limit = int(input("Enter you limit : "))
  for value in expenses:
    amount = value["Amount"]
    if amount>limit:
      high_expenses.append(value)
  return high_expenses


def spending_percentage(category_total,expenses):
  percentage = {}
  for category , amount in category_total.items():
    total = calculate_total(expenses)
    category_percentage = (amount / total) * 100
    percentage[category] = category_percentage
  return percentage

@log_analysis
def generate_report(expenses):

    total = calculate_total(expenses)
    average = calculate_average(expenses)
    highest, lowest = find_highest_lowest(expenses)
    payment = payment_analysis(expenses)
    monthly = monthly_analysis(expenses)

    report = {
        "Total": total,
        "Average": average,
        "Highest": highest,
        "Lowest": lowest,
        "Payment": payment,
        "Monthly": monthly
    }

    return report
  
