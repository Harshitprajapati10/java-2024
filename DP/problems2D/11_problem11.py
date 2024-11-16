# Leetcode 10
# Regular expression matching

# create decision tree, use recursion and memoization

class Solution:
    def isMatch(self, s, p):
        memo = {}
        def dfs(i, j):
            if (i, j) in memo: return memo[(i,j)]
            if i >= len(s) and j >= len(p): return True
            if j >= len(p):return False 
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if (j+1) < len(p) and p[j+1] == "*": 
                memo[(i,j)] = (dfs(i, j+2) or (match and dfs(i +1 ,j)))
                return memo[(i,j)]
            if match: 
                memo[(i,j)] = dfs(i +1,j +1)
                return memo[(i,j)]
            
            memo[(i,j)] = False
            return False
        return dfs(0,0)
    
o = Solution()
print(o.isMatch("aa","a."))
print(o.isMatch("aaaaa","a*"))