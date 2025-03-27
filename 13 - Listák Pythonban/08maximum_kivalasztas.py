szamok = [12, 3, 93, 38, 234, 79, 68, 52, 91, 111, 312, 489, 32]
maximum = 0
i = 1

while i < len(szamok):
    if szamok[i] > szamok[maximum]:
        maximum = i

    i += 1

print(szamok[maximum])



#print(f"A lista legnagyobb értékű eleme: {max(szamok)}")   → jó megoldás, de ciklust kell alkalmazni