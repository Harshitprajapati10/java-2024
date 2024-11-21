# 338
# counting bits

# n = 2
# count bits for 0,1,2
# ans = [0,1,1]

def countBits(n):
    dp = [0] *(n+1)
    offset = 1
    for i in range(1, n+1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i-offset]
    return dp

ans = countBits(2)
print(ans)