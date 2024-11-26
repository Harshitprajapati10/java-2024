# problem 36
# Return no of intervals to remove to get 
# non overlapping intervals

# leetcode 435

# intervals = [[1,2],[2,3],[3,4],[1,3]]
# output = 1 (remove = (1,3))

# intervals = [[1,2],[1,2],[1,2]]
# output = 2

def eraseoverlapping(intervals):
    intervals.sort()
    res = 0
    prevEnd = intervals[0][1]
    for start,end in intervals[1:]:
        if start >= prevEnd:
            prevEnd = end
        else:
            res += 1
            prevEnd = min(end,prevEnd)
    return res

print(eraseoverlapping(
    [[1,2],[2,3],[3,4],[1,3]]
))
print(eraseoverlapping(
    [[1,2],[1,2],[1,2]]
))