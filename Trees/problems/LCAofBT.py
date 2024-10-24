# 236 -> lowest common ancestors of binary Tree
# pending to submit 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def LCA(root, p, q):
    if root is None:
        return None
    if root == p or root == q:
        return root
    left = LCA(root.left, p ,q)
    right = LCA(root.right, p ,q)
    if (left is not None) and (right is not None):
        return root
    return right if left is None else left

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

print(LCA(root, root.left, root.right.right).val)