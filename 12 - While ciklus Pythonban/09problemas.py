# Mi a probléma az alábbi kóddal?

i = 10

while i >= 0:
    i -= 1
    
    if i == 1:
        i = 10


# Végtelen ciklus → amikor az i eléri az 1-et akkor újra 10-re állítódik, így soha nem ér véget
# a while i >= 0: feltétel mindig igaz marad