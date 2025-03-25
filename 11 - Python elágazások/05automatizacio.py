nap = input("\nAdja meg milyen nap van ma! (h, k, sz, cs, p, szo, v): ").lower()
ora = int(input("Adja meg hány óra van! (0-23): "))

homerseklet = None

if nap in ("h", "k", "sz", "cs", "p", "szo", "v"):
    if 0 <= ora < 6 or 22 <= ora < 24:
        homerseklet = 20.5
    elif 6 <= ora < 9:
        homerseklet = 22.0 if nap in ("h", "k", "sz", "cs", "p") else 21.0
    elif 9 <= ora < 12:
        homerseklet = 19.0 if nap in ("h", "k", "sz", "cs", "p") else 22.0
    elif 12 <= ora < 16:
        if nap in ("h", "k", "sz", "cs"):
            homerseklet = 19.0
        elif nap == "p":
            homerseklet = 21.0
        else:
            homerseklet = 22.0
    elif 16 <= ora < 22:
        homerseklet = 22.0
else:
    print("Hibás napot adott meg!")

if homerseklet is not None:
    print(f"-------------------------------------------------")
    print(f"A beállított hőmérséklet {homerseklet}°C.")
