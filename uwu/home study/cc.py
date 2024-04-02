import turtle
from tkinter import *
from tkinter.colorchooser import askcolor

def terc(pocet):
    turtle.speed(0)
    colors = ['blue', 'yellow']
    for i in range(pocet):
        color = colors[i % 2]
        size = 15 + i * 15
        turtle.dot(size, color)
    turtle.done()

def zmenit_farby():
    nova_farba1 = entry_farba1.get()
    nova_farba2 = entry_farba2.get()
    colors = [nova_farba1, nova_farba2]
    turtle.clear()
    terc(10)  # Príklad s počtom bodiek 10 a novými farbami

# Vytvorenie GUI
root = Tk()
root.title("Terc s farbami")

label_farba1 = Label(root, text="Farba 1:")
label_farba1.pack()
entry_farba1 = Entry(root)
entry_farba1.pack()

label_farba2 = Label(root, text="Farba 2:")
label_farba2.pack()
entry_farba2 = Entry(root)
entry_farba2.pack()

button_prekresli = Button(root, text="Prekresli", command=zmenit_farby)
button_prekresli.pack()

terc(10)  # Príklad s počtom bodiek 10 a predvolenými farbami

root.mainloop()