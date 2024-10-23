# 637
"""
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
 
"""

# 102 -> Binary tree level order traversal

import queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def averageOfLevels(root):
    result = []
    if(root == None):
        return result
    q = queue.Queue()
    q.put(root)

    while not q.empty():
        levelSize = q.qsize()
        currentAvg = 0
        for i in range(levelSize):
            currentNode = q.get()
            currentAvg += currentNode.val
            if currentNode.left != None:
                q.put(currentNode.left)
            if currentNode.right != None:
                q.put(currentNode.right)
        currentAvg = currentAvg/levelSize
        result.append(currentAvg)

    return result

# Create the tree: [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(averageOfLevels(root))