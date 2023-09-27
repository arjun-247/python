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
# print(string())

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
# print(three())


def twolist():
    list1=[]
    n1=int(input("Enter the number of elements in the first list: "))
    for i in range(n1):
        n=int(input("Enter an integer for the first list: "))
        list1.append(n)
    list2=[]
    n2=int(input("Enter the number of elements in the second list: "))
    for i in range(n2):
        n=int(input("Enter an integer for the first list: "))
        list2.append(n)
    common=[]
    for i1 in range(len(list1)):
        for i2 in range(len(list2)):
            if list1[i1]==list2[i2]:
                if list1[i1] not in common:
                    common.append(list1[i1])
    return common
print(twolist())
