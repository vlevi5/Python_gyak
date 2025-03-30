szoveg = "aMyQojAqHRVELdAwpPcJOE"

tomb = [1]
i = 0

while i < 5:
    i += 1
    szam = round((tomb[i-1] + 12) /2)
    tomb.append(szam)

for i in tomb:
    print(szoveg[i], end="")