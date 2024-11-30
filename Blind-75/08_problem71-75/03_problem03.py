# problem 73
#find median from data stream

# LC 295

"""
create two heaps

.add(3)
.add(2)
.add(7)
.add(4)
.getMedian()

*)first add in minHeap
*)|len(maxHeap) - len(miHeap)|<= 1, check on each step
*) Also largest from maxHeap < smallest from MinHeap
*) If len is even median in  (largest from maxHeap + smallest from MinHeap)/2, else find it

SMALL HEAP              LARGE HEAP           sizeDiff          Max(small) < min(large)
(MaxHeap)                (MinHeap)
 [3]                        []                  1(OK)                          T
 [3,2]                      []                  2(Not Ok, 3-->miHeap)          T
 [2]                        [3]                 0(Ok)                          T
 [7,2]                      [3]                 1(Ok)                          F
 [2]                      [3,7]                 1(Ok)                          T
 [4,2]                    [3,7]                 0(Ok)                          F
 [2]                    [3,4,7]                 2(Not Ok,3--> maxheap)         F
 [2,3]                    [4,7]                 1(Ok)                          T


Median = 3+4/2 = 3.5

"""


import heapq

class MedianFinder:
    def __init__(self) :
        self.small = []
        self.large = []
    
    def addNum(self, num):
        heapq.heappush(self.small, -1*num)

        # every num is small is <= every num in large
        if (self.small and self.large and
            (-1*self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # uneven size
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small,-1* val)
        
    def findMedian(self):
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-1*self.small[0] + self.large[0]) /2
    
obj = MedianFinder()
obj.addNum(3)
obj.addNum(2)
obj.addNum(7)
obj.addNum(4)
obj.addNum(5)
obj.addNum(10)

print(obj.findMedian())
        
        