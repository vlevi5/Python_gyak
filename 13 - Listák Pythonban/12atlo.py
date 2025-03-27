matrix = []
matrix.append([3, 5, 1, 4])
matrix.append([1, 2, 0, 9])
matrix.append([1, 0, 9, 4])
matrix.append([5, 7, 1, 4])

i = 0

while i < len(matrix):
    print(f"Az átló {i}. eleme: {matrix[i][i]}")
    i += 1