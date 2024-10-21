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
    for rows in range(numRows):
        elements = []
        for col in range(rows + 1): # 1 2  3  4 5

            elements.append(col + 1)
            # prev = elements

        triangle.append(elements)
    return triangle

print(generate(5))