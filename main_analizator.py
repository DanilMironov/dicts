from analizator import Analizator
from hash_table_dict import HashTableDict
from balanced_tree_dict import BalancedTreeDict
from binary_tree_dict import TreeDict
from the_simpliest_dict import LinearArray


class MainAnalizator:
    @staticmethod
    def main():
        with open('words.txt', 'r', encoding='utf-8') as file:
            data = file.readlines()
        test_list = ['add', 'pop', 'get', 'items']
        simpliest_dict = LinearArray()
        for i in range(len(test_list)):
            analizator = Analizator(simpliest_dict, data,
                                    'LinearArrayDict', test_list[i])
            analizator.analyze()
        tree_dict = TreeDict()
        for i in range(len(test_list)):
            tree_analizator = Analizator(tree_dict, data,
                                         'TreeDict', test_list[i])
            tree_analizator.analyze()
        balanced_tree_dict = BalancedTreeDict()
        for i in range(len(test_list)):
            balanced_tree_analizator = Analizator(balanced_tree_dict, data,
                                                  'BalancedTreeDict',
                                                  test_list[i])
            balanced_tree_analizator.analyze()
        hash_table_dict = HashTableDict()
        for i in range(len(test_list)):
            hash_analizator = Analizator(hash_table_dict, data,
                                         'HashTableDict', test_list[i])
            hash_analizator.analyze()
        standard_dict = dict()
        for i in range(len(test_list)):
            standard_analizator = Analizator(standard_dict, data,
                                             'StandardDict', test_list[i],
                                             True)
            standard_analizator.analyze()


if __name__ == '__main__':
    MainAnalizator.main()
