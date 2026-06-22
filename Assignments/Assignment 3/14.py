# Write a Python program to display all letters except 'm' and 'i' from the string "Dreamer infotech".
text = "Dreamer infotech"
for char in text:
    if char == 'm' or char == 'i':
        continue  # Skip these characters
    print(char, end="")
print()
