a = int(input("Adja meg a négyszög 'A' oldalát: "))
b = int(input("Adja meg a négyszög 'B' oldalát: "))

if a == b:
    print(f"A négyzet területe {a**2}")
else:
    print(f"A téglalap területe {a*b}")
