# Lc 392

# is SUbsequence
# bottom up dp



def isSubseq(s,t):
    dp = [[False for _ in range(len(t)+1)] for _ in range(len(s)+1)]
    for i in range(len(t)+1):
        dp[len(s)][i] = True
    for i in range(len(s)-1,-1,-1):
        for j in range(len(t)-1,-1,-1):
            if s[i] == t[j]:
                dp[i][j] = dp[i+1][j+1]
            else:
                dp[i][j] = dp[i][j+1]
    return dp[0][0]

s = "abc"
t = "ahbgdc"
print(isSubseq(s,t))
print(isSubseq("axc","ahbgdc"))