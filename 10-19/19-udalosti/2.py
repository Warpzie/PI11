import tkinter

def click(event):
    x,y = event.x, event.y
    canvas.create_oval(x-10,y-10,x+10,y+10, fill= 'blue')
def drag(event):
    x, y = event.x, event.y
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='red')

canvas = tkinter.Canvas()
canvas.pack()
canvas.bind('<ButtonPress>',click)
canvas.bind('<B1-Motion>', drag)      # '<Motion>' namiesto '<ButtonPress>'

tkinter.mainloop()