# Напишите функцию для транспонирования матрицы. Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]] 
def transpose_matrix(matrix):
    # Проверяем, что матрица не пуста
    if not matrix:
        return []

    # Извлекаем количество строк и столбцов
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Создаем новую матрицу с транспонированными размерами
    transposed_matrix = [[0] * num_rows for _ in range(num_cols)]

    # Заполняем транспонированную матрицу
    for i in range(num_rows):
        for j in range(num_cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix

# Пример использования функции
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = transpose_matrix(matrix)
for row in transposed:
    print(row)
