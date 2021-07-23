import tkinter as tk
from tkinter import *
from tkinter import messagebox

value=''
int_value=0
operator=''

# functions
def btn1_clicked():
    global value
    value=value + "1"
    data.set(value)

def btn2_clicked():
    global value
    value= value+"2"
    data.set(value)

def btn3_clicked():
    global value
    value= value+"3"
    data.set(value)

def btn4_clicked():
    global value
    value= value+"4"
    data.set(value)

def btn5_clicked():
    global value
    value= value+"5"
    data.set(value)

def btn6_clicked():
    global value
    value= value+"6"
    data.set(value)

def btn7_clicked():
    global value
    value= value+"7"
    data.set(value)

def btn8_clicked():
    global value
    value= value+"8"
    data.set(value)

def btn9_clicked():
    global value
    value= value+"9"
    data.set(value)

def btn0_clicked():
    global value
    value= value+"0"
    data.set(value)

def btnadd_clicked():
    global int_value
    global operator
    global  value
    int_value=int(value)
    operator='+'
    value=value +"+"
    data.set(value)

def btnsub_clicked():
    global int_value
    global operator
    global value
    int_value = int(value)
    operator = '-'
    value = value + "-"
    data.set(value)

def btnmul_clicked():
    global int_value
    global operator
    global value
    int_value = int(value)
    operator = 'x'
    value = value + "x"
    data.set(value)

def btndiv_clicked():
    global int_value
    global operator
    global value
    int_value = int(value)
    operator = '/'
    value = value + "/"
    data.set(value)

def btnclear_clicked():
    global int_value
    global  operator
    global value
    value=''
    int_value=0
    operator=''
    data.set(value)

def btnequal_clicked():
    global int_value
    global operator
    global value
    value2=value
    if operator=='+':
        x= (int(value2.split("+")[1]))
        c= int_value+x
        data.set(c)
        value=str(c)

    elif operator=='-':
        x= (int(value2.split("-")[1]))
        c= int_value-x
        data.set(c)
        value=str(c)

    elif operator=='x':
        x= (int(value2.split("x")[1]))
        c= int_value * x
        data.set(c)
        value=str(c)

    elif operator == '/':
        x = (int(value2.split("/")[1]))
        if x==0:
            messagebox.showerror("Error","Division by Zero")
            int_value=0
            value=''
            data.set(value)
        else:
            c = int(int_value / x)
            data.set(c)
            value = str(c)


# initializing window
window=tk.Tk()
window.title("Calculator Project")
#window.configure(background='Green')
window.geometry('300x400+300+90')
window.resizable(0,0)

# creating label
data= StringVar()
label1=Label(
        window,text="Label",anchor=SE,font=("Verdana",20),
        textvariable=data,background='White',fg='Black'
            )  # SE=South-east

label1.pack(expand=True, fill= "both")

# creating frames

frame1= Frame(window,bg='Black') # you can use --> bg="#000000" for black
frame1.pack(expand=True, fill= "both")

frame2= Frame(window)
frame2.pack(expand=True, fill= "both")

frame3= Frame(window)
frame3.pack(expand=True, fill= "both")

frame4= Frame(window)
frame4.pack(expand=True, fill= "both")

# creating buttons for frame1
btn1=Button(frame1,text="1", font=("Verdana",22),relief=GROOVE,border=0,command=btn1_clicked)
btn1.pack(side=LEFT,expand=True,fill='both')

btn2=Button(frame1,text="2", font=("Verdana",22),relief=GROOVE,border=0,command=btn2_clicked)
btn2.pack(side=LEFT,expand=True,fill='both')

btn3=Button(frame1,text="3", font=("Verdana",22),relief=GROOVE,border=0,command=btn3_clicked)
btn3.pack(side=LEFT,expand=True,fill='both')

btnadd=Button(frame1,text="+", font=("Verdana",22),relief=GROOVE,border=0,command=btnadd_clicked)
btnadd.pack(side=LEFT,expand=True,fill='both')





# creating buttons for frame2
btn4=Button(frame2,text="4", font=("Verdana",22),relief=GROOVE,border=0,command=btn4_clicked)
btn4.pack(side=LEFT,expand=True,fill='both')

btn5=Button(frame2,text="5", font=("Verdana",22),relief=GROOVE,border=0,command=btn5_clicked)
btn5.pack(side=LEFT,expand=True,fill='both')

btn6=Button(frame2,text="6", font=("Verdana",22),relief=GROOVE,border=0,command=btn6_clicked)
btn6.pack(side=LEFT,expand=True,fill='both')

btnsub=Button(frame2,text="-", font=("Verdana",22),relief=GROOVE,border=0,command=btnsub_clicked)
btnsub.pack(side=LEFT,expand=True,fill='both')




# creating buttons for frame3
btn7=Button(frame3,text="7", font=("Verdana",22),relief=GROOVE,border=0,command=btn7_clicked)
btn7.pack(side=LEFT,expand=True,fill='both')

btn8=Button(frame3,text="8", font=("Verdana",22),relief=GROOVE,border=0,command=btn8_clicked)
btn8.pack(side=LEFT,expand=True,fill='both')

btn9=Button(frame3,text="9", font=("Verdana",22),relief=GROOVE,border=0,command=btn9_clicked)
btn9.pack(side=LEFT,expand=True,fill='both')

btnmul=Button(frame3,text="x", font=("Verdana",22),relief=GROOVE,border=0,command=btnmul_clicked)
btnmul.pack(side=LEFT,expand=True,fill='both')





# creating buttons for frame4
btnclear=Button(frame4,text="C", font=("Verdana",22),relief=GROOVE,border=0,command=btnclear_clicked)
btnclear.pack(side=LEFT,expand=True,fill='both')

btn0=Button(frame4,text="0", font=("Verdana",22),relief=GROOVE,border=0,command=btn0_clicked)
btn0.pack(side=LEFT,expand=True,fill='both')

btnequal=Button(frame4,text="=", font=("Verdana",22),relief=GROOVE,border=0,command=btnequal_clicked)
btnequal.pack(side=LEFT,expand=True,fill='both')

btndiv=Button(frame4,text="/", font=("Verdana",22),relief=GROOVE,border=0,command=btndiv_clicked)
btndiv.pack(side=LEFT,expand=True,fill='both')


window.mainloop()
