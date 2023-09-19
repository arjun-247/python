#1
# i=0
# n=10
# while(i<=n):
#     s=(input("enter a string"))
#     no=s
#     i=i+1
#     print(no,len(no))
    
#2     
# d={}
# a=str(input("enter string "))
# i=0
# while(i<len(a)):
#     s=a[i]
#     if(s in d):
#         d[s]=d[s]+1
#     else:
#         d[s]=1
#     i=i+1
# print(d)

#3
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
#     i += 1
# common= []
# i1 = 0
# while i1 < len(list1):
#     i2 = 0
#     while i2 < len(list2):
#         if list1[i1] == list2[i2]:
#             common.append(list1[i1])
#             break
#         i2 += 1
#     i1 += 1
# print("Common elements:", common)


# #4
st=input("Enter a string: ")    
rev=""
# i=len(st)-1  
# while (i>=0):
#     rev=rev+st[i]
#     i=i-1  
#     s=rev    
# result=s
s=st[5]
print("Reversed string:",s) #result)

#5
# i=0
# s=0
# while(i<10):
#     n=int(input("enter number"))
#     s=n+s
#     i=i+1    
# print("sum is",s)

#6
# a=int(input("enter no of list items"))
# list=[]
# while(a>0):
#     b=int(input("enter number "))
#     a=a-1
#     list.append(b)
#     list.sort()
# print("largest is",list[-1])

#7
# str = input("Enter a string: ")
# word_count = 0
# i = 0
# word = 0 
# while i < len(str):
#     if str[i].isspace():
#         word = 0 
#     elif not word:
#         word = 1  
#         word_count += 1      
#     i += 1
# print("Number of words in the string:", word_count)

#8
# inp = []
# n = int(input("Enter the number of strings: "))
# i = 0
# while i < n:
#     string = input("Enter a string: ")
#     inp.append(string)
#     i =i+1
# output = []
# i = 0
# while i < len(inp):
#     c = inp[i]   
#     if len(c) > 5:
#         output.append(c)    
#     i += 1
# print("Strings with more than five characters:", output)

#9
# inp=[]
# n=int(input("enter no of integers"))
# i=0
# while(i<n):
#     no=int(input("enter number "))
#     inp.append(no)
#     i+=1
# out=[]
# i=0
# while(i<len(inp)):
#     if(inp[i]%2==0):
#         out.append(inp[i])
#     i+=1
# print("even numbers are:",out)

#10
# input_list = []
# n = int(input("Enter the number of strings: "))
# i = 0
# while i < n:
#     string = input("Enter a string: ")
#     input_list.append(string)
#     i += 1
# output_list = []
# i = 0
# while i < len(input_list):
#     current_string = input_list[i]
#     capitalized_string = current_string[0].upper() + current_string[1:]
#     output_list.append(capitalized_string)    
#     i += 1
# print("Strings with the first letter capitalized:", output_list)
