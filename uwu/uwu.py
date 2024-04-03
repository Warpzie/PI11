import turtle
from tkinter import *

# create a tkinter window
root = Tk()

# Open window having dimension 100x100
root.geometry('100x100')

# Create a Button
btn = Button(root, text='Click me !', bd='5',
             command=root.destroy)

root.mainloop()