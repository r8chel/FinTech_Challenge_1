# coding: utf-8
import csv
from pathlib import Path

# List of loan costs
loan_costs = [500, 600, 200, 1000, 450]

# Number of loans in the list
number_of_loans = len(loan_costs)
print(f"There are {number_of_loans} loans")

# Total of all loans
total_amount_of_loans = sum(loan_costs)
print(f"The total amount of all loans is ${total_amount_of_loans: .2f}")

# Average loan amount
average_loan_amount = total_amount_of_loans / number_of_loans 
print(f"The average loan price is ${average_loan_amount: .2f}")

# Previously defined loan data
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Calculating and printing future value
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")

print(f"The Future Value is ${future_value: .2f}")
print(f"There are {remaining_months} remaining months in the loan")

# Calculating the fair value
discount_rate = .2
present_value =  future_value / (1 + discount_rate/12) ** remaining_months
print(f"The Present Value is ${present_value: .2f}")

# Evaluating fair value to provide buyer recommendtion
if present_value >= loan.get("loan_price"):
    print("Buy the Loan")
else: 
    print("Don't Buy the Loan")

# New loan data
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Create a function to calculate present value
def calculate_present_value(future_value, remaining_months, discount_rate):
    return present_value

future_value = new_loan.get("future_value")
remaining_months = new_loan.get("remaining_months")

present_value = calculate_present_value(
        future_value, 
        remaining_months, 
        discount_rate)

print(f"The present value of the loan is: ${present_value: .2f}")

# List of loans
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# List to store loans that are $500 or less
inexpensive_loans = []

for loans_dict in loans:
    if loans_dict["loan_price"] <= 500:
        inexpensive_loans.append(loans_dict) 

print(inexpensive_loans)

# Save inexpensive loan data to a .csv file
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]
output_path = Path("inexpensive_loans.csv" )

print("Saving data to: ", output_path)
    
with open(output_path, "w", newline="") as filename:
    csvwriter = csv.writer(filename)
    csvwriter.writerow(header)
    for row in inexpensive_loans:
        csvwriter.writerow(row.values())