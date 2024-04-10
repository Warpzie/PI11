text = input("zadaj text")
for i in range(len(text)):
    print(i,text[i])
#i = len(text)
#text = text[::-1]

#for i in range(1,len(text) + 1):
#    print(-i,text[-i])

for i in range(-1,-len(text) - 1,-1):
    print (i,text[i])
