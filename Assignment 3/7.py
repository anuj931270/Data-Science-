# Find the greatest character from the string "python"
mystr = "python"
greatest_char = max(mystr)
print("The greatest character is:", greatest_char)
greatest_char = mystr[0]
for char in mystr:
     if char > greatest_char:
         greatest_char = char
print("The greatest character is:", greatest_char)