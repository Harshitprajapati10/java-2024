# 190
# Reverse bits of a 32 bit integer

def reverseBits(n):
    res = 0
    for i in range(32):
        bit = (n>>i) & 1
        res = res | (bit << (31-i))
    return res

print(reverseBits(43261596))    # 964176192