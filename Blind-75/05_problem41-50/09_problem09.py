# Slinding window

# problem 49
# Longest Substring without repeating characters
# LC: 3

# s = "abcabcbb"
# ouput : 3

"""
Use Sliding window technique to solve this

s = " a b c a b c b b "

"""


def longest_substring(s):
    charSet = set()
    l = 0
    res = 0
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r-l+1)
    return res


print(longest_substring("abcabcbb"))
print(longest_substring("abcabcdb"))
print(longest_substring(""))
print(longest_substring("aaaaaa"))
print(longest_substring("abcdefghijklmnopqrstuvwxyz"))

