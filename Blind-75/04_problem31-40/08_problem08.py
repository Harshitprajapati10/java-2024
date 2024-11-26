# problem 38
# Meeting Rooms II
# premium, LC = 253

# find min no. of conference room required

# intervals = [(0,30),(5,10),(15,20)]
# output = 2( room1: (0,30), room2: (5,10),(15,20))


# sort on basis of start time

class Interval:
    def __init__(self,start,end):
        self.start = start
        self.end = end

class Solution:
    def numberOfRooms(self,intervals):
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        res, count = 0,0 
        s,e = 0,0
        while s<len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res


O = Solution()
intervals = [
    Interval(0,30),
    Interval(5,10),
    Interval(15,20)
]
print(O.numberOfRooms(intervals))