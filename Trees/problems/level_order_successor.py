# level order successor

#         3
#        /  \
#       /    \
#      /      \
#     /        \
#     4          8
#    /  \       /  \
# 12     14    7    11
#       /  \        /
#     36    9      2
#                   \
#                    44 

"""
input : 14, out: 7
input : 11, out :36
"""

import queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findSuccessor(root, key):
    if(root == None):
        return None
    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()
        if currentNode.left != None:
            q.put(currentNode.left)
        if currentNode.right != None:
            q.put(currentNode.right)
        if currentNode.val == key:
            break
    return q.get()

root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(12)
root.left.right = TreeNode(14)
root.right.left = TreeNode(7)
root.right.right = TreeNode(11)
root.left.right.left = TreeNode(36)
root.left.right.right = TreeNode(9)
root.right.left.left = TreeNode(2)
root.left.right.right.right = TreeNode(44)

print(findSuccessor(root, 14).val)
print(findSuccessor(root, 11).val)