# 191
# No of one bits 
# n = 1011 (11)
# output= 3

def hammingWeight(n):
    res = 0
    while n:
        n&=(n-1)
        res += 1
    return res

print(hammingWeight(11))