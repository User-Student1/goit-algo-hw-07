from bst import BinarySearchTree

tree = BinarySearchTree()
values = [15, 10, 20, 8, 12, 17, 25]

for v in values:
    tree.insert(v)

print("Maximum value in BST:", tree.find_max())
print("Minimum value in BST:", tree.find_min())
print("Sum of all values in BST:", tree.sum_values())