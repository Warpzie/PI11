import tkinter, random

canvasWidth =300
canvasHeight = 300

canvas = tkinter.Canvas(width=canvasWidth,height=canvasHeight)
canvas.pack()

polomer = 10
vzdialenost = 3
x = polomer+vzdialenost
y = polomer+vzdialenost
xx = x
for i in range(canvasHeight//(polomer*2) - 2):
    for j in range(canvasWidth//(polomer*2)-2):
        if x >= canvasWidth//2 - polomer and x <= canvasWidth//2 + polomer or y > canvasHeight//2 - polomer and y <= canvasHeight//2 + polomer:
            farba = 'red'
        else:
            farba = 'white'
        canvas.create_oval(x- polomer,y-polomer,x+polomer,y+polomer,fill=farba)
        x = x+ 2*polomer + vzdialenost
    x = xx
    y = y+2*polomer + vzdialenost

tkinter.mainloop()