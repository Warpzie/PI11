import tkinter as tk
import turtle
import random
t = turtle.Turtle()
t.speed(0)
#t.ht()

def kosostvorec(velkost,farba):
    t.fillcolor(farba)
    t.begin_fill()
    t.fd(velkost)
    t.rt(45)
    t.fd(velkost)
    t.rt(135)
    t.fd(velkost)
    t.rt(45)
    t.fd(velkost)
    t.rt(180)
    t.end_fill()
for i in range (4):
    kosostvorec(40,'tan')
    kosostvorec(40,'tomato')


turtle.done()
turtle.mainloop()