import tkinter
import random

canvas = tkinter.Canvas(width=600, height=500)
canvas.pack()
d = 100
x = 100
y = 100
canvas.create_rectangle(x,y ,x+d, y+d)
#canvas.create_line(x,y,x + (d//2) ,y -(d//2))
#canvas.create_line(x+d, y,x+(d//2),y - (d//2) )
canvas.create_polygon(x, y,x + (d//2), y - (d//2), x +d, y)
canvas.create_rectangle(x + (d//4), y + (d//4),x + 3*(d//4), y + 3*(d//4))
canvas.create_line(x + (d//2), y + (d//4),x + (d//2), y + 3*(d//4))
canvas.create_line(x + (d//4), y + (d//2), x + 3*(d//4), y + (d//2))
canvas.mainloop()
