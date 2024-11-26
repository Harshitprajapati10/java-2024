# Problem 34
# Insert Interval
# leetcode 57

# intervals = [[1,3],[6,9]]
# newInterval = [2,5]
# Output = [[1,5],[6,9]]

def InsertInterval(intervals, newInterval):
    res = []
    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return res + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
        else:
            newInterval = [
                            min(newInterval[0], intervals[i][0]),
                            max(newInterval[1], intervals[i][1])
            ]
    res.append(newInterval)
    return res

intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(InsertInterval(intervals,newInterval))

print(InsertInterval(
    [[1,2],[3,5],[6,7],[8,10],[12,16]],
    [4,8]
)) # [[1,2],[3,10],[12,16]]