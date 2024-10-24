class BST:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            self.height = 0

        def get_value(self):
            return self.value

    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return -1
        return node.height

    def is_empty(self):
        return self.root is None

    def insert(self, value):
        self.root = self._insert(value, self.root)

    def _insert(self, value, node):
        if node is None:
            node = self.Node(value)
            return node

        if value < node.value:
            node.left = self._insert(value, node.left)
        elif value > node.value:
            node.right = self._insert(value, node.right)

        node.height = max(self.height(node.left), self.height(node.right)) + 1
        return node

    def populate(self, nums):
        for num in nums:
            self.insert(num)

    def populate_sorted(self, nums):
        self._populate_sorted(nums, 0, len(nums))

    def _populate_sorted(self, nums, start, end):
        if start >= end:
            return
        mid = (start + end) // 2
        self.insert(nums[mid])
        self._populate_sorted(nums, start, mid)
        self._populate_sorted(nums, mid + 1, end)

    def balanced(self):
        return self._balanced(self.root)

    def _balanced(self, node):
        if node is None:
            return True
        return abs(self.height(node.left) - self.height(node.right)) <= 1 and self._balanced(node.left) and self._balanced(node.right)

    def display(self):
        self._display(self.root, "Root Node: ")

    def _display(self, node, details):
        if node is None:
            return
        print(details + str(node.value))
        self._display(node.left, "Left child of " + str(node.value) + ": ")
        self._display(node.right, "Right child of " + str(node.value) + ": ")


# Example of using the BST
bst = BST()
bst.populate([10, 20, 5, 6, 15, 30])
bst.display()

print("Is the tree balanced?", bst.balanced())

sorted_list = [1, 2, 3, 4, 5, 6, 7]
bst.populate_sorted(sorted_list)
bst.display()

print("Is the tree balanced after populating sorted list?", bst.balanced())
