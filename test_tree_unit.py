import unittest
from tree_unit import TreeUnit


class TestTreeUnit(unittest.TestCase):
    def test_init(self):
        unit = TreeUnit('key', 'value')
        self.assertEqual(unit.key, 'key')
        self.assertEqual(unit.value, 'value')

    def test_copy(self):
        unit = TreeUnit('key', 'value')
        copied_unit = unit.copy()
        self.assertEqual(copied_unit.value, 'value')
        self.assertEqual(copied_unit.key, 'key')
