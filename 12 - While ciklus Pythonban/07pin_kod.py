pinkod = 824
probalkozas = 0

while probalkozas < 5:
    tipp = int(input("\nTippelj egy PIN-kódot: "))
    probalkozas += 1

    if tipp == pinkod:
        print("Gratulálok, kitaláltad a PIN-kódot!")
        break
    else:
        print(f"Sajnos nem talált, próbáld újra! ({5-probalkozas} próbálkozásod van hátra)")
    
