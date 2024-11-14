# leetcode 1143 -> Longest common subsequence
# Return common subsequence of two strings

# example : text1 = "abcde"
# text2 = "ace"
# ans : 3, ace is longest subsequence common in both


# WAY ->
# if character matches , go diagonally
# if not matches, go right and down , and add max(right, down)
# bottom up approach 

"""
text1 = "abcde"
text2 = "abe"
creating 6X4 grid

       a   b   e   ''
a   [  0   0   0   0  ]
b   [  0   0   0   0  ]
c   [  0   0   0   0  ]
d   [  0   0   0   0  ]
e   [  0   0   0   0  ]
''  [  0   0   0   0  ]


       a   b   e   ''
a   [  3   2   1   0  ]
b   [  2   2   1   0  ]
c   [  1   1   1   0  ]
d   [  1   1   1   0  ]
e   [  1   1   1   0  ]
''  [  0   0   0   0  ]

 *) if matches, then get max(right, down) + 1
 *) if not matches, then get max(right, down)
 *) return grid[0][0]
 
       a   b   r   ''
a   [  2   1   0   0  ]
b   [  1   1   0   0  ]
c   [  0   0   0   0  ]
d   [  0   0   0   0  ]
e   [  0   0   0   0  ]
''  [  0   0   0   0  ]
"""

class Solution:
    def LCS(self,text1,text2):
        grid = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1 , -1 ,-1):
                if text1[i] == text2[j]: grid[i][j]  = grid[i+1][j+1] + 1
                else: grid[i][j]  = max(grid[i+1][j], grid[i][j+1])
        return grid[0][0]

obj = Solution()
print(obj.LCS("abcde","abe"))
print(obj.LCS("abcde","pqr"))
print(obj.LCS("harshit","stark"))
print(obj.LCS("harshit","harshit"))