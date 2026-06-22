# Task: Bank Loan Approval System
age =int(input("Enter Your Age:"))
monthly_income=int(input("Enter Your Monthly Income:"))
credit_score=int(input("Enter Credit Score:"))
outstanding_debts=int(input("Enter Outstanding Debts:"))

MIN_INCOME = 50000
MIN_CREDIT_SCORE = 700
MAX_DEBT = 100000
if(
    18 <= age <= 60 and monthly_income>= MIN_INCOME and credit_score>= MIN_CREDIT_SCORE and outstanding_debts<= MAX_DEBT
):
    print("loan approved")
else:
    print("rejected")