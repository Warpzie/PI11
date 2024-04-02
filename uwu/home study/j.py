import turtle,random
t = turtle.Turtle()
t.speed(0)
t.pu()

def stvorce(dlzka,krok):
    for i in range(5):
        stvorec(dlzka - (dlzka*i))
        t.fd(krok)
        t.rt(90)
        t.fd(krok)
        t.lt(90)


def stvorec(dlzka):
    t.fillcolor(f'#{random.randrange(256**3):06x}')
    t.begin_fill()
    for i in range(4):
        t.fd(dlzka)
        t.rt(90)
    t.end_fill()
stvorce(200,25)
turtle.mainloop()