import tkinter
x,y = 200,200
list = [x,y]
def draw(dx,dy):
    global x,y
    x+=dx
    y+= dy
    list.extend((x,y))
    canvas.coords(line,list)
def event_left(event):
    draw(-10,0)
def event_right(event):
    draw(10,0)
def event_up(event):
    draw(0,-10)
def event_down(event):
    draw(0,10)

canvas = tkinter.Canvas()
canvas.pack()

line = canvas.create_line(0,0,0,0)
canvas.bind_all('<Left>',event_left)
canvas.bind_all('<Right>',event_right)
canvas.bind_all('<Up>',event_up)
canvas.bind_all('<Down>',event_down)

tkinter.mainloop()
