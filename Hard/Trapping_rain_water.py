# Trapping rain water problem 42
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

"""
BAD WAY OF DOING THIS PROBLEM, BY CREATING ARRAYS

Runtime: 31 ms, faster than 92.80% 
Memory Usage: 18.8 MB, less than 5.93%

"""

def getMaxLeft(nums):   # [0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
    maxLeft = []
    maxsofar = 0
    for i in range(len(nums)):
        maxLeft.append(maxsofar)
        maxsofar = max(maxsofar, nums[i])   
    return maxLeft

def getMaxRight(nums): # [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 0]
    maxRight = []
    maxsofar = 0
    for j in range(len(nums)-1,-1,-1):
        maxRight.append(maxsofar)
        maxsofar = max(maxsofar, nums[j])
    return maxRight [::-1]

def trap(height):   #   [0,1,0,2,1,0,1,3,2,1,2,1]
    maxLeft = getMaxLeft(height)
    maxRight = getMaxRight(height)
    
    minOfLeftRight = [] # [0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 1, 0]
    for i in range(len(height)):
        minSoFar = min(maxLeft[i], maxRight[i])
        minOfLeftRight.append(minSoFar)    
    
    water = 0
    for j in range(len(height)):
        waterDroplet = minOfLeftRight[j] - height[j]
        if waterDroplet <= 0:
            continue
        water += waterDroplet
    
    return water


    

# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# print(trap(height=height))


"""
DOING USING TWO POINTERS 

1) shift smaller of L,R by one
2) check maxL/maxR - height[i] > 0 add in ans
3) change value of maxL and maxR

[0 , 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
L                                   R , maxL = 0, maxR = 1, maxL - i = 0, maxR - i = 0
Shift smaller by one
[0 , 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    L                               R , maxL = 0, maxR = 1, maxL - i = 0, maxR - i = 0

[0 , 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        L                          R , maxL = 1, maxR = 1, maxL - i = |1|, maxR - i = 0

[0 , 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
           L                       R , maxL = 1, maxR = 1, maxL - i = -1, maxR - i = 0

[0 , 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
              L                    R , maxL = 2, maxR = 1, maxL - i = |1|, maxR - i = 0

[0 , 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
              L                 R    , maxL = 2, maxR = 1, "maxL - i = |1|", maxR - i = -1

[0 , 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
              L              R       , maxL = 2, maxR = 2, "maxL - i = |1|", maxR - i = |1|

[0 , 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
                 L           R       , maxL = 2, maxR = 2, maxL - i = |2|, "maxR - i = |1|"

[0 , 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
                    L        R       , maxL = 2, maxR = 2, maxL - i = |1|, "maxR - i = |1|"

[0 , 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
                       L     R       , maxL = 2, maxR = 2, maxL - i = -1, "maxR - i = |1|"

[0 , 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
                          L  R       , maxL = 3, maxR = 2, maxL - i = |1|, "maxR - i = |1|"

[0 , 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
                          L,R         loop over false condition
"""


# Runtime: 3 ms, faster than 99.83% 
# Memory Usage: 18.1 MB, less than 99.72%

def trapByPointers(height):
    l = 0
    r = len(height) - 1
    maxL = maxR = ans = 0    
    while l < r:
        if height[l] < height[r]: 
            if height[l] >= maxL: maxL = height[l]
            else: ans += maxL - height[l]
            l += 1
        else: 
            if height[r] >= maxR: maxR = height[r]
            else:
                ans += maxR - height[r]
            r -= 1          
    return ans


height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trapByPointers(height))