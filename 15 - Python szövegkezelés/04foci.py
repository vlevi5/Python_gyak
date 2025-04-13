jatekosok = [
    "Lionel Messi-ST",
    "Cristiano Ronaldo-ST",
    "Gianluigi Buffon-GK",
    "Sergio Ramos-CB",
    "Ngolo Kanté-CM",
    "Raheem Sterling-ST",
    "Gerard Pique-CB",
    "David de Gea-GK",
]

i = 0
tamadok = 0
vedok = 0
kozeppalyasok = 0
kapusok = 0

for jatekos in jatekosok:
    if jatekos[-2:] == "ST":
        tamadok += 1
    elif jatekos[-2:] == "CB":
        vedok += 1
    elif jatekos[-2:] == "GK":
        kapusok += 1
    elif jatekos[-2:] == "CM":
        kozeppalyasok += 1

print(f"Támadók: {tamadok}\nVédők: {vedok}\nKapusok: {kapusok}\nKözéppályások: {kozeppalyasok}")