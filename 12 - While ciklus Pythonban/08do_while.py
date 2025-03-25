szam = int(input("Adjon meg egy tetszőleges számot 1 és 10 között: "))
negyzetreemelt = 0

if szam <= 10 and szam != 0:

    while True:
        print(szam)

        szam **= 2
        if szam > 100000:
            break
else:
    print("1 és 10 közötti számot adj meg! ")