# 153
# Find minimum in rotated sorted array
# use binary search

def findMin(nums):
    res = nums[0]
    l,r = 0, len(nums)-1
    while l<=r:
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break
        m = (l+r)//2
        res = min(res, nums[m])
        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m -1
    return res

print(findMin([8,9,3,5,7]))