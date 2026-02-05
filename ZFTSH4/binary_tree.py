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
        return 0,0

    q: deque[Node] = deque([root])
    while q:
        node = q.popleft()
        print(node.key, end=' ')
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


def find_min_max_with_bfs(root: Optional[Node]) -> tuple[int, int]:

    if root is None:
        return

    min_val = root.key
    max_val = root.key

    queue = deque([root])

    while queue:
        node = queue.popleft()


        if node.key < min_val:
            min_val = node.key
        if node.key > max_val:
            max_val = node.key


        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return min_val, max_val

root: Optional[Node] = None


numbers = list(map(int,input().split()))

for key in numbers:
    root = bst_insert(root, key)


if root:
    min_val, max_val = find_min_max_with_bfs(root)
    print(min_val + max_val)
else:
    print(0)

