fureszes = [
    ["a", "b", "c"],
    ["a"],
    ["a", "b"],
]

i = 0

while i < len(fureszes):
    j = 0

    while j < len(fureszes[i]):
        print(f"A(z) {i}. sor {j}. adata: {fureszes[i][j]}")
        j += 1
    
    i += 1