import tkinter, random

canvasWidth = 300
canvasHeight = 300

canvas = tkinter.Canvas(width=canvasWidth,height=canvasHeight)
canvas.pack()

polomer = 10
pocetKruhov = 300
okraj = 0
for i in range(pocetKruhov):
    x = random.randint(polomer+2,canvasWidth -polomer-2)
    y = random.randint(polomer+2,canvasHeight - polomer-2)
    if x <= canvasWidth//2 and y<=canvasHeight //2:
        farba = 'red'
    elif x >= canvasWidth//2 and y <= canvasHeight//2:
        farba = 'blue'
    elif x <= canvasWidth//2 and y>= canvasHeight//2:
        farba = 'yellow'
    else:
        farba = 'green'
    canvas.create_oval(x-polomer,y-polomer,x+polomer,y+polomer,fill=farba,width = okraj)

tkinter.mainloop()