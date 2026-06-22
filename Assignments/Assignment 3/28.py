# Given: text = "programming"
# Goal: Print all characters that repeat in the string

text="programming"
repeat= {}

for i in text:
    if text.count(i)>1:
        print(i)