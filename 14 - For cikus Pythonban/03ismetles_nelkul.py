lista = [1, 4, 2, 1, 3, 2, 4]

ismetlodes_nelkul = []

for elem in lista:
    if not(elem in ismetlodes_nelkul):
        ismetlodes_nelkul.append(elem)

print(f"A lista ismétlődések nélkül: {ismetlodes_nelkul}")