# import random
# l=[1,2,3,4,5,6,7]
# m=random.choice(l)
# print(m)


# import random
# list=['rock','paper','scissor']
# r=random.choice(list)
# n=input("enter rock,paper,scissor:")
# if r==list[0] and n==list[1]:
#     print(n,"vs",r)
#     print("paper wins")
# elif r==list[1] and n==list[1]:
#     print(n,"vs",r)
#     print("tie")
# elif r==list[2] and n==list[1]:
#     print(n,"vs",r)
#     print("sccissor wins")
# elif r==list[0] and n==list[0]:
#     print(n,"vs",r)
#     print("tie")
# elif r==list[1] and n==list[0]:
#     print(n,"vs",r)
#     print("paper wins")
# elif r==list[2] and n==list[0]:
#     print(n,"vs",r)
#     print("rock wins")
# elif r==list[0] and n==list[2]:
#     print(n,"vs",r)
#     print("rock wins")
# elif r==list[1] and n==list[2]:
#     print(n,"vs",r)
#     print("scissor wins")
# elif r==list[2] and n==list[2]:
#     print(n,"vs",r)  
#     print("tie")
# else:
#     print("enter valid choice")


import random
list=['apple','banana','grape']
f=random.choice(list)   
totalchance=5
chances=totalchance
word=["_"] * len(f)
while chances > 0:
    print(" ".join(word))
    n=input("guess the fruit:")
    if len(n)!=1:
        print("enter single letter")
        continue
    if n in f:
        for i in range(len(f)):
            if f[i]==n:
                word[i]=n
        if "".join(word)==f:
            print("correct",f)
            break
    else:
        chances -= 1
        print("chance left",chances)

if chances==0:
    print("out of chances",f)

# pas='1234'
# f=["*"]*len(pas)
# tc=3
# c=tc
# while c>0:
#     print(" ".join(f))
#     n=input("enter password")
#     if n==pas:
#         print("login successful")
#         break
#     else:
#         c-=1
#         print("error wrong password")
# if c==0:
#     print("try again")

# user=['ar','ab']
# pas=['12','jjj']
# tc=3
# c=tc
# while c>0:
#     u=input("enter username")
#     for i in range(len(user)):
#         if u==user[i]:
#             p=input("password:")
#             if p==pas[i]:
#                 print("login succesful")
#                 break
#             else:
#                 c-=1
#                 print("error wrong password")
# if c==0:
#     print("try again")

            

