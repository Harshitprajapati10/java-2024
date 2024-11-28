# problem 48
# word search
# LC: 79

# given an twoD array of words tell whether word is found or not

# board = [[A, B, C, E],
#         [S, F, C, S],
#         [A, D, E, E]]
# word = ABCCED
# Dfs + backtracking

# Do dfs on every index

class Solution:
    def word_search(self, board, word):
        ROWS, COLS = len(board), len(board[0])
        path = set()
        def dfs(r,c,i):
            if i==len(word):
                return True
            if (r<0 or c<0
                 or r>=ROWS or c>=COLS
                   or board[r][c] != word[i]
                     or (r,c) in path):
                return False
            path.add((r,c))
            res = (dfs(r+1,c,i+1) or
                   dfs(r-1,c,i+1) or
                   dfs(r,c+1,i+1) or
                   dfs(r, c-1,i+1))
            path.remove((r,c))
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0): return True
        return False




def main():
    obj = Solution()
    board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    word = "ABCCED"
    print(obj.word_search(board,word))

if __name__ == "__main__":
    main()