class BinaryTree:
    """
    A class representing a binary tree.
    """

    class Node:
        """
        A class representing a node in the binary tree.
        
        Attributes:
        value (int): The value stored in the node.
        left (Node): The left child of the node.
        right (Node): The right child of the node.
        """
        
        def __init__(self, value):
            # Initialize a Node with a value and optional left and right children.
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        # Initialize an empty binary tree.
        self.root = None

    def populate(self):
        """
        Populate the binary tree by manually entering nodes.
        
        This function uses user input to create the binary tree.
        """
        
        value = int(input("Enter the root Node: "))
        self.root = self.Node(value)
        self._populate(self.root)

    def _populate(self, node):
        # Recursively populate the binary tree.
        
        left = input(f"Do you want to enter left of {node.value}? (yes/no): ")
        if left.lower() == "yes":
            value = int(input(f"Enter the value of the left of {node.value}: "))
            node.left = self.Node(value)
            self._populate(node.left)

        right = input(f"Do you want to enter right of {node.value}? (yes/no): ")
        if right.lower() == "yes":
            value = int(input(f"Enter the value of the right of {node.value}: "))
            node.right = self.Node(value)
            self._populate(node.right)

    def display(self):
        """
        Display the binary tree in a simple format.
        
        This function prints the tree with indentation representing depth.
        """
        
        self._display(self.root, "")

    def _display(self, node, indent):
        # Recursively display the binary tree.
        
        if node is None:
            return
        print(indent + str(node.value))
        self._display(node.left, indent + "\t")
        self._display(node.right, indent + "\t")

    def pretty_display(self):
        """
        Display the binary tree in a pretty format.
        
        This function prints the tree with lines representing relationships.
        """
        
        self._pretty_display(self.root, 0)

    def _pretty_display(self, node, level):
        # Recursively display the binary tree in a pretty format.
        
        if node is None:
            return

        self._pretty_display(node.right, level + 1)

        if level != 0:
            for _ in range(level - 1):
                print("|\t\t", end="")
            print("|------->" + str(node.value))
        else:
            print(node.value)
        self._pretty_display(node.left, level + 1)

    def pre_order(self):
        """
        Traverse the binary tree in pre-order.
        
        This function prints the values in pre-order (root, left, right).
        """
        
        self._pre_order(self.root)

    def _pre_order(self, node):
        # Recursively traverse the binary tree in pre-order.
        
        if node is None:
            return
        print(node.value, end=" ")
        self._pre_order(node.left)
        self._pre_order(node.right)

    def in_order(self):
        """
        Traverse the binary tree in in-order.
        
        This function prints the values in in-order (left, root, right).
        """
        
        self._in_order(self.root)

    def _in_order(self, node):
        # Recursively traverse the binary tree in in-order.
        
        if node is None:
            return
        self._in_order(node.left)
        print(node.value, end=" ")
        self._in_order(node.right)

    def post_order(self):
        """
        Traverse the binary tree in post-order.
        
        This function prints the values in post-order (left, right, root).
        """
        
        self._post_order(self.root)

    def _post_order(self, node):
        # Recursively traverse the binary tree in post-order.
        
        if node is None:
            return
        self._post_order(node.left)
        self._post_order(node.right)
        print(node.value, end=" ")


# Example usage:
tree = BinaryTree()
tree.populate()
print("Simple Display:")
tree.display()
print("\nPretty Display:")
tree.pretty_display()
print("\nPre-order Traversal:")
tree.pre_order()
print("\nIn-order Traversal:")
tree.in_order()
print("\nPost-order Traversal:")
tree.post_order()