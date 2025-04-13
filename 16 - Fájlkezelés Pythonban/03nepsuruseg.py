matrix = [
    [100, 1230000],
    [245, 152000],
    [1000, 300],
    [155, 3895000],
]

with open("feladat_4.txt", "w", encoding="utf-8") as fajl:
    for sor in matrix:
        fajl.write(f"{round(sor[1] / sor[0], 2)} fő / km^2\n")