#  Write a Python program to count the total number of characters in a string entered by the user.
user=input("Enter a string: ")
total_char=0
for char in user:
    total_char +=1
print(f"The total char is:",total_char)