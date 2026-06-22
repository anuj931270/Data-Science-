#  Write a Python program to display the odd and even elements from the list [10, 23, 11, 12, 33, 44, 2, 5, 6]. 

list [10, 23, 11, 12, 33, 44, 2, 5, 6]
odd_count=0
for i in list:
    if i%2==0:
        odd_count+=1
print("Odd:", odd_count)