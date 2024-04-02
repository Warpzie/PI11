import turtle
import tkinter as tk

# Define the turtle with specified attributes
t = turtle.Turtle()
t.pensize(3)
t.pencolor('blue')
t.fillcolor('red')

# Function to move turtle forward by 50 units
def move_forward():
    t.forward(50)

# Create the main tkinter window
root = tk.Tk()

# Create a button to move turtle forward
button_forward = tk.Button(root, text="Dopredu", command=move_forward)
button_forward.pack()

turtle.done()
root.mainloop()