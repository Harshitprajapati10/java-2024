# problem 57
# Encode and decode strings
# pre, LC 271

def encode(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res

def decode(strs):
    res, i = [],0
    while i< len(strs):
        j = i
        while(strs[j] != "#"):
            j+=1
        length = int(strs[i:j])
        res.append(strs[j+1 : j+1+length])
        i = j+1+length
    return "".join(res)

s = "harshit"
encoded = encode(s)
print(encoded)
decoded = decode(encoded)
print(decoded)
