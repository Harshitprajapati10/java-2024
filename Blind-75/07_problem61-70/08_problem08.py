# problem 68
#LCA of BST

# 235

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def LCA(root, p, q):
    cur = root
    while cur:
        if p.val>cur.val and q.val>cur.val:
            cur = cur.right
        elif p.val<cur.val and q.val<cur.val:
            cur = cur.left
        else:
            return cur

root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

"""
        3
    5       1
  6   2    0  8
     7  4
"""


print(LCA(root, root.left, root.right).val)