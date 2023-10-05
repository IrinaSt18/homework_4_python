# Напишите функцию для транспонирования матрицы. Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]] 

def transpose_matrix(matrix):
    if not matrix:
        return []
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    transposed_matrix = [[0] * num_rows for _ in range(num_cols)]

    for i in range(num_rows):
        for j in range(num_cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix

matrix = [[1, 2, 3], [4, 5, 6]]
transposed = transpose_matrix(matrix)
for row in transposed:
    print(row)
