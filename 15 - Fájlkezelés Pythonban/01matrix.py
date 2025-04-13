matrix = [
    ["Budapest", 10, 134412],
    ["Szeged", 2, 9723],
    ["Debrecen", 18, 86722],
    ["Balatonfüred", 5, 98302],
]

with open("feladat_3.txt", "w", encoding="utf-8") as fajl:
    for sor in matrix:
        for index, ertek in enumerate(sor):
            if index == 2:
                fajl.write(f"{ertek}\n")
            else:
                fajl.write(f"{ertek}\t")