# 5 -> Longest palindromic substring
# find longest palindromic substring in s

# example -> babcd, ans-> bab
# cbbd -> bb

# start from index and expand from every index outwards and check for palindromes

class Solution:
    def longestPalindrome(self, s):
        res = ""
        resLen = 0

        for i in range(len(s)):
            # for odd length string
            l,r = i, i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if(r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l +1
                l -= 1
                r += 1

            # for even length string
            l,r = i, i + 1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if(r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l +1
                l -= 1
                r += 1

        return res

obj = Solution()
print(obj.longestPalindrome("babcd"))
print(obj.longestPalindrome("cbbd"))
print(obj.longestPalindrome("cjsdklfjnanankkk"))