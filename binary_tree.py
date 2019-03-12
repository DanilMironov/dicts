from tree_unit import TreeUnit


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if self.root is None:
            self.root = TreeUnit(key, value)
            return
        else:
            curr_node = self.root
            while True:
                if key < curr_node.key:
                    if curr_node.left is not None:
                        curr_node = curr_node.left
                    else:
                        curr_node.left = TreeUnit(key, value, curr_node)
                        break
                else:
                    if curr_node.right is not None:
                        curr_node = curr_node.right
                    else:
                        curr_node.right = TreeUnit(key, value, curr_node)
                        break

    def find(self, key):
        if self.root is None:
            return None
        else:
            curr_node = self.root
            while True:
                if key == curr_node.key:
                    return curr_node
                else:
                    if key > curr_node.key:
                        if curr_node.right is None:
                            return None
                        curr_node = curr_node.right
                    else:
                        if curr_node.left is None:
                            return None
                        curr_node = curr_node.left

    def remove(self, key):
        root = self.find(key)
        returned = root.copy()
        if root is None:
            raise Exception("This key doesn't exist")
        if root.left is None and root.right is None:
            if root.parent.left == root:
                root.parent.left = None
            else:
                root.parent.right = None
        elif root.left is not None and root.right is not None:
            if root.right.left is None:
                root.left.parent = root.right
                root.right.left = root.left
                root.right.parent = root.parent
                if root.parent.left == root:
                    root.parent.left = root.right
                else:
                    root.parent.right = root.right
            else:
                left_most_element = self._get_leftmost(root.right)
                if left_most_element.right is not None:
                    root.key = left_most_element.key
                    root.value = left_most_element.value
                    left_most_element.right.parent = left_most_element.parent
                    left_most_element.parent.left = left_most_element.right
                else:
                    root.key = left_most_element.key
                    root.value = left_most_element.value
                    left_most_element.parent.left = None
        else:
            if root.right is not None and root.left is None:
                root.right.parent = root.parent
                if root.parent.left == root:
                    root.parent.left = root.right
                else:
                    root.parent.right = root.right
            else:
                root.left.parent = root.parent
                if root.parent.left == root:
                    root.parent.left = root.left
                else:
                    root.parent.right = root.left
        return returned

    def _get_leftmost(self, root: TreeUnit):
        if root.left is None:
            return root
        else:
            return self._get_leftmost(root.left)
