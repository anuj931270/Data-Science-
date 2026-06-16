# Write a Python program to print all odd and even numbers from 1 to 20.
num1=int(input("Enter the 1st number= "))
num2=int(input("Enter the 2nd number= "))
while num1 <= num2:
        if num1 % 2 == 0:
            print(num1,"even")
        else:
            print(num1,"odd")
        num1 += 1