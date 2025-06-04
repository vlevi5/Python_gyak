#Írj egy algoritmust, ami összegzi a 10, vagy annál nagyobb értékeket a szamok listában! Írd ki az eredményt.

szamok = [5, 12, 7, 14, 9, 10, 3]
osszeg = 0
counter = 0

for elem in szamok:
    if elem >= 10:
        osszeg += elem
        counter += 1

print(f"A 10-nél nagyobb számok összege: {osszeg}")


# Hogyan tudnád módosítani a megírt algoritmusodat, hogy az ne csak az összeget, hanem az összegzett elemek darabszámát is megjelenítse az algoritmus eredményeképp?
print(f"Az összegzett elemek darabszáma: {counter}")