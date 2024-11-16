# Leetcode 312, burst ballons
# Given array of ballons , get coins, return max coins

# Make decision tree, memoize

class Solution:

    def getCoins(self,nums):
        nums = [1] + nums + [1]
        return self._getCoinsHelper(nums, 1, len(nums)-2, {})
    
    def _getCoinsHelper(self, nums, left, right, memo):
        if left > right: return 0
        if (left, right) in memo: return memo[(left, right)]
        max_coins = 0
        for i in range(left, right + 1):
            coins = nums[left-1]*nums[i]*nums[right+1]
            coins += (self._getCoinsHelper(nums,left, i-1, memo) + 
                      self._getCoinsHelper(nums, i+1, right, memo))
            max_coins = max(max_coins, coins)
        memo[(left, right)] = max_coins
        return max_coins


o = Solution()
print(o.getCoins([3,1,5,8]))

# burst 1 -> burst 5 -> burst 3 -> burst 8
# [3,1,5,8] -> [3,5,8] -> [3,8] -> [8] -> []
# 3X1X5 + 3X5X8 + 1X3X8 + 1X8X1 = 15 + 120 + 24 + 8  = 167 
