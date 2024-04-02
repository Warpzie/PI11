import tkinter as tk
import turtle
t = turtle.Turtle()
t.speed(0)
t.width(3)
t.color('blue')
t.fillcolor('red')
root = tk.Tk()
def dopredu():
    t.fd(50)
dopreduB = tk.Button(root, text="Dopredu", command=dopredu)
dopreduB.pack()

def vpravo():
    t.rt(90)
vpravoB = tk.Button(root, text="vpravo", command=vpravo)
vpravoB.pack()

def vlavo():
    t.lt(18)
vlavoB = tk.Button(root, text="vlavo", command=vlavo)
vlavoB.pack()

def begin():
    t.begin_fill()
beginFill = tk.Button(root,text="begin fill",command=begin)
beginFill.pack()

def end():
    t.end_fill()
endFill = tk.Button(root, text="end fill", command=end)
endFill.pack()
turtle.done()
turtle.mainloop()