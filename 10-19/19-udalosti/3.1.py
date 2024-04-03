import random
import tkinter
canvas = tkinter.Canvas()
canvas.pack()

list = []
def click(event):
    global poly
    list[:] = [event.x, event.y]
    farba = f'#{random.randrange(256**3):06x}'
    poly = canvas.create_polygon(0,0,0,0,fill = farba)
def drag(event):
    list.extend([event.x,event.y])
    canvas.coords(poly, list)


canvas.bind('<ButtonPress>',click)
canvas.bind('<B1-Motion>',drag)

tkinter.mainloop()