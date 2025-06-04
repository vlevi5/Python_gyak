szoveg = "Az alma nem esett messze a fától."

szoveg = szoveg.lower()
elofordulasok = {}

for karakter in szoveg:
    if karakter in elofordulasok:
        elofordulasok[karakter] += 1
    else:
        elofordulasok[karakter] = 1

for karakter, darab in elofordulasok.items():
    print(f"'{karakter}' ---> {darab} alkalommal")