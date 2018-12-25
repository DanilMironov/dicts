class BalancedTreeUnit:
    def __init__(self, key, value, parent=None):
        self.right = None
        self.left = None
        self.parent = parent
        self.key = key
        self.value = value
        self.height = 1

    def copy(self):
        unit = BalancedTreeUnit(self.key, self.value)
        unit.right = self.right
        unit.left = self.left
        unit.parent = self.parent
        return unit
