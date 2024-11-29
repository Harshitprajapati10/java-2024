# Problem 61
# max path sum in a binary Tree
# LC 124

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root):
    res = [root.val]
    def dfs(node):
        if not node:
            return 0
        leftMax = dfs(node.left)
        rightMax = dfs(node.right)
        leftMax = max(leftMax,0)
        rightMax = max(rightMax,0)
        res[0] = max(res[0], leftMax+rightMax+node.val)
        return node.val + max(leftMax,rightMax)
    dfs(root)
    return res[0]



root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)

print(maxPathSum(root))

"""
     4
    2  7
  1  3 6   -->22
"""