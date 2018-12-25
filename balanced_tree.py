from balanced_tree_unit import BalancedTreeUnit


class BalancedTree:
    def __init__(self):
        self.tree_root = None

    def insert(self, key, value):
        if self.tree_root is None:
            self.tree_root = BalancedTreeUnit(key, value)
            return
        else:
            curr_node = self.tree_root
            while True:
                if key < curr_node.key:
                    if curr_node.left is not None:
                        curr_node = curr_node.left
                    else:
                        curr_node.left = BalancedTreeUnit(key,
                                                          value,
                                                          curr_node)
                        inserted = curr_node.left
                        break
                else:
                    if curr_node.right is not None:
                        curr_node = curr_node.right
                    else:
                        curr_node.right = BalancedTreeUnit(key,
                                                           value,
                                                           curr_node)
                        inserted = curr_node.right
                        break
        while inserted.parent is not None and \
                inserted.height == inserted.parent.height:
            inserted.parent.height += 1
            self._balance(inserted)
            inserted = inserted.parent
        self._balance(self.tree_root)

    def find(self, key):
        if self.tree_root is None:
            return None
        else:
            curr_node = self.tree_root
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
        left_subtree = root.left
        right_subtree = root.right
        curr_root = None
        if left_subtree is None and right_subtree is None:
            curr_root = root.parent
            if root.parent.left == root:
                root.parent.left = None
            else:
                root.parent.right = None
        if right_subtree is None and left_subtree is not None:
            curr_root = root.parent
            left_subtree.parent = root.parent
            if root.parent.left == root:
                root.parent.left = left_subtree
            else:
                root.parent.right = left_subtree
        if right_subtree is not None:
            min_right_unit = self._find_min(right_subtree)
            curr_root = min_right_unit.parent
            self._remove_min(min_right_unit)
            min_right_unit.parent = root.parent
            min_right_unit.left = left_subtree
            if right_subtree == min_right_unit:
                min_right_unit.right = None
            else:
                min_right_unit.right = right_subtree
                right_subtree.parent = min_right_unit
            left_subtree.parent = min_right_unit
            if root.parent.left == root:
                root.parent.left = min_right_unit
            else:
                root.parent.right = min_right_unit
        while curr_root is not None:
            self._balance(curr_root)
            curr_root = curr_root.parent
        return returned

    @staticmethod
    def _remove_min(root: BalancedTreeUnit):
        if root.right is None:
            if root.parent.left == root:
                root.parent.left = None
            else:
                root.parent.right = None
        else:
            root.right.parent = root.parent
            root.parent.left = root.right

    def _find_min(self, root: BalancedTreeUnit):
        if root.left is None:
            return root
        else:
            return self._find_min(root.left)

    @staticmethod
    def _get_height_value(root: BalancedTreeUnit):
        if root is not None:
            return root.height
        return 0

    def _calculate_height(self, root: BalancedTreeUnit):
        left_height = self._get_height_value(root.left)
        right_height = self._get_height_value(root.right)
        root.height = max(left_height, right_height) + 1

    @staticmethod
    def _get_height_difference(root: BalancedTreeUnit):
        if root.right is not None:
            right_height = root.right.height
        else:
            right_height = 0
        if root.left is not None:
            left_height = root.left.height
        else:
            left_height = 0
        return right_height - left_height

    def _balance(self, root):
        self._calculate_height(root)
        if self._get_height_difference(root) == 2:
            if self._get_height_difference(root.right) < 0:
                root.right = self._turn_right(root.right)
            self._turn_left(root)
        if self._get_height_difference(root) == -2:
            if self._get_height_difference(root.left) > 0:
                root.left = self._turn_left(root.left)
            self._turn_right(root)

    def _turn_left(self, root: BalancedTreeUnit):
        right_subtree = root.right
        root.right = right_subtree.left
        if right_subtree.left is not None:
            right_subtree.left.parent = root
        right_subtree.left = root
        if root.parent is not None:
            if root == root.parent.left:
                root.parent.left = right_subtree
            else:
                root.parent.right = right_subtree
        else:
            self.tree_root = right_subtree
        right_subtree.parent = root.parent
        root.parent = right_subtree
        self._calculate_height(root)
        self._calculate_height(right_subtree)
        return right_subtree

    def _turn_right(self, root: BalancedTreeUnit):
        left_subtree = root.left
        root.left = left_subtree.right
        if left_subtree.right is not None:
            left_subtree.right.parent = root
        left_subtree.right = root
        if root.parent is not None:
            if root == root.parent.left:
                root.parent.left = left_subtree
            else:
                root.parent.right = left_subtree
        else:
            self.tree_root = left_subtree
        left_subtree.parent = root.parent
        root.parent = left_subtree
        self._calculate_height(root)
        self._calculate_height(left_subtree)
        return left_subtree
