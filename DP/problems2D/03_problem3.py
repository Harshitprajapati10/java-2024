# Leetcode 309
# best time to buy and sell stock with cooldown

# construct decision tree , solve, write code, memoize


def maxProfit(prices):
    dp = {}
    def dfs(i, buying):
        if i >= len(prices):
            return 0
        if (i, buying) in dp:
            return dp[(i, buying)]
        cooldown = dfs(i + 1, buying)

        if buying:
            buy = dfs(i+1, not buying) - prices[i]
            dp[(i, buying)] = max(buy, cooldown)
        else:
            sell = dfs(i+2, not buying) + prices[i]
            dp[(i, buying)] = max(sell, cooldown)
        return dp[(i, buying)]
    
    return dfs(0, True)

print(maxProfit([1,2,3,0,2]))