# 103 -> Binary tree zigzag order traversal

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigZagorder(root):
    result = []
    if(root == None):
        return result
    q = deque()
    q.append(root)
    reverse = False

    while q:
        levelSize = len(q)
        currentLevel = []
        for i in range(levelSize):
            if not reverse:  # forward order
                currentNode = q.popleft()
                if currentNode:
                    currentLevel.append(currentNode.val)
                    if currentNode.left:
                        q.append(currentNode.left)
                    if currentNode.right:
                        q.append(currentNode.right)
            else:  # reverse order
                currentNode = q.pop()
                if currentNode:
                    currentLevel.append(currentNode.val)
                    if currentNode.right:
                        q.appendleft(currentNode.right)
                    if currentNode.left:
                        q.appendleft(currentNode.left)

        reverse = not reverse
        result.append(currentLevel)

    return result

# Create the tree: [3,9,20,null,null,15,7]
# output = [[3],[20,9],[15,7]]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(zigZagorder(root))