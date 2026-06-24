# Find the repetitive elements in the list [1,2,3,4,56,1,22,23,33,23, 56]
def rep_ele(r):
    repetitive=[]
    for i in r:
        if r.count(i)>1 and i not in repetitive:
            repetitive.append(i)
    return repetitive
mylist =[1,2,3,4,56,1,22,23,33,23, 56]
repetitive_elements=rep_ele(mylist)
print(repetitive_elements)

