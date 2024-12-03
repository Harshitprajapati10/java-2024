# LC 17, letter combination of a phone number

def letterComb(digits):
    digitsToLetters = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz",
    }
    res = []
    def dfs(i,word):
        if len(word) == len(digits):
            res.append(word)
            return
        for c in digitsToLetters[digits[i]]:
            dfs(i+1, word+c)
    if digits:
        dfs(0, "")
    return res

print(letterComb("23"))