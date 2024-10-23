# 101 - symmetric tree

import queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root):
    q = queue.Queue()
    q.put(root.left)
    q.put(root.right)

    while not q.empty():
        left = q.get()
        right = q.get()
        if left == None and right == None: continue
        if left == None or right == None: return False
        if left.val != right.val: return False
        q.put(left.left)
        q.put(right.right)
        q.put(left.right)
        q.put(right.left)
    return True



# Create the tree root = [1,2,2,3,4,4,3]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right =  TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(isSymmetric(root))