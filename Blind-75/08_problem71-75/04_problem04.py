# problem 74
# Valid Anagram
# problem 242


def isValid(s,t):
    return sorted(s) == sorted(t)

print(isValid("anagram","nagaram"))
print(isValid("rat","car"))
print(isValid("rat","carads"))