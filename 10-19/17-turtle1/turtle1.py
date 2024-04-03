import turtle
import random
t = turtle.Turtle()
t.speed(0)
def stvorec(dlzka):
    for i in range(4):
        t.forward(dlzka)
        t.left(90)

for i in range (100):
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    t.fillcolor(random.choice(("blue","red","yellow","orange","green")))
    t.begin_fill()
    stvorec(30)
    t.end_fill()
    t.penup()
    t.setpos(x,y)
    t.right(random.randint(0,360))
    t.pendown()

turtle.mainloop()