# Find the sum of string “198765456412”.
str1="198765456412"

digit_sum = sum(int(c) for c in str1)
ascii_sum = sum(ord(c) for c in str1) #The ord() function stands for ordinalfunction stands for ordinal. Instead of converting text to its literal math value, it looks up the character's underlying ASCII/Unicode code point value.
print(f"Digit sum: {digit_sum}")
print(f"ASCII sum: {ascii_sum}")