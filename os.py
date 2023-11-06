def create():
    n=input("enter file name:")
    f=open(n,'x')
    f.close()
    # print(f.read())
def write():
    n=input("enter file name:")
    f=open(n,'a')
    s=input("enter content ")
    f.write(s)
    f.close()
    # print(f.read())
def read():
    n=input("enter file name:")
    f=open(n,'r')
    print(f.read())
def remove():
    import os
    n=input("enter file name to remove:")
    if os.path.exists(n):
        os.remove(n)
    else:
        print("file does not exists")
while True:
    print("1.create\n2.write\n3.read\n4.remove\n5.exit")
    n=int(input("enter choice "))
    if n==1:
        create()
    elif n==2:
        write()
    elif n==3:
        read()
    elif n==4:
        remove()
    elif n==5:
        break
    else:
        print("invalid")
        break
