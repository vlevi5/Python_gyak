import random

while True:
    while True:
        tipp = int(input("\r\nTippeljen, mit dob a dobókocka: "))

        if tipp >= 1 and tipp <=6:
            break
    
    dobas = random.randint(1,6)
    print(f"A dobás eredménye: {dobas}\r\n")
    if dobas == tipp:
        print("Eltalálta a dobott számot! Ön nyert!")
    else:
        print("Sajnos nem találta el a dobott számot!")
    
    uj_kor = input("Szeretne még egy kört játszani? (i/n): ")

    if uj_kor != "i" and uj_kor != "I":
        break