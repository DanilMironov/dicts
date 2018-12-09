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
        # if root is None:
        #     return None
        # if key < root.key:
        #     self.remove(root.left, key)
        # elif key > root.key:
        #     self.remove(root.right, key)
        root = self.find(key)
        if root.left is None and root.right is None:  # если удаляемый элемент это лист
            if root.parent.left == root:
                root.parent.left = None
            else:
                root.parent.right = None  # тут все хорошо
        elif root.left is not None and root.right is not None:  # если существуют оба поддерева
            if root.right.left is None:  # взяли правый и поставили его на место удаляемого
                root.left.parent = root.right
                root.right.left = root.left
                root.right.parent = root.parent
                if root.parent.left == root:
                    root.parent.left = root.right
                else:
                    root.parent.right = root.right  # вот тут теперь все в порядке
            else:
                left_most_element = self.get_leftmost(root.right)  # нашли самый левый
                                                                   # и изменил поля root
                if left_most_element.right is not None:
                    root.key = left_most_element.key
                    root.value = left_most_element.value
                    left_most_element.right.parent = left_most_element.parent
                    left_most_element.parent.left = left_most_element.right  # вроде норм
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

    def get_leftmost(self, root: TreeUnit):
        if root.left is None:
            return root
        else:
            return self.get_leftmost(root.left)
