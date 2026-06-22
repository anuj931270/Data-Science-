#  Given: text = "python programming"
# Goal: Count how many vowels are in the string.
# Constraint: Do not use indexing (text[i]) or slicing (text[:]).

text="Python Programming"
count=0
vowels="aeiouAeiou"

for i in text:
    if i in vowels:
        count +=1
print(count)
