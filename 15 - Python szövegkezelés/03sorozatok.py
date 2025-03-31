sorozatok = [
    "Az elit alakulat-9.5(2001)",
    "Totál szívás-9.4(2008)",
    "Csernobil-9.3(2019)",
    "Trónok Harca-9.2(2011)",
    "Peaky Blinders-8.8(2013)",
]

eredmeny = []

for sorozat in sorozatok:
    tores = sorozat.split("-")

    cim = tores[0]
    ertekeles = float(tores[1][0:3])
    evszam = int(tores[1][4:8])

    eredmeny.append([cim, ertekeles, evszam])

print(eredmeny)