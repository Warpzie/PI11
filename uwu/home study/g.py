import tkinter as tk
import turtle
import math
t = turtle.Turtle()
t.speed(0)
t.lt(90)
def domcek(d):
    a = math.sqrt(2*(d*d))
    for i in range(4):
        t.fd(d)
        t.rt(90)
    t.rt(45)
    t.fd(a)
    t.lt(90)
    t.fd(a/2)
    t.lt(90)
    t.fd(a/2)
    t.lt(90)
    t.fd(a)
    t.lt(135)


domcek(20)

turtle.done()
turtle.mainloop()