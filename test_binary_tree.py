import unittest
from binary_tree import BinaryTree
from tree_unit import TreeUnit


class TestBinaryTree(unittest.TestCase):
    def test_init(self):
        tree = BinaryTree()
        self.assertIsNone(tree.root)

    def test_insert(self):
        tree = BinaryTree()
        tree.insert(19, 1)
        tree.insert(10, 1)
        tree.insert(20, 1)
        tree.insert(7, 1)
        tree.insert(11, 1)
        tree.insert(12, 1)
        self.assertEqual(tree.root.key, 19)
        self.assertEqual(tree.root.left.key, 10)
        self.assertEqual(tree.root.right.key, 20)

    def test_find_none_first(self):
        tree = BinaryTree()
        self.assertIsNone(tree.find('key'))

    def test_find_none_second(self):
        tree = BinaryTree()
        tree.insert(10, 1)
        result_1 = tree.find(20)
        result_2 = tree.find(5)
        self.assertIsNone(result_1)
        self.assertIsNone(result_2)

    def test_find(self):
        tree = BinaryTree()
        tree.insert(19, 1)
        tree.insert(10, 1)
        tree.insert(20, 1)
        tree.insert(7, 1)
        tree.insert(11, 1)
        tree.insert(12, 1)
        result = tree.find(12)
        self.assertIsInstance(result, TreeUnit)
        self.assertEqual(result.key, 12)
        self.assertEqual(result.value, 1)

    def test_remove_with_only_right_sub(self):
        tree = BinaryTree()
        tree.insert(19, 1)
        tree.insert(8, 1)
        tree.insert(10, 1)
        tree.insert(20, 1)
        tree.insert(7, 1)
        tree.insert(11, 1)
        tree.insert(12, 1)
        tree.remove(8)
        self.assertEqual(tree.root.left.key, 10)
        self.assertEqual(tree.root.left.parent.key, 19)

    def test_remove_with_only_right_sub_2(self):
        tree = BinaryTree()
        tree.insert(19, 1)
        tree.insert(30, 1)
        tree.insert(20, 1)
        tree.insert(31, 1)
        tree.insert(32, 1)
        tree.remove(30)
        self.assertEqual(tree.root.right.key, 31)
        self.assertEqual(tree.root.right.parent.key, 19)

    def test_remove_right_leaf(self):
        tree = BinaryTree()
        tree.insert(19, 1)
        tree.insert(8, 1)
        tree.insert(10, 1)
        tree.remove(10)
        self.assertEqual(tree.root.left.key, 8)
        self.assertEqual(tree.root.left.parent.key, 19)

    def test_remove_left_leaf(self):
        tree = BinaryTree()
        tree.insert(19, 1)
        tree.insert(8, 1)
        tree.insert(6, 1)
        tree.remove(6)
        self.assertEqual(tree.root.left.key, 8)
        self.assertEqual(tree.root.left.parent.key, 19)

    def test_remove_except(self):
        tree = BinaryTree()
        try:
            tree.remove('zhe')
        except Exception as error:
            self.assertRaises(Exception, error)

    def test_get_leftmost(self):
        tree = BinaryTree()
        tree.insert(19, 1)
        tree.insert(18, 1)
        tree.insert(17, 1)
        result = tree.get_leftmost(tree.root)
        self.assertEqual(result.key, 17)

    def test_remove_with_leftmost(self):
        tree = BinaryTree()
        tree.insert(19, 1)
        tree.insert(8, 1)
        tree.insert(30, 1)
        tree.insert(20, 1)
        tree.insert(35, 1)
        tree.insert(37, 1)
        tree.insert(34, 1)
        tree.insert(33, 1)
        tree.remove(30)
        res = tree.find(34)
        self.assertEqual(tree.root.right.key, 33)
        self.assertEqual(tree.root.right.parent.key, 19)
        self.assertEqual(tree.root.right.right.key, 35)
        self.assertIsNone(res.left)

    def test_remove_with_leftmost2(self):
        tree = BinaryTree()
        tree.insert(19, 1)
        tree.insert(8, 1)
        tree.insert(30, 1)
        tree.insert(20, 1)
        tree.insert(38, 1)
        tree.insert(40, 1)
        tree.insert(35, 1)
        tree.insert(33, 1)
        tree.insert(34, 1)
        tree.remove(30)
        res = tree.find(35)
        self.assertEqual(tree.root.right.key, 33)
        self.assertEqual(tree.root.right.parent.key, 19)
        self.assertEqual(res.left.key, 34)

    def test_other_case(self):
        tree = BinaryTree()
        tree.insert(20, 1)
        tree.insert(8, 1)
        tree.insert(15, 1)
        tree.insert(9, 1)
        tree.insert(16, 1)
        tree.remove(8)
        self.assertEqual(tree.root.left.key, 15)
        self.assertEqual(tree.root.left.parent.key, 20)

    def test_other_case2(self):
        tree = BinaryTree()
        tree.insert(5, 1)
        tree.insert(8, 1)
        tree.insert(15, 1)
        tree.insert(9, 1)
        tree.insert(16, 1)
        tree.remove(8)
        self.assertEqual(tree.root.right.key, 15)
        self.assertEqual(tree.root.right.parent.key, 5)

    def test_other_case3(self):
        tree = BinaryTree()
        tree.insert(20, 1)
        tree.insert(8, 1)
        tree.insert(6, 1)
        tree.insert(4, 1)
        tree.insert(7, 1)
        tree.remove(8)
        self.assertEqual(tree.root.left.key, 6)
        self.assertEqual(tree.root.left.parent.key, 20)

    def test_other_case4(self):
        tree = BinaryTree()
        tree.insert(3, 1)
        tree.insert(8, 1)
        tree.insert(6, 1)
        tree.insert(4, 1)
        tree.insert(7, 1)
        tree.remove(8)
        self.assertEqual(tree.root.right.key, 6)
        self.assertEqual(tree.root.right.parent.key, 3)


if __name__ == '__main__':
    unittest.main()
