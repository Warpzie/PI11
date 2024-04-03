import turtle

pocet = 5
turtles = []
for i in range(5):
    t = turtle.Turtle()
    t.penup()
    t.setpos(i*50,0)
    t.pendown()
    turtles.append(t)

for i in range (4):
    for t in turtles:
        t.forward(20)
        t.right(90)




turtle.mainloop()
