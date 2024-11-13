# Leetcode 300
# longest increasing subsequence

# use decision tree -> constructed
# use right to left approach(DP)

class solution:
    def lengthLIS(self,nums):
        LIS = [1]*(len(nums))

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i],1 + LIS[j])
        return max(LIS)

obj = solution()
print(obj.lengthLIS([0,1,4,2,1]))

# [0,1,4,2,1]
# LIS = [1,1,1,1,1]
# [3,2,1,1,1]