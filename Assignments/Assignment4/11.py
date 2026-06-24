#  Write a Python program to duplicate all items in the list l = [1, 2, 3] to
# produce the result:
# result = [1, 2, 3, 1, 2, 3, 1, 2, 3].

def duplicate_list(original_list,d):#function name duplicate_list, 
    result=[]
    for _ in range(d):
        result.extend(original_list) #extend adds all items from l at once
    return result
mylist=[1,2,3]
duplicate=duplicate_list(mylist,3)
print("Duplicate List: ",duplicate)