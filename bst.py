class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return

        def _insert(current, value):
            if value < current.value:
                if current.left:
                    _insert(current.left, value)
                else:
                    current.left = Node(value)

            else:
                if current.right:
                    _insert(current.right, value)
                else:
                    current.right = Node(value)

        _insert(self.root, value)

    #Завдання 1
    def find_max(self):
        if not self.root:
            return None

        current = self.root
        while current.right:
            current = current.right
        return current.value
    
    #Завдання 2
    def find_min(self):
        if not self.root:
            return None

        current = self.root
        while current.left:
            current = current.left
        return current.value
    #Завданння 3
    def sum_values(self):
        def _sum(node):
            if not node:
                return 0
            return node.value + _sum(node.left) + _sum(node.right)

        return _sum(self.root)


    