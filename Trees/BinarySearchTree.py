# Python Implementation of Binary Search Tree

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if not self.root:
            self.root = Node(data)
            print(f"Inserted {data} as root")
        else:
            self.insert_recursive(self.root,data)
            print(f"Inserted {data}")

    def insert_recursive(self,root,data):
        if data < root.data:
            if root.left == None:
                root.left = Node(data)
            else:
                self.insert_recursive(root.left,data)
        elif data > root.data:
            if root.right == None:
                root.right = Node(data)
            else:
                self.insert_recursive(root.right,data)

    def search(self,root,data):
        if not root:
            print(f"{data} not Found")
        else:
            self.search_recursive(root,data)

    def search_recursive(self,root,data):
        if root is None:
            print(f"{data} not found in BT")
        elif root.data == data:
            print(f"{data} found in BT")
        elif root.data < data:
            self.search_recursive(root.right,data)
        elif root.data > data:
            self.search_recursive(root.left,data)

    def inorder_traversal(self,root):
        res = []
        if self.root:
            self.recursive_inorder(root,res)
            return res
        else:
            print("No Nodes in the BT")


    def recursive_inorder(self,root,res):
       if root:
            self.recursive_inorder(root.left,res)
            res.append(root.data)
            self.recursive_inorder(root.right,res)

    def preorder_traversal(self,root):
        res = []
        if self.root:
            self.recursive_preorder(root,res)
            return res
        else:
            print("No Nodes in the BT")


    def recursive_preorder(self,root,res):
       if root:
            self.recursive_preorder(root.left,res)
            self.recursive_preorder(root.right,res)
            res.append(root.data)

    def postorder_traversal(self,root):
        res = []
        if self.root:
            self.recursive_postorder(root,res)
            return res
        else:
            print("No Nodes in the BT")


    def recursive_postorder(self,root,res):
       if root:
            res.append(root.data)
            self.recursive_postorder(root.left,res)
            self.recursive_postorder(root.right,res)

    def delete_node(self,root, key):
        if root is None:
            return root

        if key < root.data:
            root.left = self.delete_node(root.left, key)
        elif key > root.data:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.find_min(root.right)
            root.data = temp.data
            root.right = self.delete_node(root.right, temp.data)
        return root

    def find_min(self,node):
        current = node
        while current.right is not None:
            current = current.right
        return current

if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(20)
    tree.insert(3)
    tree.insert(50)
    tree.insert(1)
    tree.search(tree.root,70)
    print(tree.inorder_traversal(tree.root))
    print(tree.preorder_traversal(tree.root))
    print(tree.postorder_traversal(tree.root))
    tree.delete_node(tree.root,40)
    print(tree.inorder_traversal(tree.root))