from tkinter import*
from math import*
def lahenda():
    if (a.get()!=""and b.get()!="" and c.get()!=""):
        a_=int(a.get())
        b_=int(b.get())
        c_=int(c.get())
        D=b_*b_-4*a_*c_

        if D>0:
            x1_=round(-1*b_+sqrt(D))/(2*a_)
            x2_=round(-1*b_-sqrt(D))/(2*a_)
            t=f"X1={x1_}, \nX2={x2_}"
        elif D==0:
            x1_=round(-1*b_)/(2*a_)
            t=f"X1={x1_}"
        else:
            t="Нету корней"
    otvet.configure(text=f"D={D}\n{t}")
    a.configure(bg="purple")
    b.configure(bg="purple")
    c.configure(bg="purple")
aken=Tk()
aken.geometry("600x200")
aken.title("Квадратные уравнения")
lbl=Label(aken,text="Решение квадратного уравнения",font="Calibri 26",fg="black",bg="purple")
lbl.pack()
a=Entry(aken,font="Calibri 26",fg="black",bg="purple",width=3)
a.pack(side=LEFT)
x2=Label(aken,text="x**2+",font="Calibri 26",fg="black")
x2.pack(side=LEFT)
b=Entry(aken,font="Calibri 26", fg="black",bg="purple",width=3)
b.pack(side=LEFT)
y2=Label(aken,text="x+",font="Calibri 26",fg="black")
y2.pack(side=LEFT)
c=Entry(aken,font="Calibri 26",fg="black",bg="purple",width=3)
c.pack(side=LEFT)
z2=Label(aken,text="=0",font="Calibri 26",fg="black")
z2.pack(side=LEFT)
knopka=Button(aken,text="Решить",font="Calibri 30",fg="purple",command=lahenda)
knopka.pack(side=LEFT)
knopka.bind("<Button-1>",lahenda)
otvet=Label(aken,text="Ответ",font="Calibri 15",fg="purple")
otvet.pack(side=BOTTOM)
aken.mainloop()