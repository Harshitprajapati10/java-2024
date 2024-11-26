# problem 37
# Meeting rooms I
# premium, lC 252

# Determine if person can attend all the meetings

# intervals = [(0,30),(5,10),(15,20)]
# Output = False


# sort based on start time

class Interval:
    def __init__(self,start,end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self,intervals):
        intervals.sort(key=lambda i:i.start)
        for i in range(1,len(intervals)):
            i1 = intervals[i-1]
            i2 = intervals[i]
            if i1.end > i2.start:
                return False
        return True

O = Solution()
intervals = [
    Interval(0,30),
    Interval(5,10),
    Interval(15,20)
]
print(O.canAttendMeetings(intervals))