import tkinter
import turtle
import random
t = turtle.Turtle()
t.speed(0)
t.pensize(10)
t.pencolor('gold')
def slnko(pocet, velkost):
    t.dot(velkost)
    for i in range (pocet):
        t.rt(360/pocet)
        t.fd(velkost*1.5)
        t.rt(180)
        t.fd(velkost*1.5)
        t.rt(180)
slnko(10,100)
def nove_slnko():
    t.clear()
    slnko(random.randint(3,20),random.randint(20,100))
tkinter.Button(text="nove slnko",command=nove_slnko).pack()
turtle.mainloop()
