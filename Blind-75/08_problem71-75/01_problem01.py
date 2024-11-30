# problem 71

# word search II
# LC 212

"""
board = [
    ["o","a","a","n"],
    ["e","t","a","e"],
    ["i","h","k","r"],
    ["i","f","l","v"]
]
words = ["oath","pea","eat","rain"]
output :["eat","oath"]



create a trie to store words
check , and backtrack

board = [
    ["a","c"],
    ["p","e"]
]
words = ["app","ape","ace"]

    prefix tree -->     ()
                    a
                p       c
            p      e       e
# search in tree, and match with board i,j
"""


class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False
    def addWord(self,word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True


class Solution:
    def findWords(self, board, words):
        root = TrieNode()
        for w in words:
            root.addWord(w)
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(),set()

        def dfs(r,c,node,word):
            if (r<0 or c<0 or r==ROWS or c==COLS or (r,c) in visit or board[r][c] not in node.children):
                return
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)

            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")
        
        return list(res)
    

obj = Solution()
board = [
    ["o","a","a","n"],
    ["e","t","a","e"],
    ["i","h","k","r"],
    ["i","f","l","v"]
]
words = ["oath","pea","eat","rain"]
print(obj.findWords(board, words))

print(obj.findWords(
    board = [
    ["a","c"],
    ["p","e"]
    ],
    words = ["app","ape","ace"]
))
