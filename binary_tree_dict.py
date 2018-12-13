from collections import deque
from binary_tree import BinaryTree


class TreeDict:
    def __init__(self):
        self._tree = BinaryTree()

    def add(self, key, value):
        self._tree.insert(key, value)

    def get(self, key):
        return self._tree.find(key).value

    def items(self):
        units = deque()
        items = []
        units.append(self._tree.root)
        while True:
            try:
                unit = units.popleft()
                items.append((unit.key, unit.value))
                if unit.right is not None:
                    units.append(unit.right)
                if unit.left is not None:
                    units.append(unit.left)
            except IndexError:
                return items

    def values(self):
        units = deque()
        values = []
        units.append(self._tree.root)
        while True:
            try:
                unit = units.popleft()
                values.append(unit.value)
                if unit.right is not None:
                    units.append(unit.right)
                if unit.left is not None:
                    units.append(unit.left)
            except IndexError:
                return values

    def keys(self):
        units = deque()
        keys = []
        units.append(self._tree.root)
        while True:
            try:
                unit = units.popleft()
                keys.append(unit.key)
                if unit.right is not None:
                    units.append(unit.right)
                if unit.left is not None:
                    units.append(unit.left)
            except IndexError:
                return keys

    def pop(self, key):
        return self._tree.remove(key).value
