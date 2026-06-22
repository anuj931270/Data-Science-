# Given: text = "knowyourself"
# Goal: Find and print the alternate characters. 

text="knowyourself"
char1=text[::2]
char2=text[1::2]
print(f"Starting from 1st character: {char1}, Starting from 2nd character: {char2}")