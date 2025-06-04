szamok = [12, 43, 21, 8, 74, 32, 19, 22]
legk_paratlan = None
index = -1

for elem in range(len(szamok)):
    if szamok[elem] % 2 == 0: 
        if legk_paratlan is None or szamok[elem] < legk_paratlan:
            legk_paratlan = szamok[elem]
            index = elem

if index != -1:
    print(f"A legkisebb páratlan szám: {legk_paratlan}")
    print(f"Első előfordulás indexe: {index}")
    
