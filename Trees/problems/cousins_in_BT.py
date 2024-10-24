# 993 -cousins in BT

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isCousins(root, x, y):
    xx = findNode(root, x)
    yy = findNode(root, y)
    return (
        (level(root, xx, 0) == level(root, yy ,0)) and (not isSibling(root, xx, yy))
    )

def findNode(node, x):
    if node == None:
        return None
    if node.val == x:
        return node
    n = findNode(node.left, x)
    if n != None:
        return n
    return findNode(node.right, x)

def isSibling(node,x,y):
    if node == None:
        return False
    return (
        (node.left == x and node.right == y) or
        (node.left == y and node.right == x) or
        isSibling(node.left, x, y) or
        isSibling(node.right,x ,y)
    )

def level(node, x, lev):
    if node == None:
        return 0
    if node == x:
        return lev
    l = level(node.left, x, lev+1)
    if l!=0:
        return l
    return level(node.right, x,lev+1)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)

print(isCousins(root, 4,5))
print(isCousins(root, 4,3))