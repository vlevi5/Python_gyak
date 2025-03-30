matrix = [
    [2.4, 8.6, 5.7],
    [1.1, 5.3, 5.1],
    [9.7, 6.9, 8.4],
]

elemszam = 0
osszeg = 0

for sor in matrix:
    for elem in sor:
        osszeg += elem
        elemszam += 1

atlag = (osszeg/elemszam)

print(f"A mátrix elemeinek átlaga: {atlag}")