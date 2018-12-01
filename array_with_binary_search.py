class BinaryArray:
    def __init__(self):
        self._data = []

    def add(self, key, value):
        new_element = (key, value)
        if key in self.keys():
            self._data.sort()
            left = 0
            right = len(self._data)
            while left != right:
                middle = (left + right) // 2
                element = self._data[middle]
                if key == element[0]:
                    self._data.remove(element)
                    self._data.append(new_element)
                elif key < element[0]:
                    right = middle
                else:
                    left = middle + 1
        else:
            self._data.append(new_element)

    def get(self, key):
        self._data.sort()
        left = 0
        right = len(self._data)
        while left != right:
            middle = (left + right) // 2
            if key == self._data[middle][0]:
                return self._data[middle][1]
            elif key < self._data[middle][0]:
                right = middle
            else:
                left = middle + 1
        return None

    def values(self):
        result = []
        for element in self._data:
            result.append(element[1])
        return result

    def items(self):
        return self._data

    def keys(self):
        result = []
        for element in self._data:
            result.append(element[0])
        return result

    def pop(self, key):
        self._data.sort()
        left = 0
        right = len(self._data)
        while left != right:
            middle = (left + right) // 2
            element = self._data[middle]
            if key == element[0]:
                result = element[1]
                self._data.remove(element)
                return result
            elif key < element[0]:
                right = middle
            else:
                left = middle + 1
        raise KeyError("This key doesn't exist")

    def clear(self):
        self._data.clear()

    def copy(self):
        return self._data.copy()
