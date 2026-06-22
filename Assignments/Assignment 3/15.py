# Write a Python program to print alternate characters from a given string.
text = input("Enter a string: ")
for i in range(0, len(text), 2):
    print(text[i], end="")
print()