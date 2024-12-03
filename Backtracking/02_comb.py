# combinations, LC 77

def combine(n,k):
    res = []
    def dfs(start,comb):
        if len(comb) == k:
            res.append(comb.copy())
            return
        for i in range(start, n+1):
            comb.append(i)
            dfs(i+1, comb)
            comb.pop()
    dfs(1,[])
    return res

print(combine(4,2))