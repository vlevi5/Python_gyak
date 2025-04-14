def szamologep(szam1, szam2, muvelet):
    if muvelet == "+":
        return szam1 + szam2
    if muvelet == "-":
        return szam1 - szam2
    if muvelet == "*":
        return szam1 * szam2
    if muvelet == "/":
        return szam1 / szam2
    
eredmeny1 = szamologep(1, 2, "+")
eredmeny2 = szamologep(10, 5, "/")
eredmeny3 = szamologep(6, 4, "*")

print(eredmeny1, eredmeny2, eredmeny3, sep=" | ")