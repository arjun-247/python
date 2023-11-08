# def add():
#     a=10
#     b=20
#     s=a+b
#     print(s)
# add()

# def add(a,b):
#     n=a
#     m=b
#     s=n+m
#     print(s)
# add(5,10)

# def add(a,b):
#     n=a
#     m=b
#     s=n+m
#     return s
# p=int(input("enter no"))
# k=(int(input("enter no ")))
# print(add(p,k))


# def capital(name):
#     list=[]
#     result=""
#     words=name.split()
#     for i in words:
#         c=i.capitalize()
#         list.append(c)
#     result=' '.join(list)
#     return result
# name=input("enter name ")
# s=capital(name)
# print(s)


# def string():
#     st=""
#     alphabets=set("abcdefghijklmnopqrstuvwxyz")
#     for i in strg:
#         if i in alphabets:
#             st=st+i
#     return st
# strg=input("enter string with special characters ")
# print("string without special characters ",string())


# def squ(n):
#     no=[]
#     for i in range(n):
#         s=int(input("enter no "))
#         no.append(s)
#     square=[]
#     for i in range(n):
#         sq=no[i]**2
#         square.append(sq)
#     return no,square
# s=int(input("enter limit"))
# print(squ(s))


# def three():
#     sum=0
#     for i in range(3):
#         n=int(input("enter no "))
#         sq=n**2
#         sum=sum+sq 
#     return sum
# print("sum of squares of three numbers ",three())


# def twolist():
#     list1=[]
#     n1=int(input("Enter the number of elements in the first list: "))
#     for i in range(n1):
#         n=int(input("enter integer for first list "))
#         list1.append(n)
#     list2=[]
#     n2=int(input("Enter the number of elements in the second list: "))
#     for i in range(n2):
#         n=int(input("enter integer for second list "))
#         list2.append(n)
#     common=[]
#     for i1 in range(len(list1)):
#         for i2 in range(len(list2)):
#             if list1[i1]==list2[i2]:
#                 if list1[i1] not in common:
#                     common.append(list1[i1])
#     return common
# print("common elements are ",twolist())


# def fact():
#     n=int(input("enter number"))
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     return f
# print("factorial is ",fact())

# def fib():
#     n=int(input("enter no of terms"))
#     f=[0,1]
#     for i in range(n-2):
#         b=f[i]+f[i+1]
#         f.append(b)
#     return f
# print(fib())

# def prime():
#     n=int(input("enter limit"))
#     p=[]
#     for i in range(0,n+1):
#             if i%2!=0 or i==2: 
#                 if i%3!=0 or i%5!=0:
#                     print(i)       
# prime()


# n=5
# for i in range(n):
#     for j in range(n,i+1,-1):
#         print(" ",end="")
#     for j in range(2*i+1):
#         if j==0 or j==2*i:
#             print("*",end="")
#         elif i==2:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()



# n = 6
# for i in range(1, n + 1):
#     for j in range(0,i):
#         print("*",end="")
#     print()
#     if i % 2 == 0:
#         for j in range(1, i + 1):
#             print(j, end="")
#     else:
#         for j in range(i, 0, -1):
#             print(j, end="")
#     print()



# def binarynum():
#     binary=""
#     d=n
#     while d>0:
#         binary=str(d%2)+binary
#         d=d//2
#     return binary
# def octalnum():
#     octal=""
#     o=n
#     while o>0:
#         octal=str(o%8)+octal
#         o=o//8
#     return octal
# def hexadecimal():
#     hexa=""
#     h=n
#     while h>0:
#         r=h%16
#         if r<10:
#             hexa=str(r)+hexa
#         else:
#             hexa= chr(65+(r-10)) + hexa
#         h//=16
#     return hexa
# n=int(input("enter number "))
# print("binary :",binarynum()) 
# print("octal :",octalnum())
# print("hexa decimal :",hexadecimal())


# n=int(input("enter limit"))
# asc=[]
# dec=[]
# for i in range(n):
#     a=int(input("enter no :"))
#     asc.append(a)
#     dec.append(a)
# asc.sort()
# dec.sort(reverse=True)
# print("ascending order :",asc)
# print("desc order :",dec)



# def fib(): 
#     f=[0,1]
#     for i in range(100) :
#         b=f[i]+f[i+1]
#         f.append(b)
#     r=[]
#     for i in range(len(f)):
#         if f[i]<n:
#             r.append(f[i])
#     return r
# n=int(input("enter no"))
# print(fib())



# list=[3,8,12,7,6,10,21,15]
# for i in range(len(list)):
#     for j in range(len(list)):
#         if list[i]+list[j]==18:
#             print(list[i],list[j])


# list = ["apple", "banana", "cherry", "date"]
# for i in range(len(list)):
#     for j in range(len(list)):
#         for c in list[i]:
#             if c in list[j]:
#                 print(list[i],list[j])
#                 break

# list=[2,3,4,5,6]
# print("numbers whose sum is odd")
# for i in range(len(list)):
#     for j in range(i,len(list)):
#         s=list[i]+list[j]
#         if s%2!=0:
#             print(list[i],list[j])
# print("numbers whose product is even")
# for i in range(len(list)):
#     for j in range(i+1,len(list)):
#         p=list[i]*list[j]
#         if p%2==0:
#             print(list[i],list[j])   


# str = input("Enter sentnce: ")
# words=str.split()
# print("no of words in the sentence:",len(words))

# def longest_word():
#     sent=input("enter a sentence")
#     words=sent.split()
#     result=""
#     length=0
#     for i in words:
#         if(len(i)>length):
#             result=i
#             length=len(i)
#     return result
# print(longest_word())

# def capital():
#     words=sent.split()
#     cap=[]
#     for i in words:
#         if i[0].isupper():
#             cap.append(i)
#     return cap
# sent=input("enter a sentence")
# print(capital())



# nums=[2,7,11,15]
# target=9
# result=[]
# for i in range(len(nums)):
#     for j in range(1,len(nums)):
#         if(nums[i]+nums[j]==target):
#             result.append(i) 
#             result.append(j) 
# print(result) 

# x=int(input("enter no:"))
# y=x**0.5
# print(int(y))          

# def wrds():
#     snt=input("enter sentence")
#     word_count=0
#     words=0
#     for i in range(len(snt)):
#         if snt[i].isspace():
#             words=0
#         elif not words:
#             words=1
#             word_count+=1
#     return word_count
# print(wrds())

# def long():
#     sent=input("enter sentence")
#     words=sent.split()
#     longest_word=""
#     length=0
#     for i in range(len(words)):
#         if len(words[i])>length:
#             longest_word=words[i]
#             length=len(words[i])
#     return longest_word
# print(long())

# def capital():
#     sent=input("enter sentence ")
#     words=sent.split()
#     for i in words:
#         if i[0].isupper():
#             print(i)
# capital()

