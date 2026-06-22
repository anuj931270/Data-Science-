# Write a Python program to display the odd and even elements from the list [10,
# 23, 11, 12, 33, 44, 2, 5, 6].

def odd_even(n):
    for i in n:
        if i%2==0:
            print("Even",i)
        else:
            i%2!=0
            print("odd",i)
mylist=[10, 23, 11, 12, 33, 44, 2, 5, 6]
odd_even(mylist)