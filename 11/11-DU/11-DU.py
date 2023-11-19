import tkinter

canvas = tkinter.Canvas(width=580, height=500)
canvas.pack()

x = 10
y = 10
d = 20
#A
canvas.create_rectangle (x, y+d, x+d, y + (7*d), fill= "black")
canvas.create_rectangle(x+d, y, x + (4*d), y +d,fill="black")
canvas.create_rectangle(x+ (4*d), y+d, x+(5*d), y + (7*d), fill="black")
canvas.create_rectangle(x+d, y+(3*d), x + (4*d), y + (4*d), fill ="black")
#L
x = x+(6*d)
canvas.create_rectangle(x,y,x+d,y+(7*d),fill="black")
canvas.create_rectangle(x+d,y+(6*d),x+(4*d),y+(7*d),fill="black")
#E
x = x+(5*d)
canvas.create_rectangle(x,y,x+(5*d),y+d,fill="black")
canvas.create_rectangle(x,y+d, x+d,y+(7*d),fill="black")
canvas.create_rectangle(x+d,y+(3*d),x+(4*d),y+(4*d),fill="black")
canvas.create_rectangle(x+d,y+(7*d),x+(5*d),y+(6*d),fill="black")
#X
x= x+(6*d)
canvas.create_rectangle(x,y,x+d,y+(d*2),fill="black")
canvas.create_rectangle(x+d,y+(d*2),x+(2*d),y+(3*d),fill="black")
canvas.create_rectangle(x+(2*d),y+(3*d),x+(3*d),y+(4*d),fill="black")
canvas.create_rectangle(x+d, y+(4*d),x+(2*d),y+(5*d),fill="black")
canvas.create_rectangle(x,y+(5*d),x+d,y+(7*d),fill="black")
canvas.create_rectangle(x+(4*d),y,x+(5*d),y+(2*d),fill="black")
canvas.create_rectangle(x + (3*d), y+(2*d),x+(4*d),y+(3*d),fill="black")
canvas.create_rectangle(x+(3*d), y + (4*d),x+(4*d), y + (5*d),fill="black")
canvas.create_rectangle(x+(4*d), y+(5*d),x+(5*d),y +(7*d),fill="black")
#T
x = x+(6*d)
canvas.create_rectangle(x,y,x+(5*d),y+d,fill="black")
canvas.create_rectangle(x+(2*d),y+d, x+(3*d),y+(7*d),fill="black")

canvas.mainloop()