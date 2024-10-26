# 124 -> maximum path sum in binary tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.ans = -2**31   #Min value of a integer

    def maxPathSum(self,root):
        self.helper(root)
        return self.ans
    
    def helper(self,node):
        if node is None: return 0
        left = self.helper(node.left)
        right = self.helper(node.right)
        left = max(0,left)
        right = max(0,right)
        pathSum = left + right + node.val
        self.ans = max(self.ans,pathSum)
        return max(left,right) + node.val

root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

obj = Solution()
obj.maxPathSum(root)
print(obj.ans)