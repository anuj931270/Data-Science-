# # switch value of two strings
# chr1 = "hello"
# chr2 = "java"
# chr1, chr2 = chr2,chr1
# print(f"chr1 ='{chr1}', chr2= '{chr2}'")

# current_balance = 10000
# deposit_balance = 5000
# print(f"Before deposit: current_balance={current_balance}")
# deposit_balance += current_balance
# print(f"After deposit: current_balance={deposit_balance}")


# balance=12000
# Withdrawal=3000
# print(f"Before: balance={balance}")
# Withdrawal -= balance
# print(f"after: Withdrawal={Withdrawal}")

# cart_items=5
# Increase=3
# print(f"Before: cart_items= {cart_items}")
# Increase += cart_items
# print(f"after: Increase cart_items= {Increase}")

# price = 1000
# discount_price=20
# discount_amnt=price*(discount_price/100)
# price_after=price-discount_amnt
# print(f"before price= {price}")
# # print(f"after price= {price_after}")

# n1=int(input("Enter the 1st number= "))
# n2=int(input("Enter the 2nd number= "))
# while n1<=n2:
#     if n1%2==0:
#         print(n1,"even")
#     else:
#         print(n1,"odd")
#     n1+=1

# str1="python programming"
# size=len(str1)
# i=0
# while i<=size:
#     print(str1[i])
#     i+=1

str1 = "python programming"
size = len(str1)
i = size - 1
while i >= 0:
        print(str1[i], end="")
        i -= 1






num = int(input("Enter a number: "))

# Prime numbers must be greater than 1
if num > 1:
    # Check for factors from 2 up to num - 1
    for i in range(2, num):
        if (num % i) == 0:
            print(f"{num} is not a prime number.")
            print(f"Because {i} times {num // i} is {num}")
            break
    else:
        # If the loop finishes without finding a factor
        print(f"{num} is a prime number.")
else:
    # If the number is less than or equal to 1
    print(f"{num} is not a prime number.")