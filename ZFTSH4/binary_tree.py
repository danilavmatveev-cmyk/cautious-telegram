from collections import deque
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

def bfs_traversal(root: Optional[Node]) -> None:
    if root is None:
        return

    q: deque[Node] = deque([root])
    while q:
        node = q.popleft()
        print(node.key, end=' ')
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

root: Optional[Node] = None


numbers = list(map(int,input().split()))

for key in numbers:
    root = bst_insert(root, key)




print(bintree_height(root)-1)