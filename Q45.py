# Write a Python program to check if a number provided by the user is prime or not.
num=int(input("Enter a number"))
if num > 1:
    for i in range (2,num):
        if (num % i) ==0:
            print(f"{num} is not a prime number.")
        else:
            print(f"{num}is prime number.")
else:
    print("f{num} is not a prime number.")
