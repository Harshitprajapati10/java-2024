"""

Given an integer array nums and an integer k, 
return true if there are two distinct indices 
i and j in the array such that nums[i] == nums[j] 
and abs(i - j) <= k.

"""

def containsNearbyDuplicate(nums, k):
        seen = set()
        
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
            
            if len(seen) > k:
                seen.remove(nums[i-k])
        return False

nums = [1,2,3,1]
k = 3

print(containsNearbyDuplicate(nums, 3))