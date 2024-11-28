# Problem 46
# spiral order matrix

# LC 54

"""
[1, 2, 3, 4]
[5, 6, 7 ,8]  --> [1,2,3,4,8,12,11,10,9,5,6,7]
[9,10,11,12]

    L         R
  T [1, 2, 3, 4]
    [5, 6, 7 ,8] 
  B [9,10,11,12]
"""

def spiralOrder(matrix):
    res = []
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    while left < right and top < bottom:
        for i in range(left, right): # get i in top row
            res.append(matrix[top][i])
        top += 1
        for i in range(top, bottom): # get i in right row
            res.append(matrix[i][right-1])
        right -= 1
        if not (left < right and top < bottom): break # for row/col matrix
        for i in range(right-1,left-1,-1): # get i in bottom row
            res.append(matrix[bottom-1][i])
        bottom -= 1
        for i in range(bottom-1, top-1, -1): # get i in right row
            res.append(matrix[i][left])
        left += 1
        
    return res

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7 ,8],
    [9,10,11,12]
]
print(spiralOrder(matrix))

matrix2 = [
    [1, 2, 3, 4],
]
print(spiralOrder(matrix2))


matrix3 = [
    [1], [2], [3], [4],
]
print(spiralOrder(matrix3))