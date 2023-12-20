import tkinter, time, random
canvas = tkinter.Canvas()
canvas.pack()

stvorecA = canvas.create_rectangle(10,10,110,110, fill="red")
for i in range(1000):
    canvas.update()
    time.sleep(0.01)
    canvas.move(stvorecA,1,0)
    farba = random.choice(("red","green","orange","purple"))
    canvas.itemconfig(stvorecA, fill=farba)

canvas.mainloop()