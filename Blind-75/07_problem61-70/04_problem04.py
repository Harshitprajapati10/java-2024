# problem 64
# subtree of another tree
# LC 572

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, s, t):
        if not t: return True
        if not s: return False
        if self.sameTree(s,t):
            return True
        return (self.isSubtree(s.left, t) or
                self.isSubtree(s.right,t))
    def sameTree(self,s,t):
        if not s and not t:return True
        if s and t and s.val == t.val:
            return (self.sameTree(s.left,t.left) and
                    self.sameTree(s.right,t.right))
        return False

# Create the tree: [1,2,3,null,null,4,5]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

subRoot = TreeNode(3)
subRoot.left = TreeNode(4)
subRoot.right = TreeNode(5)


OBJ = Solution()
print(OBJ.isSubtree(root,subRoot))