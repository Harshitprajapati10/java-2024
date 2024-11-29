# problem 65
# construct BT from preorder and inorder traversal

#LC 105

# 105 -> create binary tree from preorder and inorder traversal

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preOrder,inOrder):
    if len(preOrder) == 0:
        return None
    r = preOrder[0]
    index = 0
    for i in range(len(inOrder)):
        if inOrder[i] == r:
            index = i
    node = TreeNode(r)
    node.left = buildTree(preOrder[1:index+1], inOrder[0:index])
    node.right = buildTree(preOrder[index+1:], inOrder[index+1:])
    return node

preOrder = [3, 9, 20,15,7]
InOrder = [9, 3,15,20,7]



root = buildTree(preOrder, InOrder)
print(root.val)