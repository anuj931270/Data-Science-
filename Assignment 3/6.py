# Calculate the product of numbers between a starting and ending point
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
total_product = 1
for i in range(start, end + 1):
    total_product *= i

print(f"The product of numbers from {start} to {end} is: {total_product}")