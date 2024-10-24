# 98 -> validate binary search tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root):
    return helper(root, None, None)
def helper(node, low, high):
    if node is None:
        return True
    if low is not None and node.val <= low:  
        return False
    if high is not None and node.val >= high:
        return False
    leftTree = helper(node.left, low, node.val)
    rightTree = helper(node.right, node.val, high)
    return leftTree and rightTree

root = TreeNode(6)
root.left = TreeNode(4)
root.right = TreeNode(10)
root.left.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right.left = TreeNode(8)
root.right.right = TreeNode(20)
root.right.right.right = TreeNode(31)


print(isValidBST(root))