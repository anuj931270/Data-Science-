# Arranging Three Numbers in Descending Order
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
if num1>=num2 and num1>=num3:
    if num2>num3:
        order1=num1,num2,num3
        print(order1)
    else:
        order2=num1,num3,num2
        print(order2)
elif num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        order3=num2,num1,num3
        print(order3)
    else:
        order4=num2,num3,num1
        print(order4)
else:
    if num2>=num1:
        order5=num3,num2,num1
        print(order5)
    else:
        order6=num3,num1,num2
        print(order6)


