print("Kilépéshez írja be az 'x' karaktert!")
fut = True

while fut:
    szoveg = input("\nAdjon meg egy számot: ")

    if szoveg == "x":
        fut = False
        break
    else:
        szam = int(szoveg)

        if  szam %2 == 0:
            print("A szám páros!")
        else:
            print("A szám páratlan!")