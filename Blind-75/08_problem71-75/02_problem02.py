# problem 72

# Top K frequent elements
# LC 347
# BUCKET SORT


"""
nums = [1,1,1,2,2,100], k = 2
output : [1,2]

create a array ~ len(nums)
    [0, 1, 2, 3, 4, 5, 6] -> represents no of times of occuring of elements
       100 2  1
    -> Traverse from right and get top k frequent elements
       
"""

def topKfrequent(nums, k):
    count = {}
    freq = [[] for i in range(len(nums)+1)]
    for n in nums:
        count[n] = 1 + count.get(n,0)
    for n,c in count.items():
        freq[c].append(n)
    
    res = []
    for i in range(len(freq)-1,0,-1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

nums = [1,1,1,2,2,100]
k = 2
print(topKfrequent(nums,k))