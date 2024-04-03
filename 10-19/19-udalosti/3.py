import tkinter
canvas = tkinter.Canvas()
canvas.pack()

list = []
def click(event):
    global line
    list[:] = [event.x, event.y]
    line = canvas.create_line(0,0,0,0)
def drag(event):
    list.extend([event.x,event.y])
    canvas.coords(line,list)


canvas.bind('<ButtonPress>',click)
canvas.bind('<B1-Motion>',drag)

tkinter.mainloop()