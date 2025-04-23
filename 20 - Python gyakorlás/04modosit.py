index = 0
szuletesi_evek = []
adatok = []

with open("20 - Python gyakorlás/feladat_5.txt", "r", encoding="utf-8") as fajl:
    for sorszam, sor in enumerate(fajl):
        if sorszam % 3 == 0:
            adatok.append([sor.strip()])
        elif sorszam %3 == 1 or sorszam %3 == 2:
            adatok[-1].append(int(sor.strip()))

    for index, sor in enumerate(adatok):
        if sor[1] not in szuletesi_evek:
            szuletesi_evek.append(sor[1])
        else:
            break
#print(adatok)

eletkorok = []

for sor in adatok:
    eletkorok.append(sor[2]-sor[1])

with open("20 - Python gyakorlás/feladat_6.txt", "w", encoding="utf-8") as kiirt_fajl:
    for index, sor in enumerate(adatok):
        kiirt_fajl_sor = f"{sor[0]}, {sor[1]}, {sor[2]}, {eletkorok[index]}\n"

        kiirt_fajl.write(kiirt_fajl_sor)