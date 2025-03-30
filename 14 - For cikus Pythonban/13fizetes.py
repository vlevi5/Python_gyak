fizetesek = [15000, 30000, 20000, 17500]
alkalmazottak = ["Tóth Péter", "Kovács János", "Nagy Anna", "Vas Petra"]

for index, fizetes in enumerate(fizetesek):
    if fizetes < 20000:
        print(alkalmazottak[index])