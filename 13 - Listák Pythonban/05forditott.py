lista = [True, False, 10, "a", 5, "z"]
i = len(lista) - 1

while i >= 0:
    print(f"A lista {i}. eleme: {lista[i]}")
    i -= 1


#print(lista[::-1])     → jó megoldás, de ciklust kell alkalmazni