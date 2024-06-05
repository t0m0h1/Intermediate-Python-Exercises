from binarytree import Node
from binarytree import BinaryTree

# Description: Depth First Search implementation for a binary tree.
def depth_first_search(self, start, target):
    if start is None:
        return False
    if start.data == target:
        return True
    left = self.depth_first_search(start.left, target)
    right = self.depth_first_search(start.right, target)
    return left or right

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

if __name__ == '__main__':
    print(depth_first_search(tree, tree.root, 5)) # True
    print(depth_first_search(tree, tree.root, 6)) # False
    print(depth_first_search(tree, tree.root, 3)) # True