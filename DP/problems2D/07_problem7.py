# Leetcode 329
# Longest increasing path in a matrix

"""

["9",  9, 4]
["6",  6, 8]
["2", "1", 1]    Longest Increasing path is 4 as indicated by ""

create a hashmap or a matrix
# hashmap : (r,c) -> longest path
    To get longest path use dfs
# return max value of hashmap

*) LongestPathMatrix
    [1, 1, 2]
    [2, 2 ,1]
    [3, 4, 2]
max value = 4 //Answer

"""

class Solution:
    def longestInceasingPath(self, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
        memo = {}

        def dfs(r, c, prevVal):
            if (r<0 or r == ROWS or c<0 or c== COLS or matrix[r][c] <= prevVal):
                return 0
            if (r,c) in memo:
                return memo[(r,c)]
            res = 1
            res = max(res, 1 + dfs(r+1,c, matrix[r][c]))
            res = max(res, 1 + dfs(r-1,c, matrix[r][c]))
            res = max(res, 1 + dfs(r,c+1, matrix[r][c]))
            res = max(res, 1 + dfs(r,c-1, matrix[r][c]))
            memo[(r,c)] = res
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,-1)
        
        return max(memo.values())
    
obj = Solution()
matrix = [
    [9,9,4],
    [6,6,8],
    [2,1,1]
]
print(obj.longestInceasingPath(matrix))