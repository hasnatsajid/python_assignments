# Transpose of a matrix
matrix = [[1,2,3], [4,5,6]]
transpose_matrix = []

# Using for loop
for row in range(0, len(matrix[0])):
    list = []
    for j in range(0, len(matrix)):
        list.append(matrix[j][row])
    transpose_matrix.append(list)
print(transpose_matrix)

# Using list comprehension
transpose_matrix = [[matrix[j][row] for j in range(0, len(matrix))] for row in range(0, len(matrix[0])) ]
print(transpose_matrix)

