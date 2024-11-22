# 55 Jump Game

# construct decision tree, memoize
#[2,3,1,1,4] -> True

class Solution:
    def jumpGame(self,nums):
        return self._JumpGame(0, nums, {})
    def _JumpGame(self, i, nums, memo):
        if i in memo: 
            return memo[i]
        if i >= len(nums) - 1: 
            return True
        if nums[i] == 0: 
            memo[i] = False
            return False    
        for j in range(1, nums[i] + 1):
            if self._JumpGame(i + j, nums, memo):
                memo[i] = True
                return True
        
        memo[i] = False
        return False
    
    def canJump(self, nums):    #Greedy
        max_reachable = 0
        for i, jump in enumerate(nums):
            if i > max_reachable:  
                return False
            max_reachable = max(max_reachable, i + jump)
        return max_reachable >= len(nums) - 1
    
O = Solution()
print(O.jumpGame([2,3,1,1,4] ))
print(O.jumpGame([2,0,0,1,4] ))