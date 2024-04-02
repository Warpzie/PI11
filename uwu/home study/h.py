import turtle,random
t = turtle.Turtle()
t.speed(0)
t.rt(90)
def polkruznica(velkost,smer,color):
    t.color(color)
    t.begin_fill()
    if smer == True:
        for i in range(18):
            t.fd(velkost)
            t.lt(360 / 36)
    if smer == False:
        for i in range(18):
            t.fd(velkost)
            t.rt(360 / 36)
    t.end_fill()
direction2, direction1 = True, False
for i in range (2):
    for i in range (5):
        polkruznica(3,direction1,f'#{random.randrange(256**3):06x}')
        polkruznica(3,direction2,f'#{random.randrange(256**3):06x}')
    direction1, direction2 = True, False



turtle.mainloop()