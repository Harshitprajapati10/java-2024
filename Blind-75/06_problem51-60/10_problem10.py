# problem 60
# Invert binary Tree
# LC 226

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if root is None:
        return None
    left = invertTree(root.left)
    right = invertTree(root.right)
    root.left = right
    root.right = left
    return root

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(7)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

invertTree(root)
print(
    root.val,
    root.left.val,
    root.right.val,
    root.left.left.val,
    root.left.right.val,
    root.right.val,
    root.right.left.val,
    root.right.right.val,
)