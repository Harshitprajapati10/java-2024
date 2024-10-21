# 238. Product of Array Except Self
# [1,2,3,4] -> [24,12,8,6]

def productExceptSelf(nums):
    product,product_rev,answer = 1, 1 ,[]
    for i in range(len(nums)):        
        answer.append(product)
        product *= nums[i]
    for j in range(len(nums),0,-1):
        answer[j-1] *= product_rev
        product_rev *= nums[j-1]
    return answer

def main():
    print(productExceptSelf([1, 2, 3, 4]))
    print(productExceptSelf([6, 2, 3, 1]))

if __name__ == "__main__":
    main()

# 24,12,4,1
# 1,1,2 6
# answer = 24, 12, 8, 6

"""
Runtime: 22 ms, faster than 99.17% of Python3 online submissions 
Memory Usage: 22.5 MB, less than 98.58% of Python3 online submissions 
"""