matrix = []

with open("feladat_3.txt", "r", encoding="utf-8") as fajl:
    for sor in fajl:
        nev, szam1, szam2 = sor.strip().split("\t")
        matrix.append([nev, int(szam1), int(szam2)])

print(matrix)
