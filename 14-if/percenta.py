pocetBodov = int(input("zadaj pocet bodov:"))
maxBodov = 30
percenta = pocetBodov/maxBodov*100
print(f"ziskal si {percenta}%")
#if percenta >= 90:
#    print("vyborny")
#else:
#    if percenta >= 75:
#        print("chvalitebny")
#    else:
#        if percenta>=50:
#            print("dobry")
#        else:
#            if percenta>= 30:
#                print("nedostatocny")
#           else:
#                print("nedostatocny")

#if percenta >= 90:
#    print("vyborny")
#if 75<= percenta < 90:
#    print("chvalitebny")
#if 50<= percenta < 75:
#    print("dobry")
#if 30<= percenta < 50:
#    print("nedostatocny")
#    if percenta < 30:
#        print("nedostatocny")

if percenta > 90:
    print("vyborny")
elif percenta > 75:
    print("chvalitebny")
elif percenta > 50:
    print("dobry")
elif percenta > 30:
    print("nedostatocny")
else:
    print("nedostatocny")