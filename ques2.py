#1
# name=input("enter name")
# word=name.split()
# cap=[]
# for i in word:
#     cap_word=i[0].upper()+i[1:]
#     cap.append(cap_word)
# result=' '.join(cap)
# print(result)

#2
# st=input("enter string")
# result=''
# alphabets=set("abcdefghijklmnopqrstuvwxyz")
# for c in st:
#     if c in alphabets:
#         result=result+c
# print(result)    

#3
# n=int(input("enter no of list items"))
# i=0
# nos=[]
# while(i<n):
#     no=int(input("enter no"))
#     nos.append(no)
#     i+=1
# i=0
# s=[]
# while(i<n): 
#     x=nos[i]**2
#     s.append(x)
#     #print(nos[i],s[i])
#     i=i+1
# print(nos)
# print(s)
    
#4
# sum=0
# for i in range(3):
#     n=int(input("enter number"))
#     sq=n**2
#     sum=sum+sq
# print(sum)

#5
# list1 = []
# list2 = []
# n1 = int(input("Enter the number of elements in the first list: "))
# i = 0
# while i < n1:
#     int1 = int(input("Enter an integer for the first list: "))
#     list1.append(int1)
#     i += 1
# n2 = int(input("Enter the number of elements in the second list: "))
# i = 0
# while i < n2:
#     int2 = int(input("Enter an integer for the second list: "))
#     list2.append(int2)
#     i += 1st=input("Enter a string: ")    
# rev=""
# i=len(st)-1  
# while (i>=0):
#     rev=rev+st[i]
#     i=i-1  
#     s=rev    
# result=s
# print("Reversed string:", result)

# while i<n:
#     no=int(input("entr numbers"))
#     list1.append(no)
#     i=i+1
# j=1
# l=list1[0]
# while j<n:
#     if list1[j]>l:
#         l=list1[j]
#     j=j+1
# print("largest is ",l)


# n=4
# for i in range(0,n):
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()
# n=4
# for i in range(0,n):
#     for s in range(0,n):
#         print(end="  ")
#     n=n-1
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()   
# n=4
# for i in range(0,n):
#     for s in range(0,n):
#         print("*",end=" ")
#     n=n-1
#     print()
# n=4
# for i in range(0,n):
#     for j in range(0,i):
#         print(end="  ")
#     for s in range(0,n):
#         print("*",end=" ")
#     n=n-1 
#     print()



# n=5
# for i in range(1,n):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# n=5
# for i in range(2,n):
#     for j in range(2,i*2,2):
#         print(j,end=" ")
#     print()
# n=5
# k=1
# for i in range(1,n):
#     for j in range(1,i+1):
#         print(k,end=' ')
#         k=k+1
#     print()
# n=5
# k=2
# for i in range(1,n):
#     for j in range(1,i+1):
#         print(k,end=' ')
#         k=k+2
#     print()
n=5
for i in range(1,n):
    for j in range(1,i*2,2):
        print(j,end=" ")
    print()
n=5
k=1
for i in range(1,n):
    for j in range(1,i+1):
        print(k,end=' ')
        k=k+2
    print()
n=5
for i in range(1,n):
    for j in range(2,i*4,2):
        print(j,end=" ")
    print()
n=4
k=1
for i in range(1,n):
    for j in range(1,i*2):
        print(k,end=' ')
        k=k+2
    print()
n=4
k=1
for i in range(1,n):
    for j in range(1,i*2):
        print(k,end=' ')
        k=k+1
    print()