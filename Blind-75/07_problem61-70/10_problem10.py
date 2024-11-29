# problem 70
# Design add and search word Data structure

# 211
# create, insert, search Trie

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self,word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True
    
    def search(self,word):

        def dfs(j,root):
            cur = root
            for i in range(j,len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        
        return dfs(0,self.root)
    
obj = WordDictionary()
obj.addWord("apple")
print(obj.search(".pple"))
print(obj.search(".pp.."))
print(obj.search("...le"))
print(obj.search("apple"))
print(obj.search("....."))
print(obj.search("abpl."))