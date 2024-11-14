# Leetcode 548
# coin change II, return total ways to sum to target

"""  
(5,[1,2,5])

      5  4  3  2  1  0
1  [  X  X  X  X  X  1  ]
2  [  X  X  X  X  X  1  ]
5  [  X  X  X  X  X  1  ]

1-5 = -4 , look at -4, nothing found, add 0 and below one
if out of bound , put 0

i  |   a  0  1  2  3  4  5
5(2)   [  1  1  1  1  1  1  ]
2(1)   [  0  0  0  0  0  1  ]
1(0)   [  1  0  0  0  0  1  ]

"""


def coinChange(amount, coins):
    dp = [[0]*(len(coins) + 1) for i in range(amount + 1)]
    dp[0] = [1] * (len(coins) + 1)
    for a in range(1, amount + 1):
        for i in range(len(coins)-1, -1,-1):
            print(a,i)
            dp[a][i] = dp[a][i+1]
            if a - coins[i] >= 0:
                dp[a][i] += dp[a - coins[i]][i]
    return dp[amount][0]


print(coinChange(5, [1,2,5]))