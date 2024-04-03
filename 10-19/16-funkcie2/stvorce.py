import tkinter
canvas = tkinter.Canvas()
canvas.pack()

def rgb(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'
def stvorec(riadky,x,y, pocet,dlzka,r=255,g=255,b=255):
    for j in range(riadky):
        for i in range(pocet):
            krok = 255//pocet
            canvas.create_rectangle(x, y, x+dlzka, y+dlzka, fill=rgb(r,g,b))
            x+= dlzka
            if r>krok:
                r-= krok
            if g>krok:
                g-=krok
            if b>krok:
                b-=krok

stvorec(20,20,20,20,0,0,255)
canvas.mainloop()