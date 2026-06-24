#  Arrange the list [1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56] in
# # ascending order.

def ascending_order(a):
    a.sort()
    return a
mylist =[1, 2, 3, 4, 56, 1, 22, 23, 33, 23, 56]
sort_short=ascending_order(mylist)
print(sort_short)
