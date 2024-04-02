import tkinter as tk
import turtle
t = turtle.Turtle()
t.speed(0)
t.ht()


def spirala(d,krok,uhol):
    for i in range (100):
        t.fd(d+krok*i)
        t.rt(uhol)
        if t.distance(0,0)>250:
            break
spirala(5,5,25)
def rob(value):
    t.clear()
    t.reset()
    t.speed()
    t.ht()
    spirala(10,int(value),90)
posuvac = tk.Scale(command=rob,orient='horizontal',from_=5,to=179,length=300).pack()

turtle.done()
turtle.mainloop()