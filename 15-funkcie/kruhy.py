import tkinter
canvas = tkinter.Canvas()
canvas.pack()

def kruh(x, y, r,farba):
    canvas.create_oval(x-r,y-r,x+r,y+r,fill=farba)

#kruh(100,100,50,"red") #x stredu,y stredu, polomer

def kruhyRiadok(x,y,pocet,polomer,farba):
    for i in range(pocet):
        kruh(x,y,polomer,farba)
        x = x+ polomer*2

#kruhyRiadok(50,50,10,10,"red")

def kruhyFull(x,y,pocet,polomer,farba):
    for i in range(pocet):
        kruhyRiadok(x,y, pocet,polomer,farba)
        y = y+polomer*2
kruhyFull(50,50,10,10,"red")
canvas.mainloop()