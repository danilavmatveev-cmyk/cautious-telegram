from typing import Optional

class Node:
    def __init__(self, key: int):
        self.key = key
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None

def bst_insert(root: Optional[Node], key: int) -> Node:
    if root is None:
        return Node(key)

    if key != root.key:
        if key < root.key:
            root.left = bst_insert(root.left, key)
        else:
            root.right = bst_insert(root.right, key)

    return root

def bintree_height(root: Optional[Node]) -> int:
    if root is None:
        return 0
    left_h = bintree_height(root.left)
    right_h = bintree_height(root.right)
    return max(left_h, right_h) + 1

root: Optional[Node] = None
numbers = [8,4,2,1,3,12,10,9,11,14,13,15]

for key in numbers:
    root = bst_insert(root, key)



print(bintree_height(root)-1)