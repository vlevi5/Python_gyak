szamok = [3, 4, -2, 5, -6]

osszeg = 0
for szam in szamok:
    if szam > 0:  # csak pozitívakat adunk össze
        osszeg += szam

print("Az összeg:", osszeg)
