class HashTableDict:
    def __init__(self):
        self.hash_table = []
        self.degree_of_occupancy = 0
        for i in range(16):
            self.hash_table.append([])
        self.size_of_table = 16

    def _enlarge(self):
        self.size_of_table = self.size_of_table * 2
        enlarged_table = []
        for i in range(self.size_of_table):
            enlarged_table.append([])
        for element in self.hash_table:
            if len(element) != 0:
                for sub_element in element:
                    index = sub_element[2] & (self.size_of_table - 1)
                    enlarged_table[index].append(sub_element)
        self.hash_table = enlarged_table

    def add(self, key, value):
        if self.degree_of_occupancy > (2 / 3) * self.size_of_table:
            self._enlarge()
        hash_of_key = hash(key)
        index = hash_of_key & (self.size_of_table - 1)
        self.hash_table[index].append((key, value, hash_of_key))
        self.degree_of_occupancy += 1

    def get(self, key):
        hash_of_key = hash(key)
        index = hash_of_key & (self.size_of_table - 1)
        if len(self.hash_table[index]) == 0:
            return
        for element in self.hash_table[index]:
            if element[2] == hash_of_key:
                if element[0] == key:
                    return element[1]

    def items(self):
        result = []
        for element in self.hash_table:
            if len(element) != 0:
                for sub_element in element:
                    result.append((sub_element[0], sub_element[1]))
        return result

    def keys(self):
        result = []
        for element in self.hash_table:
            if len(element) != 0:
                for sub_element in element:
                    result.append(sub_element[0])
        return result

    def values(self):
        result = []
        for element in self.hash_table:
            if len(element) != 0:
                for sub_element in element:
                    result.append(sub_element[1])
        return result

    def pop(self, key):
        hash_of_key = hash(key)
        index = hash_of_key & (self.size_of_table - 1)
        if len(self.hash_table[index]) == 0:
            return
        for element in self.hash_table[index]:
            if element[2] == hash_of_key:
                if element[0] == key:
                    self.hash_table[index].remove(element)
                    self.degree_of_occupancy -= 1
                    return element[1]
