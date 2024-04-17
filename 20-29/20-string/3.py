ret = input("zadaj retazec")
posun = int(input("zadaj posun pre kodovanie: "))
for i in range(len(ret)):
    print(ret[i],":",ord(ret[i]))
#    print(f'{ret[i]}:{chr(ord(ret[i])+1)}')

retKod = ""
for i in range(len(ret)):
    retKod += chr(ord(ret[i])+posun)
print(f'zakodovany retazec: {retKod}')


