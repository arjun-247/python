# list=[]
# def create():
#     l=int(input("enter limit "))
#     for i in range(l):
#         n=int(input("enter number :"))
#         list.append(n)
#     print(list)
# def add():
#     l=int(input("enter number of elements to be added:"))
#     for i in range(l):
#         n=int(input("enter number :"))
#         list.append(n)
#     print(list)
# def remove():
#     r=int(input("enter position of no:"))
#     list.pop(r)
#     print(list)
# def srt():
#     list.sort()
#     print(list)
# def replace():
#     x=int(input("enter position to be replaced"))
#     n=int(input("enter no to be replaced:"))
#     list[x]=n
#     print(list)
# print("list operation \n 1.create list \n 2.add elements \n 3.remove elements \n 4.sort \n 5.replace \n 6.exit")
# while True:
#     n=int(input("enter choice:"))
#     if n==1:
#         create()
#     elif n==2:
#         add()
#     elif n==3:
#         remove()
#     elif n==4:
#         srt()
#     elif n==5:
#         replace()
#     elif n==6:
#         print("exits")
#         break
#     else:
#         print("enter valid no")







# list=[]
# set1=set()
# set2=set()
# set3=set()
# def create():
#     l=int(input("enter limit "))
#     for i in range(l):
#         n=int(input("enter number :"))
#         set1.add(n)
#     print(set1)
# def add():
#     l=int(input("enter number of elements to be added:"))
#     for i in range(l):
#         n=int(input("enter number :"))
#         set1.add(n)
#     print(set1)
# def remove():
#     r=int(input("enter position of no:"))
#     set1.discard(r)
#     print(set1)
# def union():
#     l=int(input("enter limit for first set "))
#     for i in range(l):
#         n=int(input("enter number :"))
#         set2.add(n)
#     l=int(input("enter limit for second set"))
#     for i in range(l):
#         n=int(input("enter number :"))
#         set3.add(n)
#     x=set1.union(set3)
#     print("set1",set2)
#     print("set2",set3)
#     print("union:",x)
#     set1.clear()
#     set2.clear()
# def inersection():
#     l=int(input("enter limit for first set "))
#     for i in range(l):
#         n=int(input("enter number :"))
#         set1.add(n)
#     l=int(input("enter limit for second set"))
#     for i in range(l):
#         n=int(input("enter number :"))
#         set2.add(n)
#     l=int(input("enter limit for third set"))
#     for i in range(l):
#         n=int(input("enter number :"))
#         set3.add(n)
#     x=set1.intersection(set2,set3)
#     print(x)
#     set1.clear()
#     set2.clear()
#     set3.clear()
# print("list operation \n 1.create set \n 2.add elements \n 3.remove elements \n 4.union \n 5.intersection \n 5.exit")
# while True:
#     n=int(input("enter choice:"))
#     if n==1:
#         create()
#     elif n==2:
#         add()
#     elif n==3:
#         remove()
#     elif n==4:
#         union()
#     elif n==5:
#         inersection()
#     elif n==6:
#         print("exits")
#         break
#     else:
#         print("enter valid no")

import random
l=[1,2,3,4,5,6,7]
m=random.choice(l)
print(random.random())