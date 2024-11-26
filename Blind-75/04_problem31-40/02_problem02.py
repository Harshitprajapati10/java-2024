# problem 32
# Graph Valid Tree
# LC 178

# given a graph return true or false if it is a valid tree or not

# n = 5 
# edges = [[0,1],[0,2],[0,3],[1,4]]
# True if its a tree
#  -- All nodes are connected
#  -- No cycle is present

class Solution:
    def validTree(self, n, edges):
        if not n: return True
        adj = {i:[] for i in range(n)}
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(i, prev):
            if i in visit:
                return False
            visit.add(i)
            for j in adj[i]:
                if j==prev:
                    continue
                if not dfs(j,i):
                    return False
            return True
        
        return dfs(0,-1) and n==len(visit) # condition for a valid tree

obj = Solution()
edges = [[0,1],[0,2],[0,3],[1,4]]
n = 5
print(obj.validTree(n, edges)) # True
print(obj.validTree(5, [[0,1],[0,2],[0,3],[1,4],[4,0]])) # False
