# Decode ways
# leetcode 91

# given a number string  , return total ways to decode it to letter
# "A" -- 1, ....., "Z" -> 26

# example -> 11106,  1 11 06 and 1 1  10 6 
# ans is 2
# example -> 12 -> ans is two 

def numDecodings(s):

    dp = {len(s) : 1}
    for i in range(len(s) -1, -1, -1):

        if s[i] == "0": dp[i] = 0
        else: dp[i] = dp[i+1]

        if ( i+ 1 < len(s) and (s[i]== "1" or s[i]=="2" and s[i+1] in "0123456")):
            dp[i] += dp[i+2]
    return dp[0]

print(numDecodings("12"))
print(numDecodings("121"))

# s = 121
# {3:1}
# {1:1, 3:1}
# {1:1, 2:1, 3:1}