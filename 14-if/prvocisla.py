
#    for delitel in range(1, cislo + 1):
#        if cislo % delitel == 0:
#            x +=1
#        if x <= 2:
#            print(cislo,"je prvocislo")
#            x=0
#        cislo+=1
while True:
    n = int(input("zadaj n"))
    print("prvocisla",end=" ")
    for cislo in range(2,(n//2)+1):
        x=0
        for delitel in range(1,cislo +1):
            if cislo % delitel == 0:
                x+=1
        if x == 2:
            print(cislo,end=" ")
    if cislo==0:
        break