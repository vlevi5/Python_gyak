# Minden érték előfordulásainak száma

lista = [1, 3, 4, 5, 6, 5, 2, 1, 3, 2, 1, 4]

ismetlodes_nelkul = []

for szam in lista:
    if szam not in ismetlodes_nelkul:
        ismetlodes_nelkul.append(szam)

elofordulasok_szama = []

for szam in ismetlodes_nelkul:
    elofordulasok_szama.append(0)

    for ertek in lista:
        if ertek == szam:
            elofordulasok_szama[-1] += 1

print(ismetlodes_nelkul)
print(elofordulasok_szama)
print()

for szam, darab in zip(ismetlodes_nelkul, elofordulasok_szama):
    print(f"Szám: {szam} - Darab: {darab}")


# - az első ciklus ismétlődés nélkül kiválogatja az értékeket egy külön listába
# - a második ciklus előtt létrehozunk egy üres listát, ebben fogjuk az elemszámokat tárolni
# - a második ciklus az ismétlődés nélküli értékeket járja be
# - minden iteráció elején egy új 0 értéket fűzünk a darabszámokat tároló listához
# - minden kiválasztott - ismétlődés nélküli - listaelem esetén végignézzük a teljes - ismétlődéseket tartalmazó listát,
# - és ha a két ciklus ciklusváltozója egyenlő, akkor növeljük a darabszámot