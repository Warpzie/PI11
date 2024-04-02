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

# Function to turn turtle right by 90 degrees
def turn_right():
    t.right(90)

# Function to turn turtle left by 18 degrees
def turn_left():
    t.left(18)

# Create the main tkinter window
root = tk.Tk()

# Create buttons to control turtle movements
button_forward = tk.Button(root, text="Dopredu", command=move_forward)
button_forward.pack()

button_right = tk.Button(root, text="Vpravo", command=turn_right)
button_right.pack()

button_left = tk.Button(root, text="Vľavo", command=turn_left)
button_left.pack()

# Draw shapes based on button clicks
t.penup()
t.goto(-50, 50)
t.pendown()
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.right(90)
t.end_fill()

t.penup()
t.goto(50, -50)
t.pendown()
t.begin_fill()
for _ in range(4):
    t.forward(150)
    t.right(90)
t.end_fill()

t.penup()
t.goto(-25, -75)
t.pendown()
t.begin_fill()
for _ in range(5):
    t.forward(50)
    t.right(72)
t.end_fill()

t.penup()
t.goto(75, 25)
t.pendown()
t.begin_fill()
for _ in range(5):
    t.forward(50)
    t.right(72)
t.end_fill()

turtle.done()
root.mainloop()