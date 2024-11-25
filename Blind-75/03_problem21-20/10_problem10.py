# 128, Longest consecutive sequence

# [100,4 ,200,1,3,2]
# 1,2,3,4 ans is 4

class Sol:
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length+=1
                longest=max(length,longest)
        return longest

obj = Sol()
nums = [100,4 ,200,1,3,2]
print(obj.longestConsecutive(nums))