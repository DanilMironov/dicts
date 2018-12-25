import unittest
from balanced_tree_unit import BalancedTreeUnit


class TestBalancedTreeUnit(unittest.TestCase):
    def test_init(self):
        unit = BalancedTreeUnit('key', 'value')
        self.assertEqual(unit.value, 'value')
        self.assertEqual(unit.key, 'key')

    def test_copy(self):
        unit = BalancedTreeUnit('key', 'value')
        copy_unit = unit.copy()
        self.assertEqual(unit.value, copy_unit.value, 'value')
        self.assertEqual(unit.key, copy_unit.key)


if __name__ == '__main__':
    unittest.main()
