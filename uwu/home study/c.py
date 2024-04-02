import tkinter as tk
import turtle
t = turtle.Turtle()
t.speed(0)
root = tk.Tk()
colors = ['blue', 'yellow']
def terc(pocet):
    for i in range(pocet):
        size = pocet*15-15*i
        color = colors[i%2]
        t.dot(size,color)
def zmenFarbu():
    newColorA= entryColorA.get()
    newColorB= entryColorB.get()
    colors=[newColorA,newColorB]
    terc(10)
labelColorA=tk.Label(root,text="farba 1")
labelColorA.pack()
entryColorA= tk.Entry(root)
entryColorA.pack()

labelColorB=tk.Label(root,text="farba 2")
labelColorB.pack()
entryColorB= tk.Entry(root)
entryColorB.pack()

prekresliB = tk.Button(root,text="prekresli",command=zmenFarbu)
prekresliB.pack()
print(colors)
turtle.done()
turtle.mainloop()