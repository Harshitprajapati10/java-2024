# N-queens

class Solution:
    def N_queens(self,n):
        col = set()
        posDiag = set() # r+c constant
        negDiag = set() # r-c constant

        res = []
        board = [["."]*n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"
                backtrack(r+1)
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
        backtrack(0)
        return res

obj = Solution()
answer = obj.N_queens(5)

for i in answer:
    for j in i:
        for k in j:
            print(k,end=" ")
        print()
    print()

