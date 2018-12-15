import unittest
from binary_tree_dict import TreeDict
from binary_tree import BinaryTree


class TestTreeDict(unittest.TestCase):
    def test_init(self):
        binary_tree_dic = TreeDict()
        self.assertIsInstance(binary_tree_dic._tree, BinaryTree)

    def test_add(self):
        binary_tree_dic = TreeDict()
        binary_tree_dic.add(1, 'value')
        self.assertEqual(binary_tree_dic._tree.root.value, 'value')
        self.assertEqual(binary_tree_dic._tree.root.key, 1)

    def test_pop(self):
        binary_tree_dic = TreeDict()
        binary_tree_dic.add(1, 'value')
        binary_tree_dic.add(2, 'value2')
        result = binary_tree_dic.pop(2)
        self.assertEqual(result, 'value2')

    def test_get(self):
        binary_tree_dic = TreeDict()
        binary_tree_dic.add(1, 'value')
        binary_tree_dic.add(2, 'value2')
        result = binary_tree_dic.get(1)
        self.assertEqual(result, 'value')

    def test_items(self):
        binary_tree_dic = TreeDict()
        binary_tree_dic.add(1, 'value')
        binary_tree_dic.add(2, 'value2')
        binary_tree_dic.add(0, 'value3')
        result = binary_tree_dic.items()
        self.assertEqual(result, [(1, 'value'), (2, 'value2'), (0, 'value3')])

    def test_values(self):
        binary_tree_dic = TreeDict()
        binary_tree_dic.add(1, 'value')
        binary_tree_dic.add(2, 'value2')
        binary_tree_dic.add(0, 'value3')
        result = binary_tree_dic.values()
        self.assertEqual(result, ['value', 'value2', 'value3'])

    def test_keys(self):
        binary_tree_dic = TreeDict()
        binary_tree_dic.add(1, 'value')
        binary_tree_dic.add(2, 'value2')
        binary_tree_dic.add(0, 'value3')
        result = binary_tree_dic.keys()
        self.assertEqual(result, [1, 2, 0])


if __name__ == '__main__':
    unittest.main()
