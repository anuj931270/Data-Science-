# Employee Salary Based on Experience
years = int(input("Enter Years of experience: "))

if years > 15:
    base_salary =80000
    bonus=5000
    salary=base_salary+bonus
    print("10 or more years of experience is classified as a Senior Employee and the salary is =",(salary))
elif years >=10:
    print("Senior Employee")
    final_salary = 80000
    print(f"Salary: {final_salary}")

elif years >= 5:
    print("Mid-level employee")
    final_salary = 50000
    print(f"Salary: {final_salary}")

else:
    print("Junior employee")
    final_salary = 30000
    print(f"Salary: {final_salary}")