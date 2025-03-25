szam = int(input("Adjon meg egy tetszőleges számot: "))

''' 
if  szam % 15 == 0 and szam % 15 == 0:
    print("A szám 5-tel és 15-tel is osztható! ")
'''
if szam % 15 == 0:
    print("A szám osztható 15-tel.")
elif szam % 5 == 0:
    print("A szám osztható 5-tel.")
elif  szam % 15 != 0 and szam % 15 != 0:
    print("A szám sem 5-tel, sem 15-tel nem osztható! ")
    print(f"A szám öttel való osztásának maradéka: {szam%5}")