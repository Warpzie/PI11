import turtle


t1=turtle.Turtle()
t1.speed(0)
t2=turtle.Turtle()
t2.speed(0)
t3=turtle.Turtle()
t3.speed(0)

t1.penup()
t1.setpos(-100,0)
t1.pendown()

t2.penup()
t2.setpos(100,0)
t2.pendown()

t3.penup()
t3.setpos(0,100)
t3.pendown()

def stvorec1(dlzka):
    for i in range(4):
        t1.forward(dlzka)
        t1.left(90)

for i in range(20):
    stvorec1(100)
    t1.left((360/20))

def stvorec2(dlzka):
    for i in range(4):
        t2.forward(dlzka)
        t2.left(90)

for i in range(20):
    stvorec2(100)
    t2.left((360/20))

def stvorec3(dlzka):
    for i in range(4):
        t3.forward(dlzka)
        t3.left(90)

for i in range(20):
    stvorec3(100)
    t3.left((360/20))


turtle.mainloop()