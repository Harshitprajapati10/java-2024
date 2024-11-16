# Two Sum , Leetcode 1

def twoSum(nums, target):
    hash_set = {} # to store val, index
    for i, n in enumerate(nums):
        complement = target - n
        if complement in hash_set:
            return [hash_set[complement], i ]       
        hash_set[n] = i
    return []

print(twoSum([2,3,4,5,1],3))

