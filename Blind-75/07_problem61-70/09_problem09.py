# problem 69

# Implement Trie
# prefix tree

# lC : 208
# insert , search, startswith
# trie is efficient data structure to search and startswith 

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
    def search(self,word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord
    def startsWith(self,prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
    
obj = Trie()
obj.insert("apple")
print(obj.search("apple"))   #T
print(obj.search("app"))     #F
print(obj.startsWith("app")) #T
print(obj.startsWith("qpp")) #F