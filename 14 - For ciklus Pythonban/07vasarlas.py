processzorok = [
    ["Core i7-4771"  , 2 , 10000],
    ["Core i7-4790"  , 2 , 11900],
    ["Core i7-4790K" , 2 , 12700],
    ["Core i7-4770S" , 2 , 15600],
    ["Core i7-4790S" , 2 , 18000],
    ["Core i7-4765T" , 2 , 17000],
    ["Core i7-4770T" , 4 , 20500],
    ["Core i7-4785T" , 2 , 19700],
    ["Core i7-4790T" , 2 , 28000],
    ["Core i7-4770T" , 4 , 25000],
    ["Core i7-4770R" , 4 , 30000],
    ["Core i7-5820K" , 4 , 21000],
    ["Core i7-5930K" , 4 , 25000],
    ["Core i7-5960X" , 4 , 27000],
    ["Core i7-5775C" , 2 , 22000],
    ["Core i7-5775R" , 2 , 23000],
    ["Core i7-6800K" , 4 , 31000],
    ["Core i7-6950X" , 4 , 30000],
    ["Core i7-6700"  , 4 , 29000],
    ["Core i7-6700K" , 4 , 32900],
    ["Core i7-7800X" , 6 , 33000],
    ["Core i7-7820X" , 6 , 35000],
    ["Core i7-9800X" , 4 , 37000],
    ["Core i7-7700"  , 6 , 40000],
    ["Core i7-7700K" , 8 , 50000],
    ["Core i7-8086K" , 8 , 55000],
    ["Core i7-8700"  , 6 , 39000],
    ["Core i7-8700K" , 8 , 65000],
    ["Core i7-9700"  , 10, 50000],
    ["Core i7-9700F" , 6 , 45000],
    ["Core i7-9700K" , 6 , 75000],
    ["Core i7-9700KF", 8 , 78000],
]

megfelelo = []

minimum = int(input("Mennyi a MINIMUM ár amennyit a processzorra szeretne szánni? "))
maximum = int(input("Mennyi a MAXIMUM ár amennyit a processzorra szeretne szánni? "))

for elem in processzorok:
    if (elem[2] >= minimum) and (elem[2] <= maximum):
        megfelelo.append(elem)

print(f"Az árban Önnek mefelelő processzorok:")     

for elem in megfelelo:
    print(elem[0], end=", ")
