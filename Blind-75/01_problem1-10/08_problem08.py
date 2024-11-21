# 33
# search in rotated sorted array

def search(nums, target):
    l,r = 0, len(nums)-1

    while l<=r :
        mid = (l+r)//2
        if target == nums[mid]:
            return mid
        
        # left sorted portion
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target<nums[l]:
                l = mid + 1
            else:
                r = mid -1
        
        # right sorted portion
        else:
            if target < nums[mid] or target>nums[l]:
                r = mid-1
            else:
                l = mid + 1
    return -1


print(search([8,9,3,5,7],5))