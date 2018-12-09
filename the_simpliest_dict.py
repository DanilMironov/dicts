class LinearArray:
    def __init__(self):
        self._data = []

    def add(self, key, value):
        new_element = (key, value)
        if key in self.keys():
            for element in self._data:
                if element[0] == key:
                    self._data.remove(element)
                    self._data.append(new_element)
        else:
            self._data.append(new_element)

    def get(self, key):
        for element in self._data:
            if key == element[0]:
                return element[1]
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
        for i in range(0, len(self._data)):
            element = self._data[i]
            if element[0] == key:
                result = element[1]
                self._data.remove(element)
                return result
        raise KeyError("This key doesn't exist")

    def clear(self):
        self._data.clear()

    def copy(self):
        dic = LinearArray()
        dic._data = self._data.copy()
        return dic
