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







list=[]
set=set()
def create():
    l=int(input("enter limit "))
    for i in range(l):
        n=int(input("enter number :"))
        set.add(n)
    print(set)
def add():
    l=int(input("enter number of elements to be added:"))
    for i in range(l):
        n=int(input("enter number :"))
        set.add(n)
    print(set)
def remove():
    r=int(input("enter position of no:"))
    set.discard(r)
    print(set)
print("list operation \n 1.create list \n 2.add elements \n 3.remove elements  \n 4.exit")
while True:
    n=int(input("enter choice:"))
    if n==1:
        create()
    elif n==2:
        add()
    elif n==3:
        remove()
    elif n==4:
        print("exits")
        break
    else:
        print("enter valid no")    