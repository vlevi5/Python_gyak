binaris = [0, 1, 0, 0, 1, 0]

i = len(binaris)-1
szorzo = 1
tizes = 0

while i >= 0:
    tizes += (szorzo*binaris[i])
    szorzo *= 2
    i -= 1

print(f"Eredmény: {tizes}")

