# 112 -> path sum of BT

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root, sum1):
    if root is None:
        return False    
    if root.val == sum1 and root.left == None and root.right == None:
        return True
    return hasPathSum(root.left, sum1 - root.val) or hasPathSum(root.right, sum1-root.val)


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

print(hasPathSum(root,22))