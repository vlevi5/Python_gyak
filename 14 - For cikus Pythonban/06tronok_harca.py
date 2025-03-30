got = [
    ["Tyrion Lannister", "Lannister-ház"],
    ["Jaime Lannister", "Lannister-ház"],
    ["Daenerys Targaryen", "Targaryen-ház"],
    ["Margaery Tyrell", "Tyrell-ház"],
    ["Havas Jon", "Stark-ház"],
    ["Stannis Baratheon", "Baratheon-ház"],
    ["Bran Stark", "Stark-ház"],
    ["Sansa Stark", "Stark-ház"],
    ["Sansa Stark", "Stark-ház"],
    ["Ramsay Bolton", "Bolton-ház"],
    ["Theon Greyjoy", "Greyjoy-ház"],
]

hazak = []

for elem in got:
    if elem[1] not in hazak:
        hazak.append(elem[1])

print(hazak)        