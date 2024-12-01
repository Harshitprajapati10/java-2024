

#


def mergeTwoArrays(nums1,nums2):
    f,s = 0,0
    res = [] 
    while(f<len(nums1) and s<len(nums2)):
        if nums1[f] <= nums2[s]:
            res.append(nums1[f])
            f += 1
        else:
            res.append(nums2[s])
            s += 1
    if f < len(nums1):
        res += nums1[f:]
    if s < len(nums2):
        res += nums2[s:]

    return res

nums1 = [2]
nums2 = [1]
# output = [1,2,3,4,5,6,7,8]
print(mergeTwoArrays(
    nums1,
    nums2
))


def mergeInPlace(nums1, m, nums2, n):
     i, j, k = m - 1, n - 1, m + n - 1
     while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
     while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
     return nums1



nums1 = [1,2,3,4,0] 
m = 4
nums2 = [2]
n = 1
ans = mergeInPlace(nums1, m, nums2, n)
print(ans)