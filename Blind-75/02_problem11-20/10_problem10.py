# 39 
# combination Sum

# return unique combination to sum up to target
# ex : [2,3,6,7] tar = 7
# [[2,2,3],[7]]
# construct a unique type decision tree


def combinationSum(nums, target):
    res = []

    def dfs(i, cur,total):
        if total == target:
            res.append(cur.copy())
            return
        if i >= len(nums) or total > target:
            return 
        
        cur.append(nums[i])
        dfs(i, cur, total + nums[i])
        cur.pop()
        dfs(i+1, cur, total)

    dfs(0,[],0)
    return res

print(combinationSum([2,3,6,7],7))
print(combinationSum([2,5,2,1,2],5))

