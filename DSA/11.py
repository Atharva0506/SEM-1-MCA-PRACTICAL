# 11.	Write a program to create Binary search tree and traverse it using recursive preorder, inorder, postorder methods

# Node class for Binary Search Tree (BST)
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

# BST class to handle insertion and traversal
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a new node in the BST
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursively(self.root, key)

    # Helper function for recursive insertion
    def _insert_recursively(self, node, key):
        if key < node.data:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursively(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursively(node.right, key)

    # Preorder Traversal (Root, Left, Right)
    def preorder(self):
        print("Preorder Traversal: ", end="")
        self._preorder_recursively(self.root)
        print()

    # Helper function for recursive preorder traversal
    def _preorder_recursively(self, node):
        if node:
            print(node.data, end=" -> ")
            self._preorder_recursively(node.left)
            self._preorder_recursively(node.right)

    # Inorder Traversal (Left, Root, Right)
    def inorder(self):
        print("Inorder Traversal: ", end="")
        self._inorder_recursively(self.root)
        print()

    # Helper function for recursive inorder traversal
    def _inorder_recursively(self, node):
        if node:
            self._inorder_recursively(node.left)
            print(node.data, end=" -> ")
            self._inorder_recursively(node.right)

    # Postorder Traversal (Left, Right, Root)
    def postorder(self):
        print("Postorder Traversal: ", end="")
        self._postorder_recursively(self.root)
        print()

    # Helper function for recursive postorder traversal
    def _postorder_recursively(self, node):
        if node:
            self._postorder_recursively(node.left)
            self._postorder_recursively(node.right)
            print(node.data, end=" -> ")

# Main function to test the BinarySearchTree class
def main():
    bst = BinarySearchTree()
    
    # Insert elements into the BST
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    # Perform traversals
    bst.preorder()  # Output: Preorder Traversal
    bst.inorder()   # Output: Inorder Traversal
    bst.postorder() # Output: Postorder Traversal


main()
