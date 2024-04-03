#Riešenie:1


import turtle
import tkinter

def dopredu():
    t.fd(50)

def vpravo():
    t.rt(90)

def vlavo():
    t.lt(18)

t = turtle.Turtle()
tkinter.Button(text='Dopredu', command=dopredu).pack(side='left')
tkinter.Button(text='Vpravo', command=vpravo).pack(side='left')
tkinter.Button(text='Vlavo', command=vlavo).pack(side='left')

t.pensize(3)
t.color('blue', 'red')

turtle.done()

#Riešenie:2

import turtle
import tkinter

def dopredu():
    t.fd(50)

def vpravo():
    t.rt(90)

def vlavo():
    t.lt(18)

def begin():
    t.begin_fill()

def end():
    t.end_fill()

t = turtle.Turtle()
tkinter.Button(text='Dopredu', command=dopredu).pack(side='left')
tkinter.Button(text='Vpravo', command=vpravo).pack(side='left')
tkinter.Button(text='Vlavo', command=vlavo).pack(side='left')
tkinter.Button(text='begin_fill', command=begin).pack(side='left')
tkinter.Button(text='end_fill', command=end).pack(side='left')

t.pensize(3)
t.color('blue', 'red')

turtle.done()

#Riešenie:3

import turtle
import tkinter
import random

def slnko(pocet, velkost):
    t.pencolor('gold')
    t.pensize(10)
    for i in range(pocet):
        t.fd(velkost)
        t.fd(-velkost)
        t.rt(360 / pocet)
    t.dot(velkost)

def nove_slnko():
    t.clear()
    slnko(random.randint(3, 20), random.randint(20, 100))

turtle.delay(0)
t = turtle.Turtle()
tkinter.Button(text='Nové slnko', command=nove_slnko).pack()
t.speed(0)
slnko(12, 100)

turtle.done()

#Riešenie:4

import turtle
import tkinter

def terc(n, farba1='blue', farba2='yellow'):
    for i in reversed(range(1, n + 1)):
        t.dot(i * 15, farba1)
        farba1, farba2 = farba2, farba1

def prekresli():
    t.clear()
    terc(20, farba1.get(), farba2.get())

turtle.delay(0)
t = turtle.Turtle()
farba1 = tkinter.Entry()
farba1.pack()
farba2 = tkinter.Entry()
farba2.pack()
tkinter.Button(text='Prekresli', command=prekresli).pack()

terc(20)

turtle.done()

#Riešenie:5

import turtle
import random
import tkinter

def strom(kmen, koruna):
    t.lt(90)
    t.pensize(15)
    t.pencolor('brown')
    t.fd(kmen)
    t.pensize(40)
    t.pencolor('green')
    t.fd(koruna)
    t.pu()
    t.bk(kmen+koruna)
    t.pd()
    t.rt(90)

def pridaj():
    strom(random.randint(30, 60), random.randint(10, 40))
    t.pu()
    t.fd(50)
    t.pd()

def uber():
    t.pu()
    t.fd(-50)
    t.pd()
    t.lt(90)
    t.pencolor('white')
    t.pensize(40)
    t.fd(100)
    t.fd(-100)
    t.rt(90)

turtle.delay(0)
t = turtle.Turtle()
tkinter.Button(text='Pridaj', command=pridaj).pack()
tkinter.Button(text='Uber', command=uber).pack()
t.speed(0)
t.pu()
t.setpos(-250, 0)
t.pd()
for i in range(8):
    pridaj()

turtle.done()

#Riešenie:6

import turtle
import tkinter

def spirala(d, krok, uhol):
    t.reset()
    t.speed(0)
    t.ht()
    for i in range(200):
        t.fd(d)
        t.rt(uhol)
        d += krok
        if t.distance(0, 0) > 250:
            return

def rob(uhol):
    spirala(5, 3, int(uhol))

turtle.delay(0)
t = turtle.Turtle()
tkinter.Scale(command=rob, orient='horizontal', from_=5, to=179, length=300).pack()

spirala(5, 3, 5)

turtle.done()

#Riešenie:7

import turtle

def kosostvorec(velkost, farba):
    t.fillcolor(farba)
    t.begin_fill()
    for i in range(2):
        t.fd(velkost)
        t.rt(45)
        t.fd(velkost)
        t.rt(135)
    t.end_fill()

turtle.delay(0)
t = turtle.Turtle()
for i in range(8):
    kosostvorec(100, ('tan', 'tomato')[i % 2])
    t.lt(45)

turtle.done()
#Riešenie:8

import turtle

def domcek(d):
    for i in range(4):
        t.fd(d)
        t.lt(90)
    t.lt(45)
    d2 = d * 2 ** 0.5
    t.fd(d2)
    t.lt(90)
    t.fd(d2/2)
    t.lt(90)
    t.fd(d2/2)
    t.lt(90)
    t.fd(d2)
    t.lt(45)

# to isté ale zapísané úspornejšie:

def domcek(d):
    d2 = d * 2 ** 0.5
    d1 = d2 / 2
    for a, b in (d, 90), (d, 90), (d, 90), (d, 135), (d2, 90), (d1, 90), (d1, 90), (d2, 45):
        t.fd(a)
        t.lt(b)

turtle.delay(0)
t = turtle.Turtle()

t.rt(5)
domcek(100)
domcek(50)
domcek(80)

turtle.done()

#Riešenie:9

import turtle

def polkruznica(velkost, smer):
    if smer:
        uhol = 10
    else:
        uhol = -10
    for i in range(18):
        t.fd(velkost)
        t.lt(uhol)

turtle.delay(0)
t = turtle.Turtle()

t.lt(90)
for i in range(10):
    polkruznica(3, i % 2)

turtle.done()

#Riešenie:10

import turtle
import random

def polkruh(velkost, smer):
    if smer:
        uhol = 10
    else:
        uhol = -10
    t.fillcolor(f'#{random.randrange(256**3):06x}')
    t.begin_fill()
    for i in range(18):
        t.fd(velkost)
        t.lt(uhol)
    t.end_fill()

turtle.delay(0)
t = turtle.Turtle()

t.lt(90)
for i in range(10):
    polkruh(3, i % 2)
for i in range(10):
    polkruh(3, i % 2 == 0)

turtle.done()

#Riešenie:11

import turtle
import random

def bodky(n, m):
    t.pencolor('salmon')
    t.pu()
    for i in range(n):
        for j in range(m):
            t.dot(random.randint(20, 35))
            t.fd(30)
        t.fd(-m * 30)
        t.lt(90)
        t.fd(30)
        t.rt(90)

turtle.delay(0)
t = turtle.Turtle()

bodky(10, 15)

turtle.done()

#Riešenie:12

import turtle
import random

def stvorec(dlzka):
    t.fillcolor(f'#{random.randrange(256**3):06x}')
    t.begin_fill()
    for i in range(4):
        t.fd(dlzka)
        t.rt(90)
    t.end_fill()

def stvorce(dlzka, krok):
    t.pu()
    while dlzka > 0:
        stvorec(dlzka)
        t.fd(krok / 2)
        t.rt(90)
        t.fd(krok / 2)
        t.lt(90)
        dlzka -= krok

turtle.delay(0)
t = turtle.Turtle()

stvorce(200, 25)

turtle.done()

#Riešenie:13

import turtle
import random

def stvorec(dlzka):
    t.fillcolor(f'#{random.randrange(256**3):06x}')
    t.begin_fill()
    for i in range(4):
        t.fd(dlzka)
        t.rt(90)
    t.end_fill()

def veza(dlzka, krok):
    t.pu()
    while dlzka > 0:
        stvorec(dlzka)
        dlzka -= krok
        t.fd(krok / 2)
        t.lt(90)
        t.fd(dlzka)
        t.rt(90)

turtle.delay(0)
t = turtle.Turtle()

veza(120, 30)

turtle.done()

#Riešenie:14

import turtle

def dom(d):
    for i in range(4):
        t.fd(d)
        t.rt(90)
    t.lt(60)
    t.fd(d)
    t.rt(120)
    t.fd(d)

def dom1(d):
    for i in range(4):
        prerusovana_ciara(d)
        t.rt(90)
    t.lt(60)
    prerusovana_ciara(d)
    t.rt(120)
    prerusovana_ciara(d)

def dom2(d):
    for i in range(4):
        cikcakova_ciara(d)
        t.rt(90)
    t.lt(60)
    cikcakova_ciara(d)
    t.rt(120)
    cikcakova_ciara(d)

def prerusovana_ciara(d):
    for i in range(11):
        if i % 2 == 0:
            t.pd()
        else:
            t.pu()
        t.fd(d / 11)

def cikcakova_ciara(d):
    for i in range(d // 5):
        t.lt(60)
        t.fd(5)
        t.rt(120)
        t.fd(5)
        t.lt(60)

turtle.delay(0)
t = turtle.Turtle()

#dom(100)
dom1(100)
t.pu()
t.lt(60)
t.fd(30)
t.pd()
dom2(100)

turtle.done()

#Riešenie:15

import turtle
import random
from math import sin, cos, radians

def stvorec(velkost):
    t.fillcolor(f'#{random.randrange(256**3):06x}')
    t.begin_fill()
    for i in range(4):
        t.fd(velkost)
        t.rt(90)
    t.end_fill()

def pytagoras(prepona, uhol):
    odvesna1 = prepona * cos(radians(uhol))
    odvesna2 = prepona * sin(radians(uhol))
    stvorec(prepona)
    t.lt(uhol + 90)
    stvorec(odvesna1)
    t.rt(90)
    t.fd(odvesna1)
    stvorec(odvesna2)
    print('stvorec nad preponou =', prepona ** 2)
    print('stvorec nad 1. odvesnou =', odvesna1 ** 2)
    print('stvorec nad 2. odvesnou =', odvesna2 ** 2)
    print('sucet =', odvesna1 ** 2 + odvesna2 ** 2)

turtle.delay(0)
t = turtle.Turtle()

pytagoras(150, 17)

turtle.done()

#Riešenie:16

import turtle
import random
from math import sin, radians

def troj(rameno, uhol):
    zakladna = 2 * rameno * sin(radians(uhol / 2))
    t.fillcolor(f'#{random.randrange(256**3):06x}')
    t.begin_fill()
    t.fd(rameno)
    t.rt(90 +  uhol / 2)
    t.fd(zakladna)
    t.rt(90 +  uhol / 2)
    t.fd(rameno)
    t.rt(180 - uhol)
    t.end_fill()

turtle.delay(0)
t = turtle.Turtle()

for i in range(36):
    troj(300, 10)
    t.rt(10)

turtle.done()

#Riešenie:17

import turtle
import math

def kruznica(r):
    d = math.pi * r / 18
    t.pu()
    t.fd(r)
    t.rt(90)
    t.fd(-d / 2)
    t.pd()
    for i in range(36):
        t.fd(d)
        t.rt(10)
    t.pu()
    t.fd(d / 2)
    t.lt(90)
    t.fd(-r)
    t.pd()

turtle.delay(0)
t = turtle.Turtle()

t.dot(200, 'yellow')
kruznica(100)
t.pu()
t.fd(120)
t.lt(90)
t.fd(100)
t.rt(37)
t.pd()
t.dot(140, 'gold')
kruznica(70)

turtle.done()

#Riešenie:18

import turtle
import random
import tkinter

def zvacsi():
    turtle.tracer(0)
    for t in zoz:
        t.clear()
        t.pensize(t.pensize() + 1)
        t.dot()
    turtle.tracer(0)

def zmensi():
    turtle.tracer(0)
    for t in zoz:
        t.clear()
        if t.pensize() > 0:
            t.pensize(t.pensize() - 1)
        t.dot()
    turtle.tracer(0)

turtle.delay(0)
zoz = []
n = 20
for i in range(n):
    t = turtle.Turtle()
    t.ht()
    t.pu()
    t.setpos(random.randint(-250, 250), random.randint(-250, 250))
    t.pencolor(f'#{random.randrange(256**3):06x}')
    t.pensize(random.randint(5, 40))
    zoz.append(t)

for t in zoz:
    t.dot()

tkinter.Button(text='Zväčši', command=zvacsi).pack()
tkinter.Button(text='Zmenši', command=zmensi).pack()

turtle.done()

#Riešenie:19

import turtle
import random

def vyrob(n, poz):
    zoz = []

    for i in range(n):
        t = turtle.Turtle()
        t.pu()
        t.setpos(random.randint(-300, 300), random.randint(-300, 300))
        t.pencolor(f'#{random.randrange(256**3):06x}')
        t.pensize(5)
        t.setheading(t.towards(poz))
        t.pd()
        zoz.append(t)
    return zoz

def smerom(zoznam, poz):
    for i in range(50):
        for t in zoznam:
            vzd = t.distance(poz)
            t.fd(vzd / 10)

turtle.delay(0)
t = turtle.Turtle()

pp = (0, -300)
zoz = vyrob(100, pp)
smerom(zoz, pp)

turtle.done()