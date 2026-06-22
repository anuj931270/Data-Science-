#  Write a Python program to display all possible pairs of 3.
# Example: 1:3, 2:3, 3:3 , 2:1 , 2:2 ,2:3 , 3:1 ,3:2 ,3:3


# Program to display all possible pairs of 3

n = 3

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i}:{j}")