#  Given a string text = "python", calculate the sum of the indices of its characters without using the range() or len() functions.

text=input("Enter a text: ")
total=0
index=0

for i in text:
    total +=index
    index +=1
print(total)