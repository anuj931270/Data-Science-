# Remove all the odd elements from the list [10, 23, 11,12,33,44,2,5, 6]

def odd_elements(o):
    odd_count=[]
    for i in o:
        if i %2==0:
            odd_count.append(i)
    return odd_count

mylist =[10, 23, 11,12,33,44,2,5, 6]
odd_list=odd_elements(mylist)
print("List after removing odd elements: ",odd_list)


