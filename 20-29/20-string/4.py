text = input("zadaj text")
samohlasky = 0
spoluhlasky = 0
for char in (text):
    if char in 'aeiouy':
        samohlasky+=1
    else:
        spoluhlasky+=1
print(f'pocet samohlasok v texte {text} je {samohlasky}')
print(f'pocet spoluhlasok v texte {text} je {spoluhlasky}')