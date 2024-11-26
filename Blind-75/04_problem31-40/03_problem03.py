# Problem 33
# NO of connected components in a Undirected graph
# LC 323, (premium)

# n = 5, edges = [[0,1],[1,2],[3,4]]
# ans = 2 connected components

"""Union Find Algorithm """

# 0  1   2   3   4
# parent = [0,1,2,3,4]
# rank = [1,1,1,1,1] ,  # total_disconnected_components = 5 -> initially

# 0 <-- 1  2  3  4
# parent = [0,0,2,3,4]
# rank = [2,1,1,1,1] ,total_disconnected_components = 5 -1 = 4

# 0 <-- 1   3  4
# |
# <---2
# parent = [0,0,0,3,4]
# rank = [3,1,1,1,1] ,total_disconnected_components = 4 -1 = 3

# 0 <-- 1   3 <-- 4
# |
# <---2
# parent = [0,0,0,3,3]
# rank = [3,1,1,2,1] ,total_disconnected_components = 3 -1 = 2

class Solution:
    def countComponent(self,n, edges):
        par = [i for i in range(n)]
        rank = [1]*n

        def find(n1):
            res = n1
            while res!=par[res]:
                par[res]=par[par[res]]
                res = par[res]
            return res
        
        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if p1==p2:
                return 0
            if rank[p2]>rank[p1]:
                par[p1]=p2
                rank[p2]+=rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1

        res = n
        for n1,n2 in edges:
            res -= union(n1,n2)
        return res

obj = Solution()
n = 5
edges = [[0,1],[1,2],[3,4]]
print(obj.countComponent(n,edges)) #2
