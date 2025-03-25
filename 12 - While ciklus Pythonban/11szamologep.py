elso = 0
masodik = 0
fut = True

while fut:
    elso = int(input("Adja meg az első számot: "))
    masodik = int(input("Adja meg a második számot: "))

    muvelet_keres = True

    while muvelet_keres:
        muvelet = input("Adja meg a kívánt műveletet (+; -; *; /): ")

        if muvelet == "+":
            print(f"{elso} + {masodik} = {elso+masodik}")
            muvelet_keres = False
        elif muvelet == "-":
            print(f"{elso} - {masodik} = {elso-masodik}")
            muvelet_keres = False 
        elif muvelet == "*":
            print(f"{elso} * {masodik} = {elso*masodik}")
            muvelet_keres = False       
        elif muvelet == "/":
            print(f"{elso} / {masodik} = {elso/masodik}")
            muvelet_keres = False
        else:
            print("Nincsen ilyen művelet!")

    valasz = input("Szeretnél még egy műveletet elvégezni? (y/n): ")

    if valasz != "Y" and valasz != "y":
        fut = False
