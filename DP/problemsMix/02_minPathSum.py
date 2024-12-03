# lc 64


class Solution:
    def minPathSum(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[0] * COLS for _ in range(ROWS)]

        dp[0][0] = grid[0][0]

        for c in range(1, COLS):
            dp[0][c] = dp[0][c-1] + grid[0][c]

        for r in range(1, ROWS):
            dp[r][0] = dp[r-1][0] + grid[r][0]

        for r in range(1, ROWS):
            for c in range(1, COLS):
                dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + grid[r][c]
        return dp[ROWS-1][COLS-1]

obj = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
print(obj.minPathSum(grid))
print(obj.minPathSum([[1,2,3],[4,5,6]]))