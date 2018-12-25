import unittest
from balanced_tree import BalancedTree
from balanced_tree_unit import BalancedTreeUnit


class TestBalancedTree(unittest.TestCase):
    def test_init(self):
        tree = BalancedTree()
        self.assertIsNone(tree.tree_root)

    def test_insert(self):
        tree = BalancedTree()
        tree.insert(6, '6')
        tree.insert(3, '3')
        tree.insert(2, '2')
        tree.insert(10, '10')
        tree.insert(15, '15')
        self.assertEqual(tree.tree_root.right.value, '10')
        self.assertEqual(tree.tree_root.value, '3')
        self.assertEqual(tree.tree_root.left.value, '2')

    def test_find_none(self):
        tree = BalancedTree()
        res = tree.find('key')
        self.assertIsNone(res)

    def test_find_none2(self):
        tree = BalancedTree()
        tree.insert(3, '3')
        tree.insert(4, '4')
        res = tree.find(5)
        self.assertIsNone(res)

    def test_find_none3(self):
        tree = BalancedTree()
        tree.insert(6, '6')
        tree.insert(4, '4')
        tree.insert(8, '8')
        tree.insert(3, '3')
        res = tree.find(1)
        self.assertIsNone(res)

    def test_find(self):
        tree = BalancedTree()
        tree.insert(1, '1')
        res = tree.find(1)
        self.assertEqual(res.value, '1')

    def test_remove_exception(self):
        tree = BalancedTree()
        try:
            tree.remove('zhh')
        except Exception as error:
            self.assertRaises(Exception, error)

    def test_remove_right_leaf(self):
        tree = BalancedTree()
        tree.insert(2, '2')
        tree.insert(1, '1')
        tree.insert(3, '3')
        res = tree.remove(3)
        self.assertEqual(res.value, '3')

    def test_remove_left_leaf(self):
        tree = BalancedTree()
        tree.insert(2, '2')
        tree.insert(1, '1')
        tree.insert(3, '3')
        res = tree.remove(1)
        self.assertEqual(res.value, '1')

    def test_remove_right_sub_is_none(self):
        tree = BalancedTree()
        tree.insert(3, '3')
        tree.insert(2, '2')
        tree.insert(10, '10')
        tree.insert(6, '6')
        res = tree.remove(10)
        self.assertEqual(res.value, '10')
        self.assertEqual(tree.tree_root.right.value, '6')

    def test_remove_right_sub_is_none2(self):
        tree = BalancedTree()
        tree.insert(6, '6')
        tree.insert(4, '4')
        tree.insert(8, '8')
        tree.insert(3, '3')
        res = tree.remove(4)
        self.assertEqual(res.value, '4')
        self.assertEqual(tree.tree_root.left.value, '3')

    def test_remove_with_both(self):
        tree = BalancedTree()
        tree.insert(3, '3')
        tree.insert(2, '2')
        tree.insert(10, '10')
        tree.insert(6, '6')
        tree.insert(15, '15')
        res = tree.remove(10)
        self.assertEqual(tree.tree_root.right.value, '15')
        self.assertEqual(res.value, '10')

    def test_remove_with_both2(self):
        tree = BalancedTree()
        tree.insert(6, '6')
        tree.insert(2, '2')
        tree.insert(12, '12')
        tree.insert(1, '1')
        tree.insert(3, '3')
        tree.insert(9, '9')
        tree.insert(16, '16')
        tree.insert(14, '14')
        res = tree.remove(12)
        self.assertEqual(tree.tree_root.right.value, '14')
        self.assertIsInstance(res, BalancedTreeUnit)


if __name__ == '__main__':
    unittest.main()
