# problem 54
#Valid palindrome
# Lc 125

def validpalindrome(s):
    newStr = ""
    for c in s:
        if c.isalnum():
            newStr += c.lower()
    return newStr == newStr[::-1]

s = "A man, a plan, a canal; Panama"
print(validpalindrome(s))
print(validpalindrome("race a car"))