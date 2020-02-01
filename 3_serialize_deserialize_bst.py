# Given the root to a binary tree, implement serialize(root),
# which serializes the tree into a string, and deserialize(s),
# which deserializes the string back into the tree.


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deserialize_left(s):
    current_element = s.partition('|')[0]
    next_element = s.partition('|')[2]
    if current_element is '':
        return None
    n = Node(current_element)
    # skip 1
    next_element = next_element.partition('|')[2]
    current_element = next_element.partition('|')[0]
    next_element = next_element.partition('|')[2]
    n.left = deserialize(current_element)
    n.right = deserialize(next_element.partition('|')[0])
    return n

def deserialize_right(s):
    current_element = s.partition('|')[0]
    next_element = s.partition('|')[2]
    if current_element is '':
        return None
    n = Node(current_element)
    # skip 2
    next_element = next_element.partition('|')[2]
    next_element = next_element.partition('|')[2]
    current_element = next_element.partition('|')[0]
    next_element = next_element.partition('|')[2]
    n.left = deserialize(current_element)
    n.right = deserialize(next_element.partition('|')[0])
    return n


def deserialize(s):
    current_element = s.partition('|')[0]
    next_element = s.partition('|')[2]
    if current_element is '':
        return None
    n = Node(current_element)
    next_element = next_element.partition('|')[2]
    n.left = deserialize_left(next_element)
    n.right = deserialize_right(next_element.partition('|')[2])
    return n


def serialize(root):
    serialization_string = ""
    if root is None:
        return ""
    else:
        serialization_string = serialization_string + root.val + "|"
        serialization_string = serialization_string + serialize(root.left) + "|"
        serialization_string = serialization_string + serialize(root.right) + "|"

    return serialization_string


def main():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'


if __name__ == "__main__":
    main()
