    # Write a Python program to count the odd and even numbers in the list [10, 23,
    # 11, 12, 33, 44, 2, 5, 6].

def count_even_odd(n):
    even_count=0
    odd_count=0
    
    for i in n:
        if i%2==0:
            even_count+=1
        else:
            # i%2!=0
              odd_count+=1
    print(f"Number of even elements: {even_count}, Number of odd elements: {odd_count}")
mylist=[10, 23,11, 12, 33, 44, 2, 5, 6]
count_even_odd(mylist)