# problem 50
# sliding window
# Longest Repeating character replacement
# Leetcode 424

# s = AABABBA
# k = 2
# ouput = 5

"""
Make a count map for character tracking

windowlength -  most frequent character in map  <= k 
"""

def characterReplacement(s, k):
    count, res,l = {},0,0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r],0)
        while (r-l+1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, r-l+1)
    return res

print(characterReplacement("AABABBA",2))