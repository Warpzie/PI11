import tkinter
import random

canvas = tkinter.Canvas(width=600, height=500)
canvas.pack()

x = 3
xx = x
y = 10
d = 30
pocetA = 598//d # // je celociselne delenie
pocetB = 498//d
for i in range (pocetB):
    for j in range (pocetA):
        farba = random.choice(("red", "purple", "pink", "orange"))
        canvas.create_rectangle(x, y, x + d, y + d, fill=farba)
        canvas.create_line(x, y, x + d, y + d)
        canvas.create_line(x, y + d, x + d, y)
        x = x+d
    y=y+d
    x = xx

canvas.mainloop()
