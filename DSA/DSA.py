# Q1.What is data structure in python?
#      Data structure is a way to store data in more organized and make read/wrirte operation effcient.
#        1.List:- 
#             Defintion and properties of list:- List is a data tructure used to store multiple data of types in single variable/object/
#             List are mutable (change its data).
#             List can be hoogenous and hetorgenous.
#             List support indexing, slicing and order.
#             List manages memory autamatically (autamatic memory management).
#         * Creation of list:-
#              a. method[]
#              b. method list()

# marks=[90,55,88,69,78,77]
# # print(type(marks))
# i=len(marks)-1
# res=marks[i]
# print(res)

# Slicing
# [start-0:stop-1:step-1]
# marks=[90,55,88,69,78,77,85,45,65,10]
# res=marks[4::2]
# print(res)


# mutability
# marks=[90,55,88,69,78,77,85,45,65,10]
# marks[5]="India"
# marks[1]=85259
# print(marks)

# marks=[90,55,88,69,78,77,85,45,65,10]
# marks[0],marks[-1]=marks[-1],marks[0]
# print(marks)

# traversing
# marks=[85,55,33,85,25,14,66,23,145,22,99]
# for i in range(len(marks)):
#     if marks[i]%2==0:
#        print(marks[i])

# marks=[85,55,33,85,25,14,66,23,145,22,99]
# for i in marks:
#     if i%2==0:
#         print(i)

# sum of all element
# marks=[85,55,33,85,25,14,66,23,145,22,99]
# total_sum=0
# for i in marks:
#     total_sum+=i
#     print(total_sum)

# odd count
marks=[85,55,33,85,25,14,66,23,145,22,99]
odd_count=0
for i in marks:
    if i%2!=0:
        odd_count+=1
        print("odd count: ",odd_count)

#                 Indexing and slicing
#                 Creation of list
#                 Traversing
#                 In-built methods
#                 Assignment and class Activity
#        2.String:-
#        3.Dictionary:-
#        4.store
#        5.Tuple
# Type of data structure in python?
# What is data structure in python?
