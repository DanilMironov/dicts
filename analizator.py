from timeit import default_timer


class Analizator:
    def __init__(self, dictionary, data: list, dict_type: str,
                 operation: str, is_standard=False):
        self.dict = dictionary
        self.data = data
        self.count_of_data = 300
        self.result = {}
        self.is_standard_dict = is_standard
        self.operation = operation
        self.dict_type = dict_type

    def dictionary_init(self):
        for i in range(self.count_of_data):
            self.dict.add(self.data[i][:-1], 1)

    def standard_dict_init(self):
        for i in range(self.count_of_data):
            self.dict[self.data[i][:-1]] = 1

    def make_add(self):
        if self.is_standard_dict:
            start = default_timer()
            self.dict['test'] = 1
            end = default_timer()
            self.dict.pop('test')
            return end - start
        start = default_timer()
        self.dict.add('test', 1)
        end = default_timer()
        self.dict.pop('test')
        return end - start

    def make_pop(self):
        if self.is_standard_dict:
            self.dict['test'] = 1
        else:
            self.dict.add('test', 1)
        start = default_timer()
        self.dict.pop('test')
        end = default_timer()
        return end - start

    def make_get(self):
        if self.is_standard_dict:
            self.dict['test'] = 1
            start = default_timer()
            self.dict['test']
            end = default_timer()
            self.dict.pop('test')
            return end - start
        self.dict.add('test', 1)
        start = default_timer()
        self.dict.get('test')
        end = default_timer()
        self.dict.pop('test')
        return end - start

    def make_items(self):
        start = default_timer()
        self.dict.items()
        end = default_timer()
        return end - start

    def define_operation(self):
        if 'add' in self.operation.lower():
            return self.make_add
        if 'pop' in self.operation.lower():
            return self.make_pop
        if 'get' in self.operation.lower():
            return self.make_get
        if 'items' in self.operation.lower():
            return self.make_items

    def analyze(self):
        current_operation = self.define_operation()
        for i in range(5):
            if self.is_standard_dict:
                self.standard_dict_init()
            else:
                self.dictionary_init()
            res_time = 0
            n = 100
            for j in range(n):
                res_time += current_operation()
            average_result = res_time / n
            self.result[self.count_of_data] = average_result
            self.count_of_data *= 2
        with open('result.txt', 'a') as file:
            for element in self.result.items():
                file.write('Type: ' + self.dict_type
                           + '. Operation: ' + self.operation
                           + '. Count of data: ' + str(element[0])
                           + '. Time: ' + str(element[1]) + '\r\n')
            file.write('\r\n')
