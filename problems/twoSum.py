# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.



# 001 -> Two sum 1

def twoSum(nums, target):
    hash_set = {} # to store val, index
    for i, n in enumerate(nums):
        complement = target - n
        if complement in hash_set:
            return [hash_set[complement], i ]       
        hash_set[n] = i
    return []

# Two Sum II
def twoSumTwo(nums, target): #pass sorted array
    l = 0
    r = len(nums) - 1
    while(l<=r):
        if nums[l] + nums[r] < target: 
            l+=1
        elif nums[l] + nums[r] > target:
            r-=1
        else:
            return [l,r]
    return []


def threeSum(nums): # sum to zero
    res = []
    nums.sort()
    for i, a in enumerate(nums):
        if i>0 and a == nums[i-1]:
            continue

        l,r = i+1, len(nums)-1
        while l<r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l+=1
                while nums[l] == nums[l-1] and l<r:
                    l+=1
    return res


nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))

# nums = [4,7,11,15,4,2,7,9,8]
# tar = 13
# print(twoSum(nums,tar))
# nums.sort()
# print(twoSumTwo(nums,tar))


# tar = 9
# nums = [0,4,5,6,7,8]
# print(twoSumTwo(nums,tar))


"""
TWO SUM II

tar = 9
nums = [2,4,5,6,7,8]
l = 0
r = 5
if nums[l] + nums[r] > tar -> shift left one step ahead
if nums[l] + nums[r] < tar -> shift right one step back
if nums[l] + nums[r] = tar -> return [l,r] for 0 indexed array

"""