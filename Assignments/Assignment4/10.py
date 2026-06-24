# Find all non-repetitive elements in the list[1,2,3,4,56,1,22,23,33,23,56].
def non_repetitive(n):
    non_repetitive_elements=[]
    for i in n:
        if n.count(i)==1 and i not in non_repetitive_elements:
            non_repetitive_elements.append(i)
    return non_repetitive_elements
mylist=[1,2,3,4,56,1,22,23,33,23,56]
elements=non_repetitive(mylist)
print(elements)