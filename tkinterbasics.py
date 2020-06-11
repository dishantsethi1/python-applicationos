import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox

win=Tk()
win.geometry('500x500')
#def pr():
#    print('hi')
#win.geometry("500x500")
#b=Button(win,text="button",command=pr,padx=20,pady=30,activeforeground='red')
#b.place(x=100,y=200)

#c=Canvas(win,height=100,width=200,bg='blue')
#coord=10,50,190

#arc=c.create_arc(10,start=0,extent=150,fill='red')    arc not working
#line=c.create_line(10,10,200,200,fill='white')

#c.pack()
'''c1=IntVar()
c2=IntVar()
cb=Checkbutton(win,text='karan aujla ',offvalue=0,onvalue=1,height=5,width=10,variable=c1)
cb.pack()
cb2=Checkbutton(win,text='karan aujla the best singer ',offvalue=0,onvalue=1,height=5,width=30,variable=c2)
cb2.pack()



var=IntVar()
rb=Radiobutton(win,text='karan ',variable=var,value=1)
rb.pack()
rb2=Radiobutton(win,text='karan aujla ',variable=var,value=2)
rb2.pack()'''




            #calculator


'''
def sum(label,x1,x2):
    n1=x1.get()
    n2=x2.get()
    sum=int(n1)+int(n2)
    label.config(text='sum is  %d'%sum)
    return


l1=Label(win,text='first number')
l1.grid(row=1,column=0)
l2=Label(win,text='secong number')
l2.grid(row=2,column=0)

label=Label(win,text='sum is ')
label.grid(row=6,column=4)


x1=StringVar()
x2=StringVar()

e1=Entry(win,textvariable=x1)
e1.grid(row=1,column=2)
e2=Entry(win,textvariable=x2)
e2.grid(row=2,column=2)


sum=partial(sum,label,x1,x2)

button=Button(win,text='calculate',command=sum)
button.grid(row=3,column=0)'''






'''frame=Frame(win)
frame.pack()

frame2=Frame(win)
frame2.pack(side=BOTTOM)


rb=Button(frame,text='red',fg='red')
rb.pack(side=LEFT)


gb=Button(frame2,text='red',fg='green')
gb.pack()'''





#win.title('first')
#top=Toplevel()
#top.title('second')



'''                     #messagebox popup
def p():
    messagebox.showinfo('from computer ','heu there')

b=Button(win,text='popup',command=p)
b.pack()'''



win.mainloop()
