import turtle
t = turtle.Turtle()
t.speed(0)

def obluk(d):
    for i in range (d):
        t.fd(5)
        t.rt(1.5)
        #for d = 50

def lupen():
        obluk(50)
        t.rt(105)
        obluk(50)
def kvet():
    for i in range(6):
        lupen()
        t.rt(45)
kvet()

turtle.mainloop()