# class circle:
#     def __init__(self,radius) :
#         self.radius=radius
#         self.p=3.14
#     def __str__(self) -> str:
#         return f"radius is {self.radius} "
#     def getArea(self):    
#         area=self.p*(self.radius**2)
#         print("area is",area)
#     def getCircumference(self):
#         c=2*self.p*self.radius
#         print("circumference is",c)            
# r=circle(5)
# print(r)
# r.getArea()
# r.getCircumference()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  

# class temperature:
#     def getDegree(self,fahren):
#         celsius = (fahren - 32) * 5/9
#         return celsius
#     def getFahrenheit(self,cels):
#         fahrenheit = (cels * 9/5) + 32
#         return fahrenheit
# temp=temperature()
# degree=float(input("enter celsius "))
# result=temp.getFahrenheit(degree)
# print(f"temperature in fahrenheit {result}F")
# fahren=float(input("enter fahrenheit "))
# result1=temp.getDegree(fahren)
# print(f"temperature in degree celsius {result1}C")


# class student:
#     def __init__(self,name,rno) :
#         self.name=name
#         self.rollno=rno
#     def display(self):
#         print(self.name,self.rollno)
#     def setage(self,age):
#         self.age=age
#     def setmark(self,mark):
#         self.marks=mark
#     def dis(self):
#         print(self.age,self.marks)
# s=student("john",18)
# s.display()
# s.setage(24)
# s.setmark(100)
# s.dis()


# class Time():
#     def __init__(self,hours,mins) :
#         self.hours=hours
#         self.mins=mins
#     def addtime(t1,t2):
#         t3=Time(0,0)
#         if t1.mins + t2.mins > 60:
#             t3.hours=(t1.mins+t2.mins)/60
#             t3.hours=t3.hours+t1.hours+t2.hours
#             t3.mins=(t1.mins+t2.mins)-(((t1.mins+t2.mins)/60)*60)
#             return t3
#     def displayTime(self):
#         print("time is",self.hours,"hours and",self.mins,"minutes")
#     def minutes(self):
#         print(int(self.hours*60)+self.mins)
# a=Time(2,50)
# b=Time(1,20)
# c=Time.addtime(a,b)
# c.displayTime()
# c.minutes()


# class bank:
#     def __init__(self,name,acc,bal) :
#         self.name=name
#         self.accountnumber=acc
#         self.balance=bal
#     def deposit(self,amount):
#         self.balance=self.balance+amount
#         print("balance is",self.balance)
#     def withdrawal(self,wit):
#         self.balance-=wit
#         print("balance is",self.balance)
# n=input("enter name")
# a=input("enter account number")
# b=int(input("enter balance"))
# am=int(input("enter amount to deposit"))
# d=int(input("enter amount to withdraw"))
# bnk=bank(n,a,b)
# bnk.deposit(am)
# bnk.withdrawal(d)



# class bank:
#     def __init__(self,name,acc,bal) :
#         self.name=name
#         self.accountnumber=acc
#         self.balance=bal
#     def deposit(self):
#         amount=int(input("enter amount to deposit"))
#         self.balance=self.balance+amount
        
#     def withdrawal(self):
#         wit=int(input("enter amount to withdraw"))
#         self.balance-=wit
        
#     def showbal(self):
#         print(self.name,'\n',self.balance)
# l=[]
# def create():
#     n=input("enter name")
#     a=int(input("enter account number"))
#     b=int(input("enter balance"))
#     bnk=bank(n,a,b)
#     l.append(bnk)
# while True:
#     choice=int(input("enter choice 1.create 2.deposit 3.withdraw 4.exit:"))
#     if choice==1:
#         create()
#     elif choice==2:
#         accno=int(input("enter account number"))
#         for i in l:
#             if accno==i.accountnumber:
#                 i.deposit()
#                 i.showbal()
#     elif choice==3:
#         accno=int(input("enter account number"))
#         for i in l:
#             if accno==i.accountnumber:
#                 i.withdrawal()
#                 i.showbal()
#                 print(l)
#     elif choice==4:
#         break
#     else:
#         print("invalid")
#         break
    

class Employee:
    def __init__(self,id,name,salary,dep) :
        self.emp_name=name
        self.emp_id=id
        self.emp_salary=salary
        self.emp_dept=dep
    def print_employee_details(self):
        print(f"Name:{self.emp_name} \nID:{self.emp_id} \nSalary:{self.emp_salary} \nDepartment:{self.emp_dept}")
    def calculate_salary(self):
        time=int(input("enter hours worked:"))
        if time>50:
            ot=time-50
            self.emp_salary+=((ot)*(self.emp_salary/50))
        else:
            self.emp_salary=self.emp_salary
list=[]
def create():
    nme=input("enter name:")
    id=input("enter employee id:")
    sal=int(input("enter slary:"))
    dep=input("enter department:")
    emp=Employee(id,nme,sal,dep)
    list.append(emp)
while True:
    print("1.create\n2.print employee details\n3.calculate salary")
    n=int(input("enter choice:"))
    if n==1:
        create()
    elif n==2:
        eid=input("enter employee id")
        for i in list:
            if eid == i.emp_id:
                i.print_employee_details()
            else:
                print("enter correct id")
    elif n==3:
        eid=input("enter employee id")
        for i in list:
            if eid == i.emp_id:
                i.calculate_salary()
                i.print_employee_details()
    else:
        print("invalid")
        break
            


