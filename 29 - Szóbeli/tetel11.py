szamok1 = [1, 2, 2, 3, 4, 5]
szamok2 = [6, 4, 1, 3, 4, 6, 6, 2, 0]
unio = []

for szam in szamok1:
    if szam not in unio:
            unio.append(szam)

for szam in szamok2:
    if szam not in unio:
            unio.append(szam)   

print(f"Unió (ismétlések nélkül): {unio}")         