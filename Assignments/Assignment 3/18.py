#   Write a Python program to check whether a string entered by the user is a palindrome
text=input("Enter a string: ")
reversed_text=""
for char in text:
    reversed_text=char+reversed_text
    if text == reversed_text:
        print("It is a Palindrome.")
    else:
        print("It is not a Palindrome.")