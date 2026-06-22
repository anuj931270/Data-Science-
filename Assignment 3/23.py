# Write a Python program to find duplicate letters between two strings.
# Example: In "virat" and "rohit", the duplicate letter is "r".

str1=input("Enter 1st stirng: ")
str2=input("Enter 2nd string: ")

for i in str1:
    if i in str2:
        print("Duplicate letters: ",i)