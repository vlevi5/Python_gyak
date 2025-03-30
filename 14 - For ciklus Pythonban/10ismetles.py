lista = [2, 2, 4, 2, 4, 3, 3, 3, 3, 2, 1]
min_haromszor = []

for elem in lista:
    if elem not in min_haromszor and lista.count(elem) >= 3:
        min_haromszor.append(elem)

print(f"Minimum háromszor szereplő számok: {min_haromszor}")
