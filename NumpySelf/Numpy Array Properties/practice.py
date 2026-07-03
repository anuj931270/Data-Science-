import numpy as np

marks= np.array([50,70,80,90,100])
average=np.mean(marks)
highest=np.max(marks)
lowest=np.min(marks)
#Aggregation function
print("Average:",average)
print("Highest:",highest)
print("Lowest:",lowest)
print(sum(marks+2))
print(np.std(marks))
print(np.var(marks))