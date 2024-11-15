# Leetcode 115: Distinct subsequences

# s = " rabbbit "
# t = "rabbit"
# answer = 3, any one of three b is used

# use recursion -> dfs
# base case if s is "" return 0, if t is "" return 1

class Solution:
    def numDistinct(self, s , t):
        memo = {}

        def dfs(i,j):
            if j == len(t): return 1
            if i == len(s): return 0
            if (i,j) in memo: return memo[(i,j)]
            if s[i] == t[j]: memo[(i,j)] = dfs(i+1, j+1) + dfs(i+1, j)
            else: memo[(i,j)] = dfs(i+1,j)
            return memo[(i,j)]

        return dfs(0,0)

obj = Solution()
s = "rabbbit"
t = "rabbit"
print(obj.numDistinct(s,t))
