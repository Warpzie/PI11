def sucet(x,y):
    return x + y
def parne(cislo):
    if cislo % 2 == 0 :
        return "parne"
    else:
        return "neparne"

def prvocislo(cislo):
    prvocis = True
    for i in range(2,cislo):
        if cislo % i == 0:
            prvocis = False
            return prvocis
    if prvocis == True:
        return " je prvocislo"
    else:
        return "nieje prvocislo"
a = int(input("zadaj a: "))
b = int(input("zadaj b: "))
sucet = sucet(a,b)
print(f"sucet cisel {a} + {b} = {sucet}")
print(f"cislo {a} je {parne(a)}")
print(f"cislo {b} je {parne(b)}")
if prvocislo(a):
    print(f"cislo {a} je prvocislo")
if prvocislo(b):
    print(f"cislo {b} je prvocislo")
