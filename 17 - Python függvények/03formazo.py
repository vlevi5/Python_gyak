def formazo(osszeg, valuta, elvalaszto = " "):
    if osszeg < 1000:
        return f"{osszeg} {valuta}"

    forditott_osszeg = str(osszeg)[::-1]
    tagolt_osszeg = ""

    for index, karakter in enumerate(forditott_osszeg):
        if (index) % 3 == 0:
            tagolt_osszeg += elvalaszto + karakter
        else:
            tagolt_osszeg += karakter
    
    return tagolt_osszeg[::-1] + valuta

print(formazo(100, "Ft"))
print(formazo(10000, "Ft"))
print(formazo(1000000, "Ft"))