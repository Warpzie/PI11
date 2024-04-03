import tkinter

canvasWidth = 300
canvasHeight = 300

canvas = tkinter.Canvas(width=canvasWidth,height=canvasHeight)
canvas.pack()
n = int(input("zadaj sirku"))
xA = n
yA = 5
xB = 5
yB = n
pocet = canvasWidth//n
f1,f2 = "red", "blue"
for i in range (pocet):
    canvas.create_line(xA,yA,xA,canvasHeight,fill=f1)
    canvas.create_line(xB,yB,canvasWidth,yB,fill=f1)
    xA= xA+n
    yB = yB + n
    f1,f2=f2,f1
canvas.mainloop()