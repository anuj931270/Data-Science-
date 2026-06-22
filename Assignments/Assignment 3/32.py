#  Take two numbers from the user: start and end. Print a string labeling each
# number in that range as Odd or Even.
# Output_format : 3:Odd 4:Even 5:Odd 6:Even 7:Odd 8:Even 9:Odd

num1=int(input("Enter start number: "))
num2=int(input("Enter end number: "))
for i in range(num1,num2+1):
    if i %2==0:
        print(f"{i}: Even",end="")
    else:
        print(f"{i}: Odd",end="")