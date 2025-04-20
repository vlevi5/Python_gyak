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
    
if index < len(adatok):
    print("Van legalább két olyan személy, aki ugyanabban az évben született!")
else:
    print("Nincs két olyan személy, aki ugyanabban az évben született!")