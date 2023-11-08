# import tkinter
# w=tkinter.Tk()
# w.geometry('250x250')
# l1=tkinter.Label(text="Name")
# l2=tkinter.Button(text="ok")
# e1=tkinter.Entry()
# l1.grid(row=0,column=0)
# l2.grid(row=1,column=1)
# e1.grid(row=0,column=1)
# w.mainloop()


# from tkinter import*
# w=Tk()
# w.config(background='black')
# w.geometry('350x350')
# l1=Label(w,text='num1')
# e1=Entry(w,width=20)
# l2=Label(w,text='num2')
# e2=Entry(w,width=20)
# l1.grid(row=0,column=0)
# l2.grid(row=1,column=0)
# e1.grid(row=0,column=1,padx=10)
# e2.grid(row=1,column=1,padx=10)
# def add():
#     r=(int(e1.get())+int(e2.get()))
#     e3.delete(0,END)
#     e3.insert(END,r)
# def sub():
#     r=(int(e1.get())-int(e2.get()))
#     e3.delete(0,END)
#     e3.insert(END,r)
# def mul():
#     r=(int(e1.get())*int(e2.get()))
#     e3.delete(0,END)
#     e3.insert(END,r)
# def div():
#     r=(int(e1.get())/int(e2.get()))
#     e3.delete(0,END)
#     e3.insert(END,r)
# b1=Button(w,text='ADD',command=add).grid(row=3,column=0)
# b2=Button(w,text='SUB',command=sub).grid(row=3,column=1)
# b3=Button(w,text='MUL',command=mul).grid(row=3,column=2)
# b4=Button(w,text='DIV',command=div).grid(row=3,column=3)
# e3=Entry(w,width=20)
# e3.grid(row=4,column=1)
# w.mainloop()

# from tkinter import*
# w=Tk()
# w.config(background='black')
# w.geometry('350x350')
# l1=Label(w,text='height')
# l2=Label(w,text='width')
# l3=Label(w,text='area')
# e1=Entry(w,width=20)
# e2=Entry(w,width=20)
# e3=Entry(w,width=20)
# l1.grid(row=0,column=0)
# l2.grid(row=1,column=0)
# l3.grid(row=2,column=0)
# e1.grid(row=0,column=1,padx=10)
# e2.grid(row=1,column=1,padx=10)
# e3.grid(row=2,column=1,padx=10)
# def area():
#     r=(int(e1.get())*int(e2.get()))
#     e3.delete(0,END)
#     e3.insert(END,r)
# b1=Button(w,text='area',command=area).grid(row=3,column=1)
# w.mainloop()


from tkinter import*
w=Tk()
w.config(background='white')
w.geometry('250x250')
l1=Label(w,text='num')
l2=Label(w,text='factorial')
e1=Entry(w,width=20)
e2=Entry(w,width=20)
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
e1.grid(row=0,column=1,padx=10)
e2.grid(row=1,column=1,padx=10)
def fact():
    f=1
    for i in range(1,(int(e1.get()))+1):
        f=f*i
    e2.delete(0,END)
    e2.insert(END,f)
b1=Button(w,text='factorial',command=fact).grid(row=2,column=1)
w.mainloop()               
