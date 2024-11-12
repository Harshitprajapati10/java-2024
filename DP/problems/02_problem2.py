# Leetcode 746 -> Minimum cost climbing stairs
# Given array cost of cost of climbing stairs, can climb one or two at a time,
# cost[i] is ith step cost
# can start either from 0 or 1 th index

# example -> [10,"15",20], ans = 15
# example -> ["1", 100 ,"1",1,"1",100,"1","1", 100, "1"]  ,ans = 6

# decision tree consturcted and implemented
# then memoize it

class solution:
    # helper function
    def min_cost(self, cost, i, memo = None):
        if(memo is None): memo = {}
        if(i in memo): return memo[i]
        if(i>=len(cost)): return 0
        memo[i] = min(
            cost[i] + self.min_cost(cost, i+1, memo), 
            cost[i] + self.min_cost(cost,i+2, memo)
        )
        return memo[i]

    def costClimbingStairs(self,cost):
        return min(self.min_cost(cost,0), self.min_cost(cost,1))
    
    def min_Cost_Iterative(self, cost): 
        # from right to left, in const space ,modify original array
        # [10,15,20,0]
        # [10, 15, 20 ,0]
        # [25, 15 ,20, 0]
        # min(25,15) -> ans is 15
        cost.append(0)
        for i in range(len(cost)-3, -1,-1): # start from second last
            cost[i] += min(cost[i+1],cost[i+2])
        return min(cost[0], cost[1])

obj = solution()
print(obj.costClimbingStairs([10, 15, 20]))
print(obj.costClimbingStairs([1, 100,1 ,1 ,1,100,1,1,100,1]))

print(obj.min_Cost_Iterative([10, 15, 20]))
print(obj.min_Cost_Iterative([1, 100,1 ,1 ,1,100,1,1,100,1]))



# for recursive memoized solution
# time -> O(N)
# space -> O(N)