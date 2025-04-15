def visszaalakito(masodpercek):
    return f"{round((masodpercek//60)//60)}:{round(masodpercek//60) % 60}:{masodpercek % 60}"

masodperc = 32312

print(f"{masodperc} másodperc = {visszaalakito(masodperc)}")
