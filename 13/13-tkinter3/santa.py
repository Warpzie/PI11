import tkinter, time, random

canvas_width = 300
canvas_height = 600
santaX = canvas_width//2
santaY = 66
santaPosun = 1
canvas = tkinter.Canvas(width=canvas_width,height=canvas_height)
canvas.pack()

image_santa = tkinter.PhotoImage(file="santa.png")
santa = canvas.create_image(santaX,santaY,image=image_santa)
while True:
    canvas.update()
    time.sleep(0.01)
    canvas.move(santa,0,santaPosun)
    santaY = santaY + santaPosun
    if santaY == canvas_height:
        canvas.delete(santa)
        santaY=60
        santa = canvas.create_image(santaX, santaY, image=image_santa)
