import tkinter, random
canvas = tkinter.Canvas(width=500,height=500)
canvas.pack()

meno = 'alex'
priezvisko = 'trunkvalter'
vek = 16
print("volam sa ",meno," ",priezvisko)
print(f"volam sa {meno} {priezvisko} a mam {vek:02x} rokov")
for i in range (200):
    polomer = 20
    #velkost = random.randint(10, 80)
    x = random.randint(2,480)
    y = random.randint(2,480)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    farba = f"#{r:02x}{g:02x}{b:02x}"
    canvas.create_oval(x-polomer, y-polomer, x + polomer, y + polomer, fill=farba)
canvas.mainloop()
