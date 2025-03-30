lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 4, 2, 0]
metszet = []

for elem in lista1:
    if elem in lista2:
        metszet.append(elem)

print(f"A két lista metszete: {metszet}")