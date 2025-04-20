adatok = []

with open("20 - Python gyakorlás/feladat_5.txt", "r", encoding="utf-8") as fajl:
    for sorszam, sor in enumerate(fajl):
        if sorszam % 3 == 0:
            adatok.append([sor.strip()])
        elif sorszam %3 == 1 or sorszam %3 == 2:
            adatok[-1].append(int(sor.strip()))

#print(adatok)

eletkorok = []

for sor in adatok:
    eletkorok.append(sor[2]-sor[1])

#print(eletkorok)

legidosebb = eletkorok.index(max(eletkorok))

print(f"A legidősebb ember {adatok[legidosebb][0]}, {eletkorok[legidosebb]} éves.")
