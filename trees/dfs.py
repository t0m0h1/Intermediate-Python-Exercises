from binarytree import Node
from binarytree import BinaryTree

# Description: Depth First Search implementation for a binary tree.
def depth_first_search(start, target):
    if start is None:
        return False
    if start.data == target:
        return True
    left = depth_first_search(start.left, target)
    right = depth_first_search(start.right, target)
    return left or right

tree1 = BinaryTree(1)
tree1.root.left = Node(2)
tree1.root.right = Node(3)
tree1.root.left.left = Node(4)
tree1.root.left.right = Node(5)

if __name__ == '__main__':
    print(depth_first_search(tree1.root, 5)) # True
    print(depth_first_search(tree1.root, 6)) # False
    print(depth_first_search(tree1.root, 3)) # True