szoveg = input("Adjon meg egy szöveget: ")

if szoveg == szoveg[::-1]:
    print("A megadott szöveg egy palindróm!")
else:
    print("A megadott szöveg nem palindróm!")