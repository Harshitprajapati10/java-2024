# 114 -> using preorder traversal
#flatten BT to linked list
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root):
    current = root
    while(current != None):
        if current.left != None:
            temp = current.left
            while(temp.right != None):
                temp = temp.right
            temp.right = current.right
            current.right = current.left
            current.left = None
        current = current.right
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)

flatten(root)
for i in range(6):
    print(root.val)
    root = root.right