import turtle

t = turtle.Turtle()
t.speed(0)
def stvorec(dlzka):
    for i in range(4):
        t.forward(dlzka)
        t.left(90)
# for j in range(4):
#     for i in range(1,11):
#         stvorec(10*i)
#     t.left(90)

def stvorce(a):
    b=10
    for i in range (a):
        stvorec(b)
        t.penup()
        t.right(90)
        t.fd(10)
        t.right(90)
        t.fd(10)
        t.right(180)
        t.pendown()
        b = b+20
stvorce(5)
turtle.mainloop()