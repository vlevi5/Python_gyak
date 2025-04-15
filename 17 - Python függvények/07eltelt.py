def visszaalakito(masodpercek):
    return f"{round((masodpercek//60)//60)}:{round(masodpercek//60) % 60}:{masodpercek % 60}" # ← előző feladatból

def kulonbseg(ora1, perc1, mp1, ora2, perc2, mp2):
    return abs(3600 * (ora1-ora2) + 60 * (perc2-perc1) + (mp2 - mp1))

print(f"{visszaalakito(kulonbseg(16, 0, 20, 18, 0, 0))} eltérés van a két időpont között.")