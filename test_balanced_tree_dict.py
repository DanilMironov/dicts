import unittest
from balanced_tree_dict import BalancedTreeDict
from balanced_tree import BalancedTree


class TestBalancedTreeDict(unittest.TestCase):
    def test_init(self):
        balanced_dict = BalancedTreeDict()
        self.assertIsInstance(balanced_dict._tree, BalancedTree)

    def test_add(self):
        balanced_dict = BalancedTreeDict()
        balanced_dict.add('key', 'value')
        self.assertEqual(balanced_dict._tree.tree_root.value, 'value')

    def test_get(self):
        balanced_dict = BalancedTreeDict()
        balanced_dict.add('key', 'value')
        self.assertEqual(balanced_dict.get('key'), 'value')

    def test_items(self):
        balanced_dict = BalancedTreeDict()
        balanced_dict.add(1, 'value1')
        balanced_dict.add(2, 'value2')
        balanced_dict.add(3, 'value3')
        result = balanced_dict.items()
        self.assertTrue((1, 'value1') in result)
        self.assertTrue((2, 'value2') in result)
        self.assertTrue((3, 'value3') in result)

    def test_values(self):
        balanced_dict = BalancedTreeDict()
        balanced_dict.add(1, 'value1')
        balanced_dict.add(2, 'value2')
        balanced_dict.add(3, 'value3')
        result = balanced_dict.values()
        self.assertTrue('value1' in result)
        self.assertTrue('value2' in result)
        self.assertTrue('value3' in result)

    def test_keys(self):
        balanced_dict = BalancedTreeDict()
        balanced_dict.add(1, 'value1')
        balanced_dict.add(2, 'value2')
        balanced_dict.add(3, 'value3')
        result = balanced_dict.keys()
        self.assertTrue(1 in result)
        self.assertTrue(2 in result)
        self.assertTrue(3 in result)

    def test_pop(self):
        balanced_dict = BalancedTreeDict()
        balanced_dict.add(1, 'value1')
        balanced_dict.add(2, 'value2')
        balanced_dict.add(3, 'value3')
        self.assertEqual(balanced_dict.pop(3), 'value3')


if __name__ == '__main__':
    unittest.main()
