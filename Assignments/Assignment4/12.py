# Find the second greatest element in the list [89, 23, 24, 2, 55, 54, 64].

# Find the second greatest element in the list [89, 23, 24, 2, 55, 54, 64].

def second_greatest(l):
    greatest = float("-inf")
    second = float("-inf")
    for i in l:
        if i > greatest:
            second = greatest
            greatest = i
        elif i > second and i != greatest:
            second = i
    return second
mylist = [89, 23, 24, 2, 55, 54, 64]
second_greatest_element = second_greatest(mylist)
print("Second greatest element:", second_greatest_element)