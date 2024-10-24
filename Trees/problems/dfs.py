# 543 -> diameter of BT
# use post order traversal
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

diameter = 0
def diameterofBT(root):
    height(root)
    return diameter

def height(node):
    global diameter
    if node is None:
        return 0  
    leftHeight = height(node.left)
    rightHeight = height(node.right)
    diameter = max(diameter, leftHeight + rightHeight)
    return max(leftHeight, rightHeight) + 1


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(diameterofBT(root))
# print(diameter)