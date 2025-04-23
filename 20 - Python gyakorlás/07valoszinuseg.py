import random

def nyeremeny():
    random_szam = random.random()*100

    if random_szam < 0.1:
        return "Legendás tárgy"
    
    if random_szam >= 0.1 and random_szam < 5.1:
        return "Epikus tárgy"
    
    if random_szam >= 5.1 and random_szam < 25.1:
        return "Különleges tárgy"
    
    return "Normál tárgy"

nyeremenyek = []

for _ in range(200):
    nyeremenyek.append(nyeremeny())

#print(nyeremenyek)  # ← Legenerált 200 tárgy kiírása

legendas_counter = 0
epikus_counter = 0
kulonleges_counter = 0
normal_counter = 0

for adott_nyeremeny in nyeremenyek:
    if adott_nyeremeny == "Legendás tárgy":
        legendas_counter += 1
    elif adott_nyeremeny == "Epikus tárgy":
        epikus_counter += 1
    elif adott_nyeremeny == "Különleges tárgy":
        kulonleges_counter += 1
    else:
        normal_counter += 1

print(f"Legendás tárgyak száma: {legendas_counter}\nEpikus tárgyak száma: {epikus_counter}\nKülönleges tárgyak száma: {kulonleges_counter}\nNormál tárgyak száma: {normal_counter}")

# --- Innentől kezdődik az új feladat ---
print("----------")
osszes_elem = 200

if legendas_counter > 0:
    print(f"Legendás tárgy: {round(legendas_counter/osszes_elem, 2)}%")

else:
    print(f"Legendás tárgy: -")

print(f"Epikus tárgy {round(epikus_counter/osszes_elem*100, 2)}%")
print(f"Különleges tárgy {round(kulonleges_counter/osszes_elem*100, 2)}%")
print(f"Normál tárgy {round(normal_counter/osszes_elem*100, 2)}%")
