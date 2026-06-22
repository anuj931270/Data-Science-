# Write a Python program to filter out all vowels and consonants from a string
# entered by the user.

str1=input("Enter a string")
vowels=""
consonants=""
for i in str1:
    if  i.isalpha():
        if i.lower() in "aeiou":
            vowels +=i
        else:
            consonants +=i   #keep only non-alphabetic character
print("Vowels",vowels)
print("Consonants",consonants)