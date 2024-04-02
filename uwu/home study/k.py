import turtle,random
t = turtle.Turtle()
t.speed(0)
t.pu()

def stvorec(dlzka):
    t.fillcolor(f'#{random.randrange(256**3):06x}')
    t.begin_fill()
    for i in range(4):
        t.fd(dlzka)
        t.rt(90)
    t.end_fill()
def veza(dlzka,krok):
    size = dlzka
    while size>0:
        stvorec(dlzka)
        t.fd(dlzka%4)
        t.lt(90)
        size = dlzka - krok
        t.fd(size)
        t.rt(90)
        dlzka=size

veza(120,30)

turtle.mainloop()