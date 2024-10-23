# 102 -> Binary tree level order traversal

import queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    result = []
    if(root == None):
        return result
    q = queue.Queue()
    q.put(root)

    while not q.empty():
        levelSize = q.qsize()
        currentLevel = []
        for i in range(levelSize):
            currentNode = q.get()
            currentLevel.append(currentNode.val)
            if currentNode.left != None:
                q.put(currentNode.left)
            if currentNode.right != None:
                q.put(currentNode.right)
        result.append(currentLevel)

    # return result[::-1]
    return result

# Create the tree: [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(levelOrder(root))