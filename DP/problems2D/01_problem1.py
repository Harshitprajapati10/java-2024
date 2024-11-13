# Unique paths ->  how many unique paths to travel though a n cross
# Leetcode 62
# m grid

import math
def UniquePaths(m,n):
    return math.comb(m+n-2, m-1)

print(UniquePaths(1,1))
print(UniquePaths(2,2))
print(UniquePaths(3,3))
print(UniquePaths(4,3))
print(UniquePaths(4,4))
