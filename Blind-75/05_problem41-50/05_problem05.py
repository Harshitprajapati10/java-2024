# problem 45
# set rows and cols of matrix to zero
# LC 73


"""
[1, 1, 1]
[1, 0, 1]
[1, 1, 1]

[1, 0, 1]
[1, 0, 1]
[0, 1, 1]

  j  i->
  |  [0, 0, 1] var = 0
     [0, 0, 1]
     [0, 1, 1]
"""

def setMatrixToZero(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    first_row_zero = False
    first_col_zero = False
    for i in range(rows):
        if matrix[i][0] == 0:
            first_col_zero = True
            break
    for j in range(cols):
        if matrix[0][j] == 0:
            first_row_zero = True
            break
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    for i in range(1, rows):
        if matrix[i][0] == 0:
            for j in range(cols):
                matrix[i][j] = 0
    
    for j in range(1, cols):
        if matrix[0][j] == 0:
            for i in range(rows):
                matrix[i][j] = 0
    if first_row_zero:
        for j in range(cols):
            matrix[0][j] = 0
    if first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0
    
    return matrix

            
# O(3(n^2)) # space = O(1)

matrix = [
    [1, 0, 1],
    [1, 0, 1],
    [0, 1, 1]
]
print(setMatrixToZero(matrix))

matrix2 = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
]
print(setMatrixToZero(matrix2))