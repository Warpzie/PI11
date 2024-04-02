import tkinter as tk
import turtle
import random
t = turtle.Turtle()
t.speed(0)
root = tk.Tk()
t.color('gold')

def slnko(pocet,velkost):
    t.dot(velkost)
    for i in range(pocet):
        t.fd(velkost *2)
        t.rt(180)
        t.fd(velkost * 2)
        t.rt(180)
        t.rt(360/pocet)
def newSlnko():
    t.clear()
    velkost = random.randrange(20, 100)
    pocet = random.randrange(3, 20)
    slnko(pocet,velkost)
new = tk.Button(root,text="nove slnko",command=newSlnko)
new.pack()
turtle.done()
turtle.mainloop()