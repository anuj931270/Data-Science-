# Write a Python program to calculate the factorial of a number provided by the user
num=int(input("Enter the number: "))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)