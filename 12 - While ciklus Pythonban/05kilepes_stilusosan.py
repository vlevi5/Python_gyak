print("Kilépéshez írja be az 'x' karaktert!")
fut = True

while fut:
    szam = input("\nAdjon meg egy számot: ")

    if szam != "x":
        eredmeny = int(szam)*2
        print(f"{szam} * 2 = {eredmeny}")
    
    else:
        print("\n---Program vége---")
        fut = False