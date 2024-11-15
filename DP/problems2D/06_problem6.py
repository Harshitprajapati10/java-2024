# Leetcode 97 : Interleaving string

# s1 = aabcc, s2 = dbbca
# s3 = aadbbcbcac


# create a 2D grid of n+1 cross m+1
"""
s1(i)  /  s2(j)       d    b   b   c   a   ""
                      0    1   2   3   4   5

 a     0           [   F   F   F   F   F   F   ]
 a     1           [   F   F   F   F   F   F   ]
 b     2           [   F   F   F   F   F   F   ]
 c     3           [   F   F   F   F   F   F   ]
 c     4           [   F   F   F   F   F   F   ]
 ""    5           [   F   F   F   F   F   T   ]

 *) Match charcter from i and j to i+j th index of s3
 *) If matches from i then put (True) if i+1 is true
 *) If matches from j then put (True) if j+1 is true
 *) If matches from i,j then put True if i+1 or j+1 is True

 *) s3 =  a  a  d  b  b  c  b  c  a  c
          0  1  2  3  4  5  6  7  8  9
 
 s1(i)  /  s2(j)      d    b   b   c   a   ""
                      0    1   2   3   4   5

 a     0           [   T   F   F   F   F   F   ]
 a     1           [   T   F   F   F   F   F   ]
 b     2           [   T   T   T   T   T   F   ]
 c     3           [   F   T   T   F   T   F   ]
 c     4           [   F   F   T   T   T   T   ]
 ""    5           [   F   F   F   F   F   T   ]

return grid[0][0]

"""
class Solution:
    def isInterleave(self, s1,s2, s3):
        
        if len(s1) + len(s2) != len(s3): return False
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2),-1, -1):
                if i < len(s1) and s1[i] == s3[i+j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i+j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]

obj = Solution()
print(obj.isInterleave("aabcc","dbbca","aadbbcbcac"))
