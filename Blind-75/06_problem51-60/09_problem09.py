# problem 59
# same tree
# LC 100

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def SameTree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False

    return (SameTree(p.left,q.left) and
            SameTree(p.right,q.right))