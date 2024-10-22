def minimumTotal(triangle):
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
    return triangle[0][0]


triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(minimumTotal(triangle))

"""
DRY RUN

[[2],
[3,4],
[6,5,7],
[4,1,8,3]]


[[2],
[3,4],
[7,6,10], #update this  -> this + min of bottom ones pairwise
[4,1,8,3]]

[[2],
[9,10], #update this
[7,6,10],
[4,1,8,3]]

[[11], #update this 
[9,10],
[7,6,10],
[4,1,8,3]]

"""