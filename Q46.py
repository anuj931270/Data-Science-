#   Calculate the sum of numbers between a starting and ending point
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

# Using a loop to calculate the sum (inclusive)
total_sum = 0
for i in range(start, end + 1):
    total_sum += i

print(f"The sum of numbers from {start} to {end} is: {total_sum}")