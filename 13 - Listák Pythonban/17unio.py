lista1 = [1, 2, 2, 3, 4, 5]
lista2 = [6, 4, 1, 3, 4, 6, 6, 2, 0]

unio = list(set((lista1)+(lista2)))
unio.sort(reverse = True)

print(f"Unió: {unio}")