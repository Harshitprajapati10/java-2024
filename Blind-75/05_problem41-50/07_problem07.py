# problem 47
# rotate matrix clockwise

# LC: 48

"""
[1, 2, 3]     [7, 4, 1]
[4, 5, 6] --> [8, 5, 2]
[7, 8, 9]     [9, 6, 3]


    L          R
T   [5, 1, 9, 11]
    [2, 4, 8, 10]
    [13, 3, 6, 7]
B   [15,14,12,16]



        L          
    [15, 1, 9, 5]
T   [2, 4, 8, 10] R
    [13, 3, 6, 7]
    [16,14,12,11]
        B


            L          
    [15, 13,9, 5]
    [2 , 4, 8, 1] 
T   [12, 3, 6, 7] R
    [16,14,10,11]
            B


            L          
    [15, 13,2, 5]
    [14, 4, 8, 1] 
T   [12, 3, 6, 9] R
    [16,7,10, 11]
            B


            L          
    [15, 13,2, 5]
    [14, 3, 4, 1]  --> Ans
T   [12, 6, 8, 9] R
    [16,7,10, 11]
            B

l ++, R--
"""

def RotateImage(matrix):
    l, r = 0, len(matrix) - 1
    while l<r:
        for i in range(r-l):
            top, bottom = l, r

            topLeft = matrix[top][l + i] # save the topLeft
            matrix[top][l + i] = matrix[bottom - i][l] # move bottom left to top left
            matrix[bottom - i][l] = matrix[bottom][r - i] # move bottom right to bottom left
            matrix[bottom][r - i] = matrix[top + i][r] # move top right to bottom right
            matrix[top + i][r] = topLeft # move topleft to topRight
        r -= 1
        l += 1
    return matrix


matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(RotateImage(matrix1))

matrix2 = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15,14,12,16]
]
print(RotateImage(matrix2))