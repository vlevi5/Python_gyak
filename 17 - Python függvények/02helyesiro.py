def nev(vezeteknev, keresztnev):
    return f"{vezeteknev.title()} {keresztnev.title()}"

knev = input("Adja meg a keresztnevét: ")
vnev = input("Adja meg a vezetéknevét: ")

print(nev(knev, vnev))