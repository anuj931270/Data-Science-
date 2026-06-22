# Write a Python program to interchange the first and last elements in the list [10,
# 23, 11, 12, 33, 44, 2, 5, 6]

mylist = [10, 23, 11, 12, 33, 44, 2, 5, 6]
print("Before interchange the elements is: ",mylist)
mylist[0],mylist[1]=mylist[-1],mylist[0]
print("After interchange the elements is: ",mylist) 