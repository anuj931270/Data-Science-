import numpy as np
mylist=np.array([5,6,7,8,11,10])
list=np.array([11,12,13,14,15,16])
print(mylist+list)
print(mylist*5)
print(mylist+5)
print(mylist**2)
print(mylist-5)
print(mylist/5)
print(np.sum(mylist))
print(np.mean(mylist))  #average
print(np.max(mylist))  #minimum
print(np.min(mylist))  #maximum
print(np.sort(mylist)) #sorting
print(mylist[mylist>5]) #Filtering
print(list+5) #broadcasting