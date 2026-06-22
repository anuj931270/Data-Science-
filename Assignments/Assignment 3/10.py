# Write a Python program to calculate the product of numbers between a starting and ending point provided by the user
start=int(input("Enter the starting number:"))
end=int(input("Enter the ending number:"))
product_of_numbers=1
for i in range(start,end+1):
    product_of_numbers *=i
    print(f"The product of number from {start} to {end} is {product_of_numbers}")