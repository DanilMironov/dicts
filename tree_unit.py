class TreeUnit:
    def __init__(self, key, value, parent=None):
        self.right = None
        self.left = None
        self.parent = parent
        self.key = key
        self.value = value
