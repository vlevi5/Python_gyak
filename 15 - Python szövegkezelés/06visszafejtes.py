abc = "AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ"
uzenet = input("Írja be a titkosított szöveget: ")
kulcs = int(input("Adja meg a kulcsot: "))
kimenet = ""

for betu in uzenet:
    nagybetu = betu.upper()

    if nagybetu in abc:
        j = abc.find(nagybetu)
        j -= kulcs

        if j < 0:
            j += len(abc)
        
        kimenet += abc[j].lower()
    else:                            # Amennyiben olyan karaktert látunk, ami nincs a karakterkészletben
        kimenet += betu.lower()

print("Visszafejtés: {0} → {1} ({2})".format(uzenet, kimenet, kulcs))