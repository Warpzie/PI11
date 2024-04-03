import tkinter
import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(3)
t.pencolor('blue')
t.fillcolor('red')

def dopredu():
    t.fd(50)

def vpravo():
    t.rt(90)

def vlavo():
    t.lt(18)
def begin():
    t.begin_fill()
def end():
    t.end_fill()
tkinter.Button(text="dopredu",command=dopredu).pack(side="left")
tkinter.Button(text="vpravo",command=vpravo).pack(side="left")
tkinter.Button(text="vlavo",command=vlavo).pack(side="left")
tkinter.Button(text="begin_fill",command=begin).pack(side="left")
tkinter.Button(text="end_fill",command=end).pack(side="left")
turtle.mainloop()
