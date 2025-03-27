szam = 0
lista = []
i = 0

while i < 5:
    szam = int(input("Adjon meg egy számot: "))
    lista.append(szam)
    i += 1

lista.sort()
print(f"A lista rendezve: {lista}")