import turtle,random
t = turtle.Turtle()
t.speed(0)

def bodky(n,m):
    for i in range(n):
        for j in range(m):
            t.pd()
            t.dot(random.randrange(20,35),'salmon')
            t.pu()
            t.fd(30)
        t.pu()
        t.rt(180)
        t.fd(m*30)
        t.lt(90)
        t.fd(30)
        t.lt(90)
        t.pd()
bodky(13,15)


turtle.mainloop()