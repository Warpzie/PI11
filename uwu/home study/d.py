import random
import tkinter as tk
import turtle
t = turtle.Turtle()
t.speed(0)
root = tk.Tk()
t.lt(90)

def strom(kmen ,koruna):
    t.width(15)
    t.color('brown')
    t.fd(kmen)
    t.width(40)
    t.color('green')
    t.fd(koruna)
    t.pu()
    t.rt(180)
    t.fd(kmen + koruna)
    t.rt(180)
    t.pd()
global pocet
pocet = 8
def stromy(pocet):
    for i in range(pocet):
        strom(random.randint(30,60),random.randint(10,40))
        t.pu()
        t.rt(90)
        t.fd(50)
        t.lt(90)
        t.pd()
stromy(pocet)
def back():
    t.pu()
    t.clear()
    t.setpos(-200,0)
    t.pd()
global newPocet
def pridaj():
    newPocet=pocet+1
    back()
    stromy(newPocet)
pridajB=tk.Button(root,text="pridaj",command=pridaj)
pridajB.pack()
def uber():
    newPocet=pocet-1
    back()
    stromy(newPocet)
uberB=tk.Button(root,text="uber",command=uber)
uberB.pack()

turtle.done()
turtle.mainloop()