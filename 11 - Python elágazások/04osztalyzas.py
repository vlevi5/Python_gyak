maximalis = int(input("Adja meg a tesztre kapható maximális pontszámot: "))
elert = int(input("Adja meg az adott tesztre kapott pontszámot: "))
szazalek = round((elert/maximalis)*100, 2)

print(f"A dolgozat {szazalek}%-os")

if szazalek > 90:
    print ("5-ös")
elif 80 <= szazalek <= 89:
    print ("4-es")
elif 70 <= szazalek <= 79:
    print ("3-as")
elif 60 <= szazalek <= 69:
    print ("2-es")    
elif szazalek <= 59:
    print ("1-es")

