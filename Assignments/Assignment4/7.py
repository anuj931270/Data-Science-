# Find the greatest element in the list [89, 23, 24, 2, 55, 54, 64].

def greatest_no(g):
    greatest= g[0]
    for i in g:
        if i>greatest:
            greatest=i
    return greatest
mylist= [89, 23, 24, 2, 55, 54, 64]
greatest_element = greatest_no(mylist)
print("The greatest element is:", greatest_element)