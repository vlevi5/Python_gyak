lista = [True, False, 10, "a", 5, "z"]

#Mit csinál az alábbi algoritmus?
#Mi a probléma az alábbi algoritmussal?

i = 0

while i < len(lista):
    lista.pop()
    i += 1

print(lista)

#Az algoritmus a lista utolsó elemét minden iterációban törli.
#A feltétel minden iterációban kiértékelődik, emiatt mindig újra meghatározzuk a lista aktuális hosszát, ami a törlések miatt mindig egyre rövidebb lesz. Emiatt az első 3 elem nem kerül törlésre a listából, mert kevesebbszer fut le a ciklus, mint amennyi az eredeti listánk elemszáma volt.
#Megoldás: ne módosítsuk azon listák hosszát a cikluson belül, amire a ciklus feltétele épül!