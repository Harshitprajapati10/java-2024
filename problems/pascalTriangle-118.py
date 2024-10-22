# Given an integer numRows, return the first numRows of Pascal's triangle
# Input: numRows = 5
"""
 Output: [
             [ 1 ],
            [ 1, 1 ],
           [ 1, 2, 1 ],
          [ 1, 3, 3, 1 ],
         [ 1, 4, 6, 4, 1 ]

        ]
"""

def generate(numRows):
    triangle = []
    for i in range(numRows):
        row = [1] * (i+1)
        for j in range(1,i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle

# print(generate(15))



# returning nth row of pascals triangle
def generaterow(numRows):
    triangle = []
    for i in range(numRows):
        row = [1] * (i+1)
        for j in range(1,i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle[numRows-1]

print(generaterow(5))