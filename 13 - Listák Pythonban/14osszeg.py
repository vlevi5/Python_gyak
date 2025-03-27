lista = [1.4, 2.6, 1.34, 9.6, 5.4]
i = 0
osszeg = 0

while i < len(lista):
    osszeg += lista[i]
    i += 1

print(f"A lista elemeinek összege: {osszeg}")