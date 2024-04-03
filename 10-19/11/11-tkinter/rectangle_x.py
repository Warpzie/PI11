import tkinter
import random

canvas = tkinter.Canvas()
canvas.pack()

x = 10
y = 10
d = 20
farba = random.choice(("red", "green", "blue"))
farba2 = random.choice(("pink", "yellow", "orange"))

canvas.create_rectangle(x,y,x+d,y+d, fill=farba2)
canvas.create_rectangle(x + d, y + d, x + (2*d), y + (2*d), fill=farba)
canvas.create_rectangle(x+(2*d),y +(2*d), x + (3*d), y + (3*d), fill=farba2)
canvas.create_rectangle(x+(3*d),y +(3*d), x + (4*d), y + (4*d), fill=farba)
canvas.create_rectangle(x+(4*d),y +(4*d), x + (5*d), y + (5*d), fill=farba2)
canvas.create_rectangle(x+(4*d),y, x + (5*d), y +d, fill=farba2)
canvas.create_rectangle(x+(3*d),y +d, x + (4*d), y + (2*d), fill=farba)
canvas.create_rectangle(x+d, y +(3*d), x + (2*d), y + (4*d), fill=farba)
canvas.create_rectangle(x,y +(4*d), x + (1*d), y + (5*d), fill=farba2)

x = 6*d
farba3 = random.choice(("red", "green", "blue"))
farba4 =  random.choice(("pink", "yellow", "orange"))
canvas.create_rectangle(x,y,x+d,y+d, fill=farba4)
canvas.create_rectangle(x + d, y + d, x + (2*d), y + (2*d), fill=farba3)
canvas.create_rectangle(x+(2*d),y +(2*d), x + (3*d), y + (3*d), fill=farba4)
canvas.create_rectangle(x+(3*d),y +(3*d), x + (4*d), y + (4*d), fill=farba3)
canvas.create_rectangle(x+(4*d),y +(4*d), x + (5*d), y + (5*d), fill=farba4)
canvas.create_rectangle(x+(4*d),y, x + (5*d), y +d, fill=farba4)
canvas.create_rectangle(x+(3*d),y +d, x + (4*d), y + (2*d), fill=farba3)
canvas.create_rectangle(x+d, y +(3*d), x + (2*d), y + (4*d), fill=farba3)
canvas.create_rectangle(x,y +(4*d), x + (1*d), y + (5*d), fill=farba4)

canvas.mainloop()