# Maximum sum subarray

def maxSum(nums):
    maxsum = ans = nums[0]  
    for n in nums[1:]:  
        maxsum = max(n, maxsum + n) 
        ans = max(ans, maxsum)
    return ans

print(maxSum([1,-1,-4,2,1,-4,3]))
