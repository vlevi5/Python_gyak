halozat = [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1]

feszultsegmentes = 0

for elem in halozat:
    if elem == 0:
        feszultsegmentes += 1

print(f"\nÖsszesen {feszultsegmentes} percig volt feszültségmentes a hálózat.")

elozo_allapot = 0
leghosszabb = 0
leghosszabb_kezdet = 0
jelenlegi_hossz = 0
jelenlegi_kezdet = 0

for index, jelenlegi_allapot in enumerate(halozat):
    if elozo_allapot != jelenlegi_allapot:
        elozo_allapot = jelenlegi_allapot

        if jelenlegi_hossz > leghosszabb and jelenlegi_allapot == 1:
            leghosszabb = jelenlegi_hossz + 1
            leghosszabb_kezdet = jelenlegi_kezdet
        
        jelenlegi_kezdet = index
        jelenlegi_hossz = 0
    else:
        jelenlegi_hossz += 1

print(f"A leghosszabb kimaradás {leghosszabb} perc volt, és {leghosszabb_kezdet} perc után kezdődött")