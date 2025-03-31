szovegresz = "Süt a nap. A hőmérséklet 10 fok körül van."

print(szovegresz[0:16:2])
# Stanp  ő

print(szovegresz[::2])
# Stanp  őéske 0fkkrlvn

szovegresz = "Süt a nap. A hőmérséklet 10 fok körül van."

helyettesitett = szovegresz.replace("a", "\t").replace("e", "\t")
print(helyettesitett)

torolt_elem = szovegresz.split(" ").pop()
print(torolt_elem)

szoveg = input("Írjon be egy szöveget!\n > ")

if szoveg == szoveg[::-1]:
    print("A beírt szöveg egy palindróm!")
else:
    print("A beírt szöveg nem palindróm!")