mondat = input("Adjon meg egy mondatot: ") 
mondat_reszek = mondat.split(" ")

for index, mondat_resz in enumerate(mondat_reszek):
    mondat_reszek[index] = mondat_resz[::-1]

forditott = " ".join(mondat_reszek)

print(f"A mondat szavai fordítva: \n{forditott}")
