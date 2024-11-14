# 494 -> TargetSum
# Add + and - at each element of array
# Given array and a target , return total number of expression to form target


# nums = [1,1,1,1,1] target = 3
# ans => 5
# -1 +1 +1 +1 +1 = 3
# +1 -1 +1 +1 +1 = 3
# +1 +1 -1 +1 +1 = 3
# +1 +1 +1 -1 +1 = 3
# +1 +1 +1 +1 -1 = 3


# make decision tree => memoize

def findTargetSumWays(nums, target):
    memo = {}
    def backtrack(i, total):
        if i== len(nums):
            return 1 if total == target else 0
        if (i, total) in memo:
            return memo[(i, total)]
        memo[(i, total)] = backtrack(i+1, total + nums[i]) + backtrack(i+1, total - nums[i])
        return memo[(i, total)]
    return backtrack(0,0)

print(findTargetSumWays([1,1,1,1,1],3))