#while True:
#    cislo = int(input("zadaj cislo (pre ukoncenie zadaj 0)"))
#    if cislo == 0:
#        print("cislo je 0")
#        break
#    elif cislo % 2 == 0:
#        print("parne")
#    else:
#        print("neparne")
x=0
while True:
    cislo = int(input("zadaj cislo"))
    print("delitele:", end=" ")
    for delitel in range(1,cislo +1):
        if cislo % delitel == 0:
            print(delitel,end=" ")
            x+=1
    print()
    print("pocet delitelov = ", x)
    if x <= 2:
        print("je to prvocislo")
    x=0
    if cislo==0:
        break