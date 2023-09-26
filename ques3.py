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

# n=[5,2,3,4,1,3,4,2,3]
# for i in range(0,len(n)):
#     print("*"*n[i])

# st=str(input("enter string"))
# v=set("aeiou")
# vcount=0
# for i in st:
#     if i in v:
#         vcount=vcount+1
# print("no of vowels",vcount)


# st=input("enter string")
# rev=st[::-1]
# if st==rev:
#     print("palindrome")
# else:
#     print("not palindrome")



# sentence=input("enter sentence ")
# words=sentence.split()
# result=""
# for w in words:
#     if w==w[::-1]:
#         for i in range(len(w)):
#             a=len(w)*"@"
#         result=result+a
#     else:
#         result=result+w
#     result=result+" "
# print(result)

# n=[5,1,5,1,1,1]
# for i in range(0,len(n)):
#     print("*"*n[i])

# n=68
# for i in range(65,n):
#     for j in range(i,64,-1):
#         print(chr(j),end=" ")
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(n,0,-1):
#         if j==i or j==n or i==1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")       
#     print()

# km=10
# year=int(input("enter year"))
# if year%4==0:
#     t=km*366
#     print("total km walked=",t)
# else:
#     t=km*365
#     print("total km walked=",t)

m=int(input("enter marks for maths"))
p=int(input("enter marks for physics"))
c=int(input("enter marks for chemistry"))
t=m+p
if m>=55 and p>=50 and c>=50 and t>=140:
    print("passed")
else:
    print("failed")