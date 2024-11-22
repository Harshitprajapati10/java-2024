# Leetcode 198 -> House robber

# given array of adjacent houses 
# cannot rob two adjacent houses
# return maximum amount you can rob


# example -> [1, 2 ,3 ,1]
# ans -> 4

# make decision tree, solve by recursion , memoize it

class Solution:
    def maxCosthelper(self,nums, i, memo = None):
        if(memo is None): memo = {}
        if(i in memo): return memo[i]
        if(i>=len(nums)): return 0
        memo[i] =  max(
            nums[i] + self.maxCosthelper(nums, i+2,memo), 
            nums[i] + self.maxCosthelper(nums, i+3,memo)
        )
        return memo[i]

    def maxCost(self,nums):
        # Time -> O(n), space-> O(n)
        return max(self.maxCosthelper(nums,0), self.maxCosthelper(nums, 1))
    
    def maxCostIterative(self, nums):
        # [1,2,3,1]
        # [1,2,3,1,0]
        # [1,3,3,3,1,0]
        # [4,3,3,3,1,0] -> ans is 4
        # Time -> O(n), space -> O(1)
        nums.append(0)
        for i in range(len(nums)-4,-1,-1):
            nums[i] += max(nums[i+2], nums[i+3])
        return max(nums[0], nums[1])
    
    def maxCostIterativeTwo(self, nums):
        # [1,2,3,1] # pointer method
        # rob1 = 0, rob2 = 1
        # rob1 = 1, rob2 = 2
        # rob1 = 2, rob2 = 4
        # rob1 = 4, rob2 = 4
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1,rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

obj = Solution()


print(obj.maxCost([5])) 
print(obj.maxCost([1,2,3,1])) #4
print(obj.maxCost([2,1,2,1,3,2,1])) #8

print(obj.maxCostIterative([5])) 
print(obj.maxCostIterative([1,2,3,1])) 
print(obj.maxCostIterative([2,1,2,1,3,2,1])) #8

print(obj.maxCostIterativeTwo([1,2,3,1])) 
print(obj.maxCostIterativeTwo([2,1,2,1,3,2,1])) #8


