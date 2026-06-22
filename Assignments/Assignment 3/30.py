# Given: text = "knowyourself"
# Goal: Find and print the first character that repeats.

text = "knowyourself"
seen = set()

for i in text:
    if i in seen:
        print(i)
    seen.add(i)

