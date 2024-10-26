"""

A = [ 1, 2, 3 , 4 ,5 ,6 ,7]
B = [1, 2 , 3 , 4 , 5]
merged = [1,1,2,2,3,3,4,4,5,5,6,7] , total = 12
ans = 7/2 = 3.5

half = 6

B = [ 1, 2 ,3 ,4 , 5]
     s      m      e,   m = s+(e-s)/2

half - (mid+1) = 6 - 3 = 3
take 3 from A

A = [ 1, 2, 3 , 4 ,5 ,6 ,7 ]
            p

concluson 1 :if p < = m + 1 and m <= p+1 then ans is max(m,p) + min(m+1,p+1) divided by 2 if total elements is even
if total element is odd then return max(m,p)

###################################

A = [ 1, 2, 3 , 4 ,5 ,6 ,7]
B = [1, 2 , 3 , 4]
merged = [1,1,2,2,3,3,4,4,5,6,7] , total = 11
ans = 3

half = 11//2 = 5

B = [ 1, 2 ,3 ,4]
     s   m      e,   m = s+(e-s)/2

half - (mid+1) = 6 - 2 = 4
take 4 from A    

A = [ 1, 2, 3 , 4 ,5 ,6 ,7 ]
                p

p > m+1 -> do something s = m + 1
m < p+1 -> do nothing

nums2 iteration
B = [ 1, 2 ,3 ,4]
            s  e,   m = s+(e-s)/2
            m

half - (mid+1) = 6 - 3 = 3
take 3 from A
A = [ 1, 2, 3 , 4 ,5 ,6 ,7 ]
            p
p <= m+1
m <= p+1     , return  max(m,p) if len(A+B) = odd, else max(m,p)+min(m+1,p+1)/2


######################################
if m>p+1 then e = m


########################################

A = [ 1, 2, 3 , 4 ,5 ,6 ,7]
B = [1, 2 , 3 , 4 , 5]
merged = [1,1,2,2,3,3,4,4,5,5,6,7] , total = 12
ans = 7/2 = 3.5

half = 6

A = [ 1, 2, 3 , 4 ,5 ,6 ,7 ]
     s          m        e,     m = s+(e-s)/2

half - (mid+1) = 6 - 4 = 2
take 2 from B

B = [ 1, 2, 3 , 4 ,5 ]
         p

p <= m+1  
m > p+1 -> do something -> e = m

nums2 iteration:
A = [ 1, 2, 3 , 4 ,5 ,6 ,7 ]
     s   m       e            
take 4 from B

B = [ 1, 2, 3 , 4 ,5 ]
                p
p > m+1 -> do something -> s = m+1
m <= p+1 -> do nothing

third iteration:
A = [ 1, 2, 3 , 4 ,5 ,6 ,7 ]
            s   e 
            m

take 3 from B

B = [ 1, 2, 3 , 4 ,5 ]
            p

p <= m+1 -> do nothing
m <= p+1 -> do nothing

return max(p,m) + min(p+1,m+1) -> answer

"""

def medianOfSortedArrays(nums1, nums2):

    if len(nums1) > len(nums2): # nums1 is smaller
        nums1, nums2 = nums2, nums1
    half = (len(nums1) + len(nums2))// 2
      
    s = 0 # do binary search on nums1
    e = len(nums1) 

    while s <= e:
        m = (s + e) // 2 
        n = half - m 
        maxLeft1 = float('-inf') if m == 0 else nums1[m - 1]
        minRight1 = float('inf') if m == len(nums1) else nums1[m]
        maxLeft2 = float('-inf') if n == 0 else nums2[n - 1]
        minRight2 = float('inf') if n == len(nums2) else nums2[n]

        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1: # ans condition
            if (len(nums1) + len(nums2)) % 2 == 0:
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
            else:
                return max(maxLeft1, maxLeft2)
            
        elif maxLeft1 > minRight2: e = m - 1  
        else: s = m + 1

A = [ 1, 2, 3 , 4 ,5 ,6 ,7]
B = [1, 2 , 3 , 4 ,5]
print(medianOfSortedArrays(A,B))