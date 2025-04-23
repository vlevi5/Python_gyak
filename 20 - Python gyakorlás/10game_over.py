szoveg = input("Adjon meg egy szöveget: ") 
celszoveg = "game over"
kis_szoveg = szoveg.lower()

megvan = True

for karakter in celszoveg:
    if karakter not in kis_szoveg:
        megvan = False
        break

if megvan:
    for karakter in celszoveg:
        index = szoveg.find(karakter)

        if index == -1:
            index = szoveg.find(karakter.upper())
        
        print(szoveg[index], end="")
    print()
else: 
    hianyzo = [0]*9

    for karakter_index, karakter in enumerate(celszoveg):
        index = szoveg.find(karakter)

        if index == -1:
            index = szoveg.find(karakter.upper())
            hianyzo[karakter_index] += 1
            
    print("Hiányzó karakterek listája: ")  

    for karkter_index, karakter in enumerate(celszoveg):
        print(f"{karakter}: {hianyzo[karakter_index]}")