# Maximum product subarray 
# leetcode 152
# find continous subarray with max product

# example : [2,3,-2,4]
# ans : 6

# strategy : use max and min till index i 

class solution:
    def maxProduct(self, nums):
        res = max(nums)
        curMin, curMax = 1,1
        for n in nums:
            if n == 0:
                curMin, curMax = 1,1
                continue
            tmp =  curMax * n
            curMax = max(n * curMax, n*curMin, n)
            curMin = min(tmp, n* curMin, n)
            res = max(res, curMax)
        return res


obj = solution()
print(obj.maxProduct([2,3,-3,4]))