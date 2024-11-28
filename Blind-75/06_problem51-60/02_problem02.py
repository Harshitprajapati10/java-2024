# problem 52
# Group Anagrams
# LC 48

from collections import defaultdict


def groupAnagrams(strs):    
    res = defaultdict(list)
    for s in strs:
        count = [0]*26
        for c in s:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(s)
    return list(res.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))