class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)


    

if __name__ == '__main__':
    # make a tree
    tree = BinaryTree(1) # root value is 1
    tree.root.left = Node(2) # left child of root is 2
    tree.root.right = Node(3) # right child of root is 3

