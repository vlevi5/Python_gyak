eladasok = [
    [1, "alma", 600],
    [2, "körte", 800],
    [3, "alma", 600],
    [4, "banán", 1000],
    [5, "körte", 800],
    [6, "körte", 800],
    [7, "körte", 800],
    [8, "alma", 600],
    [9, "banán", 1000],
    [10, "alma", 600],
]

termekek = []

for sor in eladasok:
    if sor[1] not in termekek:
        termekek.append(sor[1])
    
osszertekek = []

for termek in termekek:
    osszertekek.append(0)

    for sor in eladasok:
        if sor[1] == termek:
            osszertekek[-1] += sor[2]

print(termekek)
print(osszertekek)
print()

for termek, osszertek in zip(termekek, osszertekek):
    print(f"{termek} - {osszertek} Ft")