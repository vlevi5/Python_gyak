halozat = [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1]

feszultsegmentes = 0

for elem in halozat:
    if elem == 0:
        feszultsegmentes += 1

print(f"\nÖsszesen {feszultsegmentes} percig volt feszültségmentes a hálózat.")