import turtle
import random
t = turtle.Turtle()
t.speed(0)
def stvorec(dlzka):
    for i in range(4):
        t.forward(dlzka)
        t.left(90)

def sachovnica(dlzka,farbaA,farbaB):
    for i in range (8):
        for j in range (8):
            t.fillcolor((farbaA))
            t.begin_fill()
            stvorec(dlzka)
            t.end_fill()
            t.fd(dlzka)
            farbaA, farbaB = farbaB, farbaA
        t.fd(-(dlzka*8))
        farbaA, farbaB = farbaB, farbaA
        t.right(90)
        t.penup()
        t.fd(dlzka)
        t.pendown()
        t.left(90)
sachovnica(10,"red","blue")

turtle.mainloop()