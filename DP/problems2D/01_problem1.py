# Unique paths I,II->  how many unique paths to travel though a n cross
# Leetcode 62  , 63
# m grid

import math

class Solution:
    def UniquePaths(self,m,n):
        return math.comb(m+n-2, m-1)

    def uniquePathsObs(self,grid):
        memo = {}
        return self._uniquePathsObsHelper(grid, 0, 0, memo)

    def _uniquePathsObsHelper(self,grid, row, col, memo):
        if row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 1:
            return 0
        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            return 1
        if (row, col) in memo:
            return memo[(row, col)]        
        right_paths = self._uniquePathsObsHelper(grid, row, col + 1, memo)
        down_paths = self._uniquePathsObsHelper(grid, row + 1, col, memo)

        memo[(row, col)] = right_paths + down_paths
        return memo[(row, col)]


def main():
    obj = Solution()
    
    print(obj.UniquePaths(1,1))
    print(obj.UniquePaths(2,2))
    print(obj.UniquePaths(3,3))
    print(obj.UniquePaths(4,3))
    print(obj.UniquePaths(4,4))

    print(obj.uniquePathsObs([
        [0, 0],
        [0, 0]
    ]))
    print(obj.uniquePathsObs([
        [0, 1],
        [0, 0]
    ]))

if __name__ == "__main__":
    main()