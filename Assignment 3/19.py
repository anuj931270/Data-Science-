#  Write a Python program that allows the user to search for a character within a given string.

user=input("Enter the string ")
character=input("Enter a char ")
found=False
for char in user:
    if char == character:
        found=True
if found:
    print(f"Character '{character}' found!")
else:
    print(f"Character '{character}' not found.")