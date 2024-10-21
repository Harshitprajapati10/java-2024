# find duplicate in an array

def containsDuplicate(nums):
        hash_set = set()
        for i in nums:
            hash_set.add(i)
        return True if len(nums) > len(hash_set) else False

print(containsDuplicate([1,2,3,1]))