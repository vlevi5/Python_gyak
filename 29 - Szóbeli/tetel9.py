import random
szamlalo = 0

for i in range(5):
    dobas = random.randint(1, 6)
    print(f" {i+1}. dobás: {dobas}")

    if dobas % 2 == 0:
        szamlalo += dobas
    else:
        szamlalo -= dobas

print(f"A számláló értéke: {szamlalo}")
