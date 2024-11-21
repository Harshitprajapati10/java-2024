# 268
# Missing number

# find missing number in range from 0,n


def missingNumber(nums):
    res = len(nums)
    for i in range(len(nums)):
        res += (i-nums[i])
    return res

print(missingNumber([0,1,2,3,5,6]))