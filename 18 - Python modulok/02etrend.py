import random

gyumolcsok = []

while True:
    print("Amennyiben végzett, írja be az 'x' karaktert!")
    gyumolcs = input("Adja meg a gyümölcs nevét: ")

    if gyumolcs == "x" or gyumolcs == "X":
        break

    gyumolcsok.append(gyumolcs)

het_napjai = ["hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap"]

for nap in het_napjai:
    napi_gyumolcs = random.choice(gyumolcsok)

    print(f"{nap} - {napi_gyumolcs}")