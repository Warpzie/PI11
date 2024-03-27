import tkinter

canvas = tkinter.Canvas()
canvas.pack()

xx= yy = None
def click(event):
    global xx,yy
    x,y = event.x, event.y
    canvas.create_oval(x-10,y-10,x+10,y+10)
    if xx != None:
        canvas.create_line(xx,yy,x,y)
    xx,yy=x,y

canvas.bind('<ButtonPress>', click)


tkinter.mainloop()
