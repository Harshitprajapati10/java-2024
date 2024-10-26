# 129 -> Sum root to leaf numbers

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class solution:
    def sumNumbers(self, root):
        return self.helper(root, 0)
    def helper(self, node, sumNumbers):
        if node is None:
            return 0
        sumNumbers = sumNumbers * 10 + node.val
        if node.left == None and node.right == None: # condition of leaf node
            return sumNumbers
        return self.helper(node.left,sumNumbers) + self.helper(node.right, sumNumbers)



root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(0)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)

obj = solution()
print(obj.sumNumbers(root))