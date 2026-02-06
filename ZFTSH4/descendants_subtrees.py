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

def bfs_traversal(root: Optional[Node], target: int) -> list[int]:
    result = []
    if root is None:
        return result

    q = deque([root])
    target_node = None

    # Поиск узла с target
    while q:
        node = q.popleft()
        if node.key == target:
            target_node = node
            break
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    # Если узел найден, обходим его поддерево BFS
    if target_node:
        q = deque([target_node])
        while q:
            node = q.popleft()
            result.append(node.key)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return result

root = None
numbers = list(map(int,input().split()))
for key in numbers:
    root = bst_insert(root, key)

nv = int(input("Введите значение для поиска: "))
result = bfs_traversal(root, nv)
if len(result) == 0:
    print("Такого элемента в дереве нет")
else:
    print(f"Найден узел и его поддерево: {result}")