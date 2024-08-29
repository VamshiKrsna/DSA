from BinarySearchTree import *

tree = BinarySearchTree()

print(tree)

tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(0)
tree.insert(1)

print(tree.inorder_traversal(tree.root))
