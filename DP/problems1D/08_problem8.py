# leetcode 322  -> Coin change
# no of coins required to sum up to target

class Solution:

    def _coinChangeHelper(self,nums, target, memo = None):
        if memo is None: memo = {}
        if target in memo: return memo[target]
        if target == 0: return []
        if target < 0: return None
        shortest_comb = None

        for num in nums:
            remainder = target - num
            remainder_result = self._coinChangeHelper(nums, remainder, memo)
            if remainder_result is not None:
                combination = remainder_result + [num]
                if shortest_comb is None or len(combination) < len(shortest_comb):
                    shortest_comb = combination
        memo[target] = shortest_comb
        return shortest_comb

    def coinChange(self,nums, target):
        result = self._coinChangeHelper(nums, target)
        return -1 if result is None else len(result)
    
obj = Solution()
print(obj.coinChange([1,2,5],11))
print(obj.coinChange([2],3))