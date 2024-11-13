# leetcode 416
# partition equal subset sum
# example => [1,5,11,5] sum = 22, sum/2 = 11
# 1+5+5 = 11 = 11 , return true else false

class solution:
    def canPartition(self, nums):
        if sum(nums) %2 :
            return False
        dp = set()
        dp.add(0)
        target = sum(nums) // 2
        
        for i in range(len(nums)-1, -1, -1):
            nextDP = set()
            for t in dp :
                if t+nums[i] == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return True if target in dp else False
    
# [1,5,11,5]
# dp = {0,5,11,16,10,21,1,6,12,17,22} <= target
# if target in dp , return true

obj = solution()
print(obj.canPartition([1,5,11,5]))