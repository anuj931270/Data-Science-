#  Reverse the list [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56]

def reverse_list(r):
    reverse=[]
    for i in range(len(r)-1,-1,-1):
        reverse.append(r[i])
    return reverse
mylist=[1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56]
reverse_ele=reverse_list(mylist)
print(reverse_ele)