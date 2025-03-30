eszkoztarak = [
    [1, ["Kard", "Sisak", "Páncél", "Fejsze"]],
    [2, ["Fejsze", "Fa", "Cipő"]],
    [3, ["Kesztyű"]],
    [4, ["Kard", "Páncél", "Fejsze"]],
]

jatekosok = [
    [1, 94, "xGamer"],
    [2, 82, "-Fighter-"],
    [3, 35, "n00b"],
    [4, 68, "proPlayer"],
]

for index, player in enumerate(jatekosok):
    if player[1] > 80 and "Fejsze" in eszkoztarak[index][1]:
        print(player[2])