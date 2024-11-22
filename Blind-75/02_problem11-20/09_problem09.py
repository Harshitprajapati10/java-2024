# leetcode 139 -> word break
# can construct
# use multiple times words possible


def can_construct(target, word_bank, memo=None):
    if memo is None:
        memo = {}
    
    if target in memo:
        return memo[target]
    
    if target == "":
        return True
    
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            if can_construct(suffix, word_bank, memo):
                memo[target] = True
                return True
    
    memo[target] = False
    return False
