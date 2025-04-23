import random

def nyeremeny():
    random_szam = random.random()*100

    if random_szam < 0.1:
        return "Legendás tárgy"
    
    if random_szam >= 0.1 and random_szam < 5.1:
        return "Epikus tárgy"
    
    if random_szam >= 5.1 and random_szam < 25.1:
        return "Különleges tárgy"
    
    return "Normál tárgy"

print(nyeremeny())
print(nyeremeny())
print(nyeremeny())
