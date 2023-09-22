# #1
# list1=[]
# list2=[]
# n1=int(input("enter no of elements in first list"))
# i=0
# while i<n1:
#     int1=int(input("enter number "))
#     list1.append(int1)
#     i+=1
# # print(list1)
# n2=int(input("enter no of elements in first list"))
# i=0
# while i<n2:
#     int2=int(input("enter number "))
#     list2.append(int2)
#     i+=1
# # print(list2)
# output=[]
# i=0
# while i<len(list1):    
#     if(list1[i]%2!=0):
#         odd=list1[i]
#         output.append(odd)
#     i+=1
# j=0
# while j<len(list2):
#     if(list2[j]%2==0):
#         even=list2[j]
#         output.append(even)
#     j+=1    
# print(output)

#2
# list=[]          
# n=int(input("enter no of elements"))
# i=0
# while i<n:
#     item=int(input("enter number "))
#     list.append(item)
#     i+=1
# print(list)
# unique=[]
# for i in list:
#     if i not in unique:
#         unique.append(i)
# print("unique elements are :",unique)

# #3
# st=(input("enter string "))
# ev=[]
# i=0
# while i<len(st):
#     if i%2!=0:
#         ev.append(st[i])
#     i+=1
# print(ev)     

# 4
# n1=int(input("enter first no "))
# n2=int(input("enter second no "))
# for i in range(n1,n2):
#     if i%2==0:
#         print(i)

n=[5,2,3,4,1,3,4,2,3]
for i in range(0,len(n)):
    print("*"*n[i])