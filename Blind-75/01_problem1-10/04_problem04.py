# 238 -> product of array except self

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