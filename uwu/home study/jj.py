import turtle
import random

def stvorce(dlzka, krok):
    turtle.speed(0)  # Nastavenie maximálnej rýchlosti kreslenia
    size = dlzka

    while size > 0:
        turtle.begin_fill()
        turtle.color(random.random(), random.random(), random.random())  # Náhodná farba
        for _ in range(4):
            turtle.forward(size)
            turtle.right(90)
        turtle.end_fill()
        turtle.fd(krok%2)
        turtle.rt(90)
        turtle.fd(krok%2)
        turtle.lt(90)
        size -= krok

    turtle.done()

# Použitie funkcie s veľkosťou štvorca 200 a krokom 20
stvorce(200, 20)