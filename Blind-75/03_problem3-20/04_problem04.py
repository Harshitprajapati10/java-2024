# Unique path 62

import math

class Solution:
    def UniquePaths(self,m,n):
        return math.comb(m+n-2, m-1)
    
obj = Solution()
    
print(obj.UniquePaths(1,1))
print(obj.UniquePaths(2,2))
print(obj.UniquePaths(3,3))
print(obj.UniquePaths(4,3))
print(obj.UniquePaths(4,4))