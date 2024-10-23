# 199
# do bfs and add last element

import queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root):
    result = []
    if(root == None):
        return result
    q = queue.Queue()
    q.put(root)

    while not q.empty():
        levelSize = q.qsize()
        for i in range(levelSize):
            currentNode = q.get()
            if i == levelSize - 1:
                result.append(currentNode.val)
            if currentNode.left != None:
                q.put(currentNode.left)
            if currentNode.right != None:
                q.put(currentNode.right)
    return result

# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)

print(rightSideView(root))