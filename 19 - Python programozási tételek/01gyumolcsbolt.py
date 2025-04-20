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
    
eladasok_szama = []

for termek in termekek:
    eladasok_szama.append(0)

    for sor in eladasok:
        if sor[1] == termek:
            eladasok_szama[-1] += 1

print(termekek)
print(eladasok_szama)
print()

for termek, db in zip(termekek, eladasok_szama):
    print(f"{termek} - {db} db")