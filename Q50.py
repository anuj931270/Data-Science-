# Write a Python program to calculate the sum of numbers between a starting and ending point provided by the user.

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
total_add=0
for i in range (start, end+1):
    total_add +=i
print(f"The sum of numbers from {start} to {end} is: {total_add}")

# start = int(input("Enter starting number: "))
# end = int(input("Enter ending number: "))
# total_sum = sum(range(start, end + 1))
# print(f"The sum is: {total_sum}")