def convert_to_row_echelon(matrix):
    rows, cols = len(matrix), len(matrix[0])

    # Perform row reduction
    for i in range(min(rows, cols)):
        # Find the pivot (the first non-zero element) in the current column
        pivot_row = i
        while pivot_row < rows and matrix[pivot_row][i] == 0:
            pivot_row += 1

        # If no pivot found, move to the next column
        if pivot_row == rows:
            continue

        # Swap rows to move the pivot to the current row
        matrix[i], matrix[pivot_row] = matrix[pivot_row], matrix[i]

        # Normalize the pivot row by dividing by the pivot element
        pivot_element = matrix[i][i]
        matrix[i] = [elem / pivot_element for elem in matrix[i]]

        # Eliminate non-zero entries below the pivot by performing row operations
        for j in range(i + 1, rows):
            multiplier = matrix[j][i]
            matrix[j] = [elem_j - multiplier * elem_i for elem_i, elem_j in zip(matrix[i], matrix[j])]

    return matrix

# Example usage:
matrix = [
    [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3]
]

result = convert_to_row_echelon(matrix)
for row in result:
    print(row)
