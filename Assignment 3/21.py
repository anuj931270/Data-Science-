# Write a Python program to filter out duplicate characters from a string entered by the user.

str1 = input("Enter a string: ")

seen = set()
result = ""

for i in str1:
    if i not in seen:
        seen.add(i)
        result += i

print("String after removing duplicate characters:", result)