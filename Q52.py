# Write a Python program to generate the Fibonacci sequence up to a specified number of terms.

n = 7
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b