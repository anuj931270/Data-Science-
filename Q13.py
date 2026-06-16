# Task: Salary Calculation
base_salary =int(input("Enter Your Base Salary:"))
bonus =int(input("Enter The Employee Bonus:"))
tax =(base_salary+bonus)/10
other_charges= int(input("Enter Other Charges:"))
gross_salary= base_salary+bonus
print(f"base salary={base_salary}, bonus={bonus}, tax={tax}, other charges= {other_charges}, gross salary= {gross_salary}")