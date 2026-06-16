# Task: Retirement Age Calculator
age=int(input("Enter your age= "))
old = 65-age
if age>=65:
    print("retire")
else:
    print(old,"years left until retirement.")
    print("not retire")