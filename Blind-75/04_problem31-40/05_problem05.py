# problem 35
# Merge Intervals
# Leetcode 56


# intervals = [[1,3],[2,6],[8,10],[15,18]]
# output = [[1,6],[8,10],[15,18]]


# intervals = [[1,4],[4,5]]
# output = [[1,5]]

# first sort on basis of first, then iterate and check

def merge(intervals):
    intervals.sort(key=lambda i: i[0])
    output = [intervals[0]]
    for start, end in intervals[1:]:
        lastEnd = output[-1][1]
        if start <= lastEnd:
            output[-1][1] = max(lastEnd,end)
        else:
            output.append([start,end])
    return output

print(merge([[1,3],[8,10],[15,18],[2,6]]))
print(merge([[1,4],[4,5]]))


