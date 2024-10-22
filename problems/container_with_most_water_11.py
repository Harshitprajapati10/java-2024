# two pointers one from start and other from end

def maxArea(height):
        ans, l, r = 0, 0, len(height)-1
        while(l<r):
            area = abs(l-r) * min(height[l], height[r])
            ans = max(ans, area)
            if height[l] < height[r]: l+=1
            else: r-= 1
        return ans

print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))