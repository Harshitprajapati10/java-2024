# problem 67
# kth smallest in BST

# 230 kth smallest in BST
# In order traversal of BST

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

count = [0] 
def kthSmallest(root, k):
    if root is None:
        return None
    left = kthSmallest(root.left, k)
    if left is not None:
        return left
    count[0] += 1
    if count[0] == k:
        return root
    return kthSmallest(root.right, k)

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)

k = 3
result = kthSmallest(root, k)
print(result.val if result else None)