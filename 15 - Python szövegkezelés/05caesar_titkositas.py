abc = "AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ"
uzenet = input("Írja be a titkosítani kívánt szöveget: ")
kulcs = int(input("Adja meg a kulcsot: "))
kimenet = ""

for betu in uzenet:
    nagybetu = betu.upper()

    if nagybetu in abc:
        j = abc.find(nagybetu)
        j += kulcs
    
        if j > len(abc):        # Amennyiben az utolsó karaktert kellene eltolnunk
            j -= len(abc)

        kimenet += abc[j].lower()
    else:                       # Amennyiben olyan karaktert látunk, ami nincs a karakterkészletben
        kimenet += betu.lower()

print("{0} → {1} ({2})".format(uzenet, kimenet, kulcs))