# Leetcode -> 213
# House robber 2 -> houses are in circular arrangement


class Solution:

    # Recursive solution -> space  O(n) , time O(n)
    def _maxCosthelper(self, nums, i, memo = None ):
            if(memo is None): memo = {}
            if(i in memo): return memo[i]
            if(i>=len(nums)): return 0
            memo[i] = max(
                nums[i] + self._maxCosthelper(nums, i+2, memo), 
                nums[i] + self._maxCosthelper(nums, i+3, memo)
            )
            return memo[i]

    def _maxCost(self, nums):
        # for [2,1,2,1,3,2,1]
        # rob ->  [2,1,2,1,3,2] and [1,2,1,3,2,1] ->7 is ans
        return max(self._maxCosthelper(nums,0),self._maxCosthelper(nums, 1))
    
    def maxCostHouse(self, nums):
         # for [2,1,2,1,3,2,1]
         # rob ->  [2,1,2,1,3,2] and [1,2,1,3,2,1] -> 7 is ans
         return max(
              nums[0],
              self._maxCost(nums[1:]),
              self._maxCost(nums[:-1])
         )
    



    # linear space solution
    def _maxCostIterativeHelper(self, nums): # using sol of house robber one
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1,rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
    
    def maxCostIterative(self, nums):
         # for [2,1,2,1,3,2,1]
         # rob ->  [2,1,2,1,3,2] and [1,2,1,3,2,1] ->7 is ans
         return max(
              nums[0],
              self._maxCostIterativeHelper(nums[1:]), 
              self._maxCostIterativeHelper(nums[:-1])
        )

obj = Solution()

print(obj.maxCostHouse([2])) 
print(obj.maxCostHouse([2,1,2,1,3,2,1])) # 7
print(obj.maxCostHouse([1,4,5]))


print(obj.maxCostIterative([2]))
print(obj.maxCostIterative([2,1,2,1,3,2,1])) # 7
print(obj.maxCostIterative([1,4,5]))