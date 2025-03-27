matrix = [
    [3, 5, 1, 4],
    [1, 2, 0, 9],
    [1, 0, 9, 4],
    [5, 7, 1, 4],
]

i = 0

while i < len(matrix):
    j = 0

    while j < i + 1:
        print(f"{matrix[i][j]},", end="")
        j += 1
    
    print()
    i += 1