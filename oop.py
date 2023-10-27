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


