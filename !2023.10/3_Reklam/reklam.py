adatok = []

with open("3_Reklam/rendel.txt", "r", encoding="utf-8") as fajl:
    for sor in fajl:
        adatok.append(sor.strip().split(" "))

print("\n2. feladat:")
print(f"Rendelések száma: {len(adatok)}")

print("\n3. feladat:")  
nap = input("Kérem, adjon meg egy napot: ")
darab = 0
for sor in adatok:
    if sor[0] == nap:
        darab += 1
print(f"A rendelések száma az adott napon: {darab}")

print("\n4. feladat:")  
erintett = []
for sor in adatok:
    if sor[1] == "NR" and sor[0] not in erintett:
        erintett.append(sor[0])

if len(erintett) == 30:
    print("Minden nap volt rendelés a reklámban nem érintett városból.")
else:
    print(f"{30-len(erintett)} nap nem volt a reklámban nem érintett városból rendelés")

print("\n5. feladat:")  
max_db = "1"
max_nap = "1"
for sor in adatok:
    if sor[2] > max_db:
        max_db = sor[2]
        max_nap = sor[0]
print(f"A legnagyobb darabszám {max_db}, a rendelés napja: {max_nap}")

#print("\n6. feladat:")  
def osszes(varos, nap):
    osszeg = 0
    for sor in adatok:
        if int(sor[0]) == nap and sor[1] == varos:
            osszeg += int(sor[2])
    return osszeg

print("\n7. feladat:")  
pl = osszes("PL", 21)
tv = osszes("TV", 21)
nr = osszes("NR", 21)
print(f"A rendelt termékek darabszáma a 21. napon: PL: {pl} TV: {tv} NR: {nr}")

print("\n8. feladat:")  
print("Napok\t1..10\t11..20\t21..30")
tablazat = [            #mátrix
    ["PL", 0, 0, 0],
    ["TV", 0, 0, 0],
    ["NR", 0, 0, 0]
]

for sor in adatok:
    if 1 <= int(sor[0]) <= 10:
        if sor[1] == "PL":
            tablazat[0][1] += 1
        elif sor[1] == "TV":
            tablazat[1][1] += 1
        else:
            tablazat[2][1] += 1
    elif 11 <= int(sor[0]) <= 20:
        if sor[1] == "PL":
            tablazat[0][2] += 1
        elif sor[1] == "TV":
            tablazat[1][2] += 1
        else:
            tablazat[2][2] += 1
    else:
        if sor[1] == "PL":
            tablazat[0][3] += 1
        elif sor[1] == "TV":
            tablazat[1][3] += 1
        else:
            tablazat[2][3] += 1

with open("3_Reklam/kampany.txt", "w", encoding="utf-8") as kiirt:
    kiirt.write("Napok\t1..10\t11..20\t21..30\n")
    for sor in tablazat:            
        print(f"{sor[0]}\t{sor[1]}\t{sor[2]}\t{sor[3]}")
        kiirt.write(f"{sor[0]}\t{sor[1]}\t{sor[2]}\t{sor[3]}\n")          