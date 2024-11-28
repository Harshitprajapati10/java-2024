# problem 56
# palindromic substrings
# LC 647

class Solution:
    def ALLpalindromicStrings(self, s):
        res = 0

        for i in range(len(s)):
            # for odd length string
            l,r = i, i
            while l>=0 and r<len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            # for even length string
            l,r = i, i + 1
            while l>=0 and r<len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res

obj = Solution()
print(obj.ALLpalindromicStrings("abc"))
print(obj.ALLpalindromicStrings("aaa"))
print(obj.ALLpalindromicStrings("cjsdklfjnanankkk"))