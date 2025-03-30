lista1 = [1, 2, 2, 3, 4, 5]
lista2 = [6, 4, 1, 3, 4, 6, 6, 2, 0]
unio = []

for elem in lista1 + lista2:
    if elem not in unio:
        unio.append(elem)

unio.sort(reverse = True)        

print(f"A két lista uniója csökkenő sorrendben: {unio}")