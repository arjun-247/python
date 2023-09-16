# print("hello")
# x=5
# y=float(x)
# print(type(x))
# print(type(y))
# z=3+2j
# print(type(z))
# a=5
# b=6
# c=0
# print("a =",a)
# print("b =",b)
# c=a
# a=b
# b=c
# print("a =",a)
# print("b =",b)
# a,b=b,a
# print(a,b)


# list1=[2,3,"hi",76]
# print(list1[2])


# tuple1=(1,2,"abc","def",7)
# print(type(tuple1))
# print(tuple1)
# tuple2=list(tuple1)
# tuple2[1]="zxc"
# tuple1=tuple(tuple2)
# print(type(tuple1))
# print(tuple1)

# fruits=["apple","orange","banana"]
# fruits.append("grapes")
# fruits.clear()
# x=fruits.copy()
# print(x)
# x=fruits.count("banana")
# print(x)
# cars=["ford","benz","ferrari"]
# fruits.extend(cars)
# x=fruits.index("apple")
# print(x)
# fruits.insert(2,"grapes")
# fruits.pop(2)
# fruits.remove("orange")
# fruits.reverse()
# fruits.sort()
# print(fruits)


# if(5<2):
#     print("greater")
# else:
#     print("not greater")
# a=5
# b=3
# if(a>b):
#     print("a is greater")
# elif(a<b):
#     print("b is greater")
# else:
#     print("a and b are equal")

# a=int(input("enter the number:"))
# if(a%2==0):
#     print("even")
# else:
#     print("odd")
    
# a=int(input("enter 1st number:"))
# b=int(input("enter 2nd number:"))
# c=int(input("enter 3rd number:"))
# if(a>b and a>b):
#     print(a," is greater")
# elif(b>a and b>c):
#     print(b," is greater")
# else:
#     print(c,"is greater")
    
# a=int(input("enter year:"))
# if(a%4==0):
#     print("leap year")
# else:
#     print("not a leap year")

# a=int(input("enter number:"))
# if(a>0):
#     print("positive")
# elif(a<0):
#     print("negative")
# else:
#     print("zero")

# a=int(input("enter marks:"))
# p=((a/100)*100)
# if(p>=90):
#     print("A+")
# elif(p>=80 and p<90):
#     print("A")
# elif(p>=70 and p<80):
#     print("B+")
# elif(p>=60 and p<70):
#     print("B")
# elif(p>=50 and p<60):
#     print("C+")
# elif(p>=40 and p<50):
#     print("C")
# elif(p<40):
#     print("fail")
# else:
#     print("try again")

# to check whether no is divisible by 5 and 7
# to display hello if a number entered is divisible by 5
# to display last digit of entered no
# to check last digit is divisible by 3


# n=int(input("enter number "))
# if(n%5==0 and n%7==0):
#     print("divisible")
# else:
#     print("not divisible")
    

# n=int(input("enter number "))
# if(n%5==0):
#     print("hello")
# else:
#     print("bye")


# n=int(input("enter number "))    
# r=n%10
# print(r)


# n=int(input("enter number "))    
# r=n%10
# if(r%3==0):
#       print("divisible") 
# else:
#     print("not divisible")
    
# u=int(input("enter unit:"))
# t=0
# if(u<100):
#     print("no charge")
# elif(u>100 and u<200):
#     t=(u-100)*5
#     print(t)
# elif(u>200):
#     t=((u-200)*10)+500
#     print(t)

# n=int(input("enter number "))
# d={1:"sunday",2:"monday",3:"tuesday",4:"wednesday",5:"thursday",6:"friday",7:"saturday"}
# print(d[n])          

# n=int(input("enter number of days"))
# d={31:["january","march","may","july","august","october","december"],28:"february",30:["april","june","september","november"]}
# print(d[n])
# m=input("enter month")
# if(m in d[31]):
#     print("31 days")
# elif(m in d[30]):
#     print("30 days")
# else:
#     print("28 days")

# n=int(input("enter number"))
# b=0
# while(n>0):
#     a=n%10
#     b=b*10+a
#     n=n//10
# print(b)

# i=0
# while(i<=10):
#     print("hello")
# #     i=i+1
# i=0
# for i in range(10):
#     print("hi")    

# i=0
# s=0
# while(i<10):
#     n=int(input("enter number"))
#     s=n+s
#     i=i+1    
# print("sum is",s)    

# i=0
# while(i<20):
#     i=i+2
#     print(i)

# i=1
# while(i<=10):
#     print(2*i-1)
#     i=i+1
# for i in range(1,20,2):
#     print(i)
    
# i=1
# s=0
# while(i<=10):
#     s=i**2
#     print(i,s)
#     i=i+1


# i=0
# s=0
# while(i<20):
#     s=i+s
#     i=i+2
# print(s)


# num = int(input("Enter a number "))  
# f = 0
# i = 2
# while (i <= num / 2):
#     if num % i == 0:
#         f=1
#         break
#     i=i+1
    
# if f==0:
#     print("PRIME number")
# else:
#     print("not a PRIME number")
    
 

for i in range(200,2700):
    if(i%5==0 and i%7==0):
        print(i)


