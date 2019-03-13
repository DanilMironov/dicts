from painter import Painter


class DataParser:
    def __init__(self):
        self.names = {'LinearArrayDict', 'BinaryArrayDict', 'TreeDict',
                      'BalancedTreeDict', 'HashTableDict', 'StandardDict'}
        self.operations = ['add', 'pop', 'get', 'items']
        self.list_of_quantity = ['300', '600', '1200', '2400', '4800']

    def parse_results(self):
        result_dict = {}
        for operation in self.operations:
            result_dict[operation] = {}
            for name in self.names:
                result_dict[operation][name] = {}
                for size in self.list_of_quantity:
                    result_dict[operation][name][size] = 0
        with open('result.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            lines = [line[:-1] for line in lines if line != '\n']
            for line in lines:
                splitted_line = line.split(' ')
                name = splitted_line[1][:-1]
                operation = splitted_line[3][:-1]
                data_length = splitted_line[7][:-1]
                time = float(splitted_line[9])
                result_dict[operation][name][data_length] = time
        return result_dict


if __name__ == '__main__':
    dp = DataParser()
    res = dp.parse_results()
    painter = Painter(res)
    painter.draw()
