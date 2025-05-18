adatok = []

with open("jeladas.txt", "r", encoding="utf-8") as fajl:
    for sor in fajl:
        sor = sor.strip().split("\t")
        for index in range(1, 4):
            sor[index] = int(sor[index])
        adatok.append(sor)
print(adatok)

print("\n2. feladat:")
print(f"Az utolsó jeladás időpontja {adatok[-1][1]}:{adatok[-1][2]}, a jármű rendszáma: {adatok[-1][0]}")

print("\n3. feladat:")
keresett = adatok[0][0]
idopontok = []
for sor in adatok:
    if sor[0] == keresett:
        idopontok.append(f"{sor[1]}:{sor[2]}")
print(f"Az első jármű: {adatok[0][0]}")
print(f"Jeladásának időpontjai:", end=" ")
print(*idopontok, sep=" ")

print("\n4. feladat:")
ora = int(input("Kérem, adja meg az órát: "))
perc = int(input("Kérem, adja meg a percet: "))
szamlalo = 0
for sor in adatok:
    if sor[1] == ora and sor[2] == perc:
        szamlalo += 1
print(f"A jeladások száma: {szamlalo}")

print("\n5. feladat:")
leggyorsabb_rendszam = []
leggyorsabb = max(sor[-1] for sor in adatok)
for sor in adatok:
    if sor[-1] == leggyorsabb:
        leggyorsabb_rendszam.append(sor[0])
print(f"A legnagyobb sebesség km/h: {leggyorsabb}")
print(f"A járművek:", end=" ")
print(*leggyorsabb_rendszam, sep=" ")

print("\n6. feladat:")
keresett = input("Kérem, adja meg a rendszámot: ")
meresek = []
talalat = False
for sor in adatok:
    if sor[0] == keresett:
        meresek.append([sor[0], sor[1], sor[2], sor[3], 0])
        talalat = True

def ora(h, p):
    return h + (p/60)

if talalat: 
    for index in range(1, len(meresek)):
        t = ora(meresek[index][1], meresek[index][2]) - ora(meresek[index-1][1], meresek[index-1][2])
        v = meresek[index-1][3]
        s = v*t
        meresek[index][-1] = meresek[index-1][-1] + s
    #print(*meresek, sep="\n")
    for meres in meresek:
        print(f"{meres[1]}:{meres[2]} {meres[-1]:.1f} km")

else:
    print("Nincs ilyen rendszámú jármű az adatbázisban!")
    exit(0)

print("\n7. feladat:")
autok = {}
for sor in adatok:
    if sor[0] not in autok:
        autok[sor[0]] = []
    autok[sor[0]].append([sor[1], sor[2]])
#print(autok)    

with open("ido.txt","w", encoding="utf-8") as kiirt:
    for szgk, meresek in autok.items():
        print(szgk, meresek[0][0], meresek[0][1], meresek[-1][0], meresek[-1][1], file=kiirt)