from typing import Optional, List

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

def find_node(root: Optional[Node], key: int) -> Optional[Node]:

    current = root
    while current and current.key != key:
        if key < current.key:
            current = current.left
        else:
            current = current.right
    return current


def get_all_descendants(node: Optional[Node]) -> List[int]:
    if node is None:
        return []

    result = []
    stack = [node]

    while stack:
        current = stack.pop()
        if current != node:
            result.append(current.key)

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return result


def get_common_descendants(root: Optional[Node], val1: int, val2: int) -> List[int]:
    node1 = find_node(root, val1)
    node2 = find_node(root, val2)

    if node1 is None or node2 is None:
        return []

    descendants1 = set(get_all_descendants(node1))
    descendants2 = set(get_all_descendants(node2))


    is_val2_descendant_of_val1 = find_node(node1, val2) is not None
    is_val1_descendant_of_val2 = find_node(node2, val1) is not None

    if is_val2_descendant_of_val1:

        return sorted(list(descendants2.union({val2})))
    elif is_val1_descendant_of_val2:

        return sorted(list(descendants1.union({val1})))


    common = descendants1.intersection(descendants2)
    return sorted(list(common))

root = None
numbers = list(map(int,input().split()))
val1, val2 = map(int, input().split())
for key in numbers:
    root = bst_insert(root, key)





common_descendants = get_common_descendants(root, val1, val2)


if common_descendants:
    print(' '.join(map(str, common_descendants)))
else:
    print(0)


