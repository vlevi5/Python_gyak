def masodfoku_megoldo(a, b, c):
    diszkriminans = b*b-4*a*c
    negyzet = (abs(diszkriminans ** (1/2)))

    if diszkriminans > 0:
        x1 = (-b + negyzet)/(2*a)
        x2 = (-b - negyzet)/(2*a)
        return [x1, x2]
    
    if diszkriminans == 0:
        x1 = -b / (2*a)
        return [x1]
    
    return None

a = int(input("Paraméter 'a': "))
b = int(input("Paraméter 'b': "))
c = int(input("Paraméter 'c': "))

eredmeny = masodfoku_megoldo(a, b, c)

if eredmeny == None:
    print("Az egyenletnek nincs megoldása!")
else:
    print(f"Az egyenlet megoldásai: {eredmeny}")