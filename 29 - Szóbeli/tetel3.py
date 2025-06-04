szamok1 = [1, 2, 3, 4, 5, 6]
szamok2 = [10, 9, 5, 3]
metszet = []

for elem in szamok1:
    if elem in szamok2:
        metszet.append(elem)

print(metszet)